from ..services.DonationDomain import DonationDomain
from fastapi import HTTPException

class DonationSettlementRelationshipModel:
    @staticmethod
    def create(tx, donation: DonationDomain):
        try:
            relationship = DonationSettlementRelationshipModel.__map_relationship_between_donation_domain_and_settlement_model(donation)
            query = '''MATCH
            (d:Donation),
            (s:Settlement)
            WHERE d.name = $donation_name AND s.name = $settlement_name
            CREATE (d)-[r:HAPPENS_IN {street: $donation_street, num_house: $donation_num_house}]->(s)
            return r
            '''
            query_result = tx.run(query,
            {'donation_name': relationship['donation_name'],'settlement_name': relationship['settlement_name'],
            'donation_street': relationship['donation_street'],'donation_num_house': relationship['donation_num_house']})

            result = query_result.single()
            if result == None:
                raise Exception(f'Item not created in the DB ', 500)
            return result
        except Exception as error:
            raise HTTPException(status_code=error.args[1], detail=f'Could not create a relationship between Donation and Settlement, {str(error.args[0])}')

    @classmethod
    def __map_relationship_between_donation_domain_and_settlement_model(cls, donation: DonationDomain):
        return {
            'donation_name': donation.__dict__['Name'].strip(),
            'settlement_name': donation.__dict__['City'].strip(),
            'donation_street': donation.__dict__['Street'].strip(),
            'donation_num_house': donation.__dict__['NumHouse'].strip()
        }