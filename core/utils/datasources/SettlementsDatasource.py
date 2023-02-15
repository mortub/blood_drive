import requests

class SettlementsDatasource:
    @staticmethod
    def get_settlement_by_name(settlement_name: str):
        URL = f'https://data.gov.il/api/3/action/datastore_search?resource_id=5c78e9fa-c2e2-4771-93ff-7f400a12f7ba&filters={{\"שם_ישוב\":\"{settlement_name}\"}}&limit=1'
        response = requests.get(URL)
        return response.json()['result']['records'][0]