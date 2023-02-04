from fastapi import Depends, FastAPI
from DonationsGraph import DonationsGraph
from core.services.Donation import Donation
from core.services.donations_filter.DonationsFilter import DonationsFilter
from core.repositories.DonationRepository import DonationRepository

app = FastAPI()

@app.get("/")
def read_root():
    return {"donations_list": Donation().get_donations()}

@app.get("/donations")
def get_donations(filtered_donations: dict = Depends(DonationsFilter().get_donations_filter)):
    return filtered_donations

@app.post("/donation")
def create_donation():
    donation = list(Donation().get_donations())[0]
    donations_graph = DonationsGraph()
    result = DonationRepository(donations_graph.driver).create(donation)
    donations_graph.close()
    return result
