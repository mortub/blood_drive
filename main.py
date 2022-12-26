from typing import Union
from fastapi import FastAPI

from core.services.Donation import Donation
app = FastAPI()


@app.get("/")
def read_root():
    donation = Donation()
    res = donation.get_donations()
    return {"Hello": res}
