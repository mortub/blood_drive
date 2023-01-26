
class DonationsFilterStrategy:
    @staticmethod
    def city_filter(user_city, donation):
        if user_city is None : return True
        donation_city = DonationsFilterStrategy.__get_donation_att(donation, 'City')
        if not user_city in donation_city and not user_city in donation.Name:
            return False
        return True

    @staticmethod
    def range_of_dates_filter():
        pass

    def func_not_found():
        print('No Function Found!')

    def __get_donation_att(donation, key):
        try:
            return getattr(donation, key)
        except AttributeError:
            print(f'could not get {key} from {donation}')
            return ''