class DonationInfo:
    def __init__(self, DateDonation, FromHour, ToHour, Name, City, Street, NumHouse, AccountType):
        self.date_donation = DateDonation
        self.from_hour = FromHour
        self.to_hour = ToHour
        self.name = Name
        self.city = City
        self.street = Street
        self.num_house = NumHouse
        self.account_type = AccountType

    def __repr__(self):
        return f'''date_donation:{self.date_donation},
        from_hour:{self.from_hour},
        to_hour:{self.to_hour},
        name:{self.name},
        city: {self.city},
        street:{self.street},
        num_house:{self.num_house},
        account_type:{self.account_type}.'''
