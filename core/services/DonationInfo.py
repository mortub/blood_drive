class DonationInfo:
    LIST_OF_FIELDS = ['DateDonation', 'FromHour', 'ToHour', 'Name', 'City', 'Street', 'NumHouse', 'AccountType']

    def __init__(self, donation: dict):
        self.__set_donation_fields(donation)

    def __set_donation_fields(self, donation: dict):
        [self.__set_donation_field(donation_field_name, donation) for donation_field_name in self.LIST_OF_FIELDS]

    def __set_donation_field(self, donation_field_name: str, donation: dict):
        if donation_field_name not in donation:
            donation[donation_field_name] = ''
        self.__dict__[donation_field_name] = donation[donation_field_name]

    def __repr__(self):
        class_string ='{'
        for field in self.LIST_OF_FIELDS:
            class_string += f'''{field}: {self.__dict__[field]};'''
        class_string = class_string[:-1] + '}'
        return class_string
