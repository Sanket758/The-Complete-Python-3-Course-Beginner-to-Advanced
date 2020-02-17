"""
Whenever a user tries to login LoginModel will be in work.
Every user's password is stored inside the database as hashed string.
So when user logs in compare the hashed password with the entered password after unhashing,
if password is correct then show successful login otherwise alert for invalid login.
"""

import pymongo
import bcrypt
from pymongo import MongoClient


# Create a login model
class LoginModel:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.CodersArena
        self.Users = self.db.users
    
    # Check if password entered by user is correct or not
    def check_user(self, data):
        # Find user by his username
        user = self.Users.find_one({"username": data.username})

        # if user is found
        if user:
            # check if password stored in database matches to the entered one
            if bcrypt.checkpw(data.password.encode(), user['password']):
                return user
            else:
                return False
        else:
            # if password is not found return error
            return 'error'

