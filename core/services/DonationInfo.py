class DonationInfo:
    list_of_fields = ['DateDonation', 'FromHour', 'ToHour', 'Name', 'City', 'Street', 'NumHouse', 'AccountType']

    def __init__(self, donation):
        self.__set_donation_fields(donation)

    def __set_donation_fields(self, donation):
        [self.__set_donation_field(donation_field_name, donation) for donation_field_name in self.list_of_fields]

    def __set_donation_field(self, donation_field_name, donation):
        if donation_field_name not in donation:
            donation[donation_field_name] = ''
        self.__dict__[donation_field_name] = donation[donation_field_name]

    def __repr__(self):
        class_string ='{'
        for field in self.list_of_fields:
            class_string += f'''{field}: {self.__dict__[field]};'''
        class_string = class_string[:-1] + '}'
        return class_string
