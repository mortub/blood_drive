from fastapi import Depends, FastAPI
from DonationsGraph import DonationsGraph
from core.services.Donation import Donation
from core.services.donations_filter.DonationsFilter import DonationsFilter
from core.repositories.DonationRepository import DonationRepository
from core.repositories.SettlementRepository import SettlementRepository
from core.repositories.DonationSettlementRelationshipRepository import DonationSettlementRelationshipRepository

app = FastAPI()

@app.get("/")
def read_root():
    return {"donations_list": list(Donation().get_donations())}

@app.get("/donations")
def get_donations(filtered_donations: dict = Depends(DonationsFilter().get_donations_filter)):
    return filtered_donations

@app.post("/donation")
def create_donation():
    donation = list(Donation().get_donations())[1]
    donations_graph = DonationsGraph()
    result = DonationRepository(donations_graph.driver).create(donation)
    donations_graph.close()
    return result


@app.post("/settlement")
def create_settlement():
    donation = list(Donation().get_donations())[1]
    donations_graph = DonationsGraph()
    result = SettlementRepository(donations_graph.driver).create(donation)
    donations_graph.close()
    return result


@app.post("/donation_settlement_relationship")
def create_donation_settlement_relationship():
    donation = list(Donation().get_donations())[1]
    donations_graph = DonationsGraph()
    result = DonationSettlementRelationshipRepository(donations_graph.driver).create(donation)
    donations_graph.close()
    return result