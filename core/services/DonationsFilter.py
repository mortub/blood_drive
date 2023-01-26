from .Donation import Donation
from .DonationsFilterStrategy import DonationsFilterStrategy

class DonationsFilter:
    filtering_fields = {}
    async def get_donations_filter(skip: int = 0, limit: int = 100, city: str | None = None):
        donations_list = Donation().get_donations()
        DonationsFilter.filtering_fields = {
            'city': city
        }

        filtered_donations_list = DonationsFilter.__filter_according_to_field(donations_list)
        return {"skip": skip, "limit": limit, "result": filtered_donations_list}

    def __filter_according_to_field(donations_list):
        filtered = filter(DonationsFilter.__get_filtered_donation, donations_list)
        return list(filtered)

    def __get_filtered_donation(donation):
        response = True
        for key in DonationsFilter.filtering_fields:
            value = DonationsFilter.filtering_fields[key]
            func_name = key + '_filter'
            func = getattr(DonationsFilterStrategy,func_name,DonationsFilterStrategy.func_not_found)
            response = func(value, donation) and response
        return response