from neo4j import GraphDatabase
from ..services.DonationDomain import DonationDomain
from ..models.DonationSettlementRelationshipModel import DonationSettlementRelationshipModel

class DonationSettlementRelationshipRepository:
    def __init__(self, driver):
        self.driver = driver

    def create(self, donation: DonationDomain):
        with self.driver.session() as session:
            tx = session.begin_transaction()
            donation_settlement_relationship = DonationSettlementRelationshipModel.create(tx, donation)
            tx.commit()
            return donation_settlement_relationship
