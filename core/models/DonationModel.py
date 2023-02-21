from neo4j import GraphDatabase
from ..services.DonationDomain import DonationDomain

class DonationModel():
    @staticmethod
    def create(tx, donation: DonationDomain):
        donation = DonationModel.__map_domain_donation_to_node_donation(donation)
        query = '''CREATE (d:Donation { donation_date: $donation_date,
         from_hour: $from_hour, to_hour: $to_hour, name: $name })'''
        result = tx.run(query,
        {"donation_date": donation['donation_date'], "from_hour": donation['from_hour'],
         "to_hour": donation['to_hour'], "name": donation['name']})
        return result

    @classmethod
    def __map_domain_donation_to_node_donation(cls, donation: DonationDomain):
        return {
            'donation_date': cls.__make_donation_date(donation.__dict__['DateDonation']).strip(),
            'from_hour': donation.__dict__['FromHour'].strip(),
            'to_hour': donation.__dict__['ToHour'].strip(),
            'name' : donation.__dict__['Name'].strip()
        }

    @classmethod
    def __make_donation_date(cls, dateDonation: str):
        return dateDonation.partition('T')[0]
