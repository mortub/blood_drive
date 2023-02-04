from neo4j import GraphDatabase
from ..services.DonationDomain import DonationDomain
from ..models.DonationModel import DonationModel

class DonationRepository:
    def __init__(self, driver):
        self.driver = driver

    def create(self, donation: DonationDomain):
        with self.driver.session() as session:
            tx = session.begin_transaction()
            donation = DonationModel.create(tx, donation)
            tx.commit()
            return donation
