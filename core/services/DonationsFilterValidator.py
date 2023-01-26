from datetime import datetime

class DonationsFilterValidator:
    @staticmethod
    def dates_range_filter_validation(user_dates_range):
        first_date, _ , second_date = user_dates_range.partition(' - ')
        try:
            format_str = '%Y-%m-%d'
            datetime.strptime(first_date, format_str)
            datetime.strptime(second_date, format_str)
        except ValueError:
            raise ValueError('Incorrect data format, should be YYYY-MM-DD')

