from fastapi import Depends, FastAPI
from core.services.Donation import Donation
from core.services.DonationsFilter import DonationsFilter

app = FastAPI()


@app.get("/")
def read_root():
    donation = Donation()
    res = donation.get_donations()
    return {"donations_list": res}

# TODO: add limit + offset for pagination
@app.get("/donations")
def get_donations(filtered_donations: dict = Depends(DonationsFilter().get_donations_filter)):
    return filtered_donations
