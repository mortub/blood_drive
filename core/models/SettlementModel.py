from neo4j import GraphDatabase
from ..services.DonationDomain import DonationDomain
from ..utils.datasources.SettlementsDatasource import SettlementsDatasource

class SettlementModel():
    @staticmethod
    def create(tx, donation: DonationDomain):
        try:
            settlement_name = SettlementModel.__extract_settlement_name_from_donation(donation)
            return SettlementsDatasource.get_settlement_by_name(settlement_name)
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            return

    @classmethod
    def __extract_settlement_name_from_donation(cls, donation: DonationDomain):
        settlement_name = donation.__dict__['City']
        if not settlement_name or settlement_name == None:
            raise Exception("City not provided in donation")
        settlement_name = (settlement_name + ' ').replace(' ', '%20')
        return settlement_name
