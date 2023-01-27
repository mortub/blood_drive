from ...utils.Dates import Dates
from .constants import DATES_RANGE_FORMAT

class DonationsFilterValidator:
    @staticmethod
    def dates_range_filter_validation(user_dates_range: str):
        first_date, _ , second_date = user_dates_range.partition(' - ')
        first_date = Dates.get_date_in_format(first_date, DATES_RANGE_FORMAT)
        second_date = Dates.get_date_in_format(second_date, DATES_RANGE_FORMAT)
        if first_date > second_date:
            raise ValueError('The first date cannot be after the second date')


