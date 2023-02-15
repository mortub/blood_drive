from neo4j import GraphDatabase
from ..services.DonationDomain import DonationDomain
from ..models.SettlementModel import SettlementModel

class SettlementRepository:
    def __init__(self, driver):
        self.driver = driver

    def create(self, donation: DonationDomain):
        with self.driver.session() as session:
            tx = session.begin_transaction()
            settlement = SettlementModel.create(tx, donation)
            tx.commit()
            return settlement