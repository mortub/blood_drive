from neo4j import GraphDatabase
from fastapi import HTTPException
from ..services.DonationDomain import DonationDomain
from ..utils.datasources.SettlementsDatasource import SettlementsDatasource

class SettlementModel():
    @staticmethod
    def create(tx, donation: DonationDomain):
        try:
            settlement =  SettlementModel.__map_between_donation_domain_and_settlement_model(donation)
            query = '''CREATE (s:Settlement { name: $name,
            english_name: $english_name, department: $department, subdistrict: $subdistrict })'''
            result = tx.run(query,
            {"name": settlement['name'], "english_name": settlement['english_name'],
            "department": settlement['department'], "subdistrict": settlement['subdistrict']})
            return settlement
        except Exception as error:
            raise HTTPException(status_code=error.args[1], detail=f'Could not create a Settlement node, {str(error.args[0])}')

    @classmethod
    def __map_between_donation_domain_and_settlement_model(cls, donation: DonationDomain):
        settlement_name = cls.__extract_settlement_name_from_donation(donation)
        settlement_record = SettlementsDatasource.get_settlement_by_name(settlement_name)
        settlement = {
            'name': 'שם_ישוב',
            'english_name': 'שם_ישוב_לועזי',
            'department': 'לשכה',
            'subdistrict' : 'שם_נפה'
        }
        for key, settlement_record_key in settlement.items():
            settlement[key] = cls.__get_settlement_record_value_by_key(settlement_record, settlement_record_key)
        return settlement

    @classmethod
    def __get_settlement_record_value_by_key(cls, settlement_record, key:str):
        try:
            value = settlement_record[key]
            return value.strip()
        except (KeyError):
            raise KeyError(f'{key} not provided in settlement record', 400)

    @classmethod
    def __extract_settlement_name_from_donation(cls, donation: DonationDomain):
        settlement_name = donation.__dict__['City']
        if not settlement_name or settlement_name == None:
            raise KeyError('City not provided in donation', 400)
        settlement_name = (settlement_name + ' ').replace(' ', '%20')
        return settlement_name
