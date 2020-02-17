"""
Whenever a new user registers the data must be stored into the data base.
We are using mongodb as database.
This File contains the model for register class which is ultimately the registration page of our html
"""
import pymongo
from pymongo import MongoClient
import bcrypt


# Create a class for our model
class RegisterModel:
    def __init__(self):
        # mongodb initializations 1.You need to start mongo client, 2.create a collection 3.add entry to the collection
        self.client = MongoClient()
        self.db = self.client.CodersArena
        self.Users = self.db.users

    # Grab and store the information entered by user into database
    def insert_user(self, data):
        # passwords are strings, for security convert them into hashes and then store them
        hashed = bcrypt.hashpw(data.password.encode(), bcrypt.gensalt())
        # insert data into mongodb, every time we make an entry it returns and id for mongo object
        id = self.Users.insert({"username": data.username, "name": data.name, "email": data.email, "password": hashed})
        print('uid is ', id)
