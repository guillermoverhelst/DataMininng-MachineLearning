import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()


class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(user=os.getenv('USER'), password=os.getenv('PASSWORD'),
                                                  host=os.getenv('HOST'), database=os.getenv('DATABASE'),
                                                  use_pure=False)

        self.cursor = self.connection.cursor()

    def insert(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
        except:
            self.connection.rollback()
