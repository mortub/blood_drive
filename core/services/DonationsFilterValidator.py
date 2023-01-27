from ..utils.dates import Dates

class DonationsFilterValidator:
    @staticmethod
    def dates_range_filter_validation(user_dates_range):
        first_date, _ , second_date = user_dates_range.partition(' - ')
        format_str = '%Y-%m-%d'
        first_date = Dates.get_date_in_format(first_date, format_str)
        second_date = Dates.get_date_in_format(second_date, format_str)
        if first_date > second_date:
            raise ValueError('The first date cannot be after the second date')


