from fastapi import Depends, FastAPI
from core.services.Donation import Donation
from core.services.donations_filter.DonationsFilter import DonationsFilter

app = FastAPI()


@app.get("/")
def read_root():
    return {"donations_list": Donation().get_donations()}

@app.get("/donations")
def get_donations(filtered_donations: dict = Depends(DonationsFilter().get_donations_filter)):
    return filtered_donations
