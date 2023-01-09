from .Donation import Donation


class DonationsFilter:
    async def get_donations_filter(skip: int = 0, limit: int = 100, city: str | None = None, distance: float | None = None ):
        # TODO: add validations - if city exist - is it from the list of possible cities?
        donation = Donation()
        donations_list = donation.get_donations()
        filtered_donations_list = []
        filtering_fields = {
            'city': city
        }
        #TODO: do it for all filtering_fields fields in a loop
        filtered_donations_list = DonationsFilter.filter_according_to_field(donations_list, "city", filtering_fields['city'])

        return {"skip": skip, "limit": limit, "result": filtered_donations_list}

    #TODO: make private
    def filter_according_to_field(donations_list, filtering_field_key ,filtering_field_value):
        filtered_donations_list = []
        for donation in donations_list:
            donation_field = getattr(donation, filtering_field_key)
            if filtering_field_value in donation_field or filtering_field_value in donation.name:
                filtered_donations_list.append(donation)
        return filtered_donations_list

    #TODO: do this line with try catch:  donation_field = getattr(donation, filtering_field_key)
    def get_donation_att():
        pass
    # for name in 'a', 'b', 'c':
    # try:
    #     thing = getattr(obj, name)
    # except AttributeError:
    #     pass
    # else:
        # break