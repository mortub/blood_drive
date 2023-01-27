from ..Donation import Donation
from .DonationsFilterStrategy import DonationsFilterStrategy
from .enums import FiteringFields

class DonationsFilter:
    filtering_fields = {}
    async def get_donations_filter(skip: int = 0, limit: int = 100, city: str | None = None, dates_range: str | None = None):
        donations_list = Donation().get_donations()
        DonationsFilter.filtering_fields = {
            FiteringFields.CITY.value: city,
            FiteringFields.DATES_RANGE.value: dates_range
        }

        filtered_donations_list = DonationsFilter.__filter_according_to_field(donations_list)
        return {"skip": skip, "limit": limit, "result": filtered_donations_list}

    def __filter_according_to_field(donations_list: list[dict]):
        filtered = filter(DonationsFilter.__get_filtered_donation, donations_list)
        return list(filtered)

    def __get_filtered_donation(donation: dict):
        response = True
        for key in DonationsFilter.filtering_fields:
            value = DonationsFilter.filtering_fields[key]
            func_name = key + '_filter'
            func = getattr(DonationsFilterStrategy,func_name,DonationsFilterStrategy.func_not_found)
            result = func(value, donation)
            response = result and response
        return response