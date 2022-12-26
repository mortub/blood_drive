import requests
import json


class DonationInfo:
    def __init__(self, DateDonation, FromHour, ToHour, Name, Street, NumHouse, AccountType):
        self.date_donation = DateDonation
        self.from_hour = FromHour
        self.to_hour = ToHour
        self.name = Name
        self.street = Street
        self.num_house = NumHouse
        self.account_type = AccountType


class Donation:
    def get_donations(self):
        with open('core\services\mada_response.json', 'r', encoding='utf-8') as read_file:
            data = json.load(read_file)
            read_file.close()
        return self.__get_donation_info(data)

    def __get_donation_info(self, data):
        if data['Success']:
            donation = json.loads(
                data['Result'].strip('][').split('},')[0] + '}')
            donation_info = DonationInfo(donation['DateDonation'], donation['FromHour'],
                                         donation['ToHour'], donation['Name'], donation['Street'],
                                         donation['NumHouse'], donation['AccountType'])
            print(donation_info)
            return donation_info
        return None

    def __fatch_donation_info():
        URL = "https://www.mdais.org/umbraco/api/invoker/execute"
        headers = {'Content-type': 'application/json',
                   'Accept': 'application/json, text/plain, */*', 'Accept-language': 'he',
                   'Content-length': '122', 'Origin': 'https://www.mdais.org',
                   'Referer': 'https://www.mdais.org/blood-donation'}
        body = {"RequestHeader": {"Application": 101, "Module": "BloodBank",
                                  "Function": "GetAllDetailsDonations", "Token": ""}, "RequestData": ""}
        return requests.post(URL, json=body, headers=headers)
