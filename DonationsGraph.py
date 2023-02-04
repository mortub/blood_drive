from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable
import os
from dotenv import load_dotenv

load_dotenv()

class DonationsGraph:
    def __init__(self):
        uri = os.getenv('NEO4J_URI')
        user = os.getenv('NEO4J_USER')
        password = os.getenv('NEO4J_PASSWORD')
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    @property
    def driver(self):
        return self._driver

    def close(self):
        self.driver.close()



