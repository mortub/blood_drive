from .Donation import Donation


class DonationsFilter:
    filtering_fields = {}
    async def get_donations_filter(skip: int = 0, limit: int = 100, city: str | None = None):
        donations_list = Donation().get_donations()
        DonationsFilter.filtering_fields = {
            'City': city
        }

        filtered_donations_list = DonationsFilter.__filter_according_to_field(donations_list)
        return {"skip": skip, "limit": limit, "result": filtered_donations_list}

    def __filter_according_to_field(donations_list):
        filtered = filter(DonationsFilter.__get_filtered_donation, donations_list)
        return list(filtered)

    def __get_filtered_donation(donation):
        for key in DonationsFilter.filtering_fields:
            value = DonationsFilter.filtering_fields[key]
            if value is None : return True
            donation_att = DonationsFilter.__get_donation_att(donation, key)
            if not value in donation_att and not value in donation.Name:
                return False
        return True

    def __get_donation_att(donation, key):
        try:
            return getattr(donation, key)
        except AttributeError:
            print(f'could not get {key} from {donation}')
            return ''
