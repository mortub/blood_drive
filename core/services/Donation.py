import requests
import json
from .DonationDomain import DonationDomain


class Donation:
    def get_donations(self):
        with open('core\services\mada_response.json', 'r', encoding='utf-8') as read_file:
            data = json.load(read_file)
            read_file.close()
        return self.__get_donations_info(data)

    def __get_donations_info(self, data: dict):
        if data['Success']:
            donations = data['Result'].strip('][').split('},')
            result = map(self.__get_donation_info, donations)
            return result
        return None

    def __get_donation_info(self, donation_string: str):
        donation = json.loads(
            donation_string) if donation_string[-1] == '}' else json.loads(donation_string + '}')
        donation_info = DonationDomain(donation)
        return donation_info

    def __fetch_donation_info():
        URL = "https://www.mdais.org/umbraco/api/invoker/execute"
        headers = {'Content-type': 'application/json',
                   'Accept': 'application/json, text/plain, */*', 'Accept-language': 'he',
                   'Content-length': '122', 'Origin': 'https://www.mdais.org',
                   'Referer': 'https://www.mdais.org/blood-donation'}
        body = {"RequestHeader": {"Application": 101, "Module": "BloodBank",
                                  "Function": "GetAllDetailsDonations", "Token": ""}, "RequestData": ""}
        return requests.post(URL, json=body, headers=headers)
