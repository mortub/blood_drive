from datetime import datetime

class Dates:
    @staticmethod
    def get_date_in_format(date: str, format: str):
        try:
            return datetime.strptime(date, format)
        except ValueError:
            raise ValueError(f'''Incorrect data format, should be {format} ''')