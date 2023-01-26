
class DonationsFilterStrategy:
    @staticmethod
    def city_filter(user_city, donation):
        #TODO: validate user_city from a list of cities, have if user_city is None : return True condition in it.
        if user_city is None : return True
        donation_city = DonationsFilterStrategy.__get_donation_att(donation, 'City')
        if not user_city in donation_city and not user_city in donation.Name:
            return False
        return True

    @staticmethod
    def dates_range_filter(user_dates_range, donation):
        #TODO: validate user_dates_range format
        if user_dates_range is None : return True
        first_date, _ , second_date = user_dates_range.partition(' - ')
        donation_date = DonationsFilterStrategy.__get_donation_att(donation, 'DateDonation').partition('T')[0]
        if donation_date < first_date or donation_date > second_date:
            return False
        return True


    def func_not_found():
        print('No Function Found!')

    def __get_donation_att(donation, key):
        try:
            return getattr(donation, key)
        except AttributeError:
            print(f'could not get {key} from {donation}')
            return ''