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

    def selectAll(self):
        data = []
        users = []
        items = []
        ratings = []
        self.cursor.execute("select rating, Users_idUsers, Recipe_idRecipe from rating;")
        rows = self.cursor.fetchall()
        for r in rows:
            ratings.append(r[0])
            users.append(r[1])
            items.append(r[2])
        data.append(users)
        data.append(items)
        data.append(ratings)
        return data