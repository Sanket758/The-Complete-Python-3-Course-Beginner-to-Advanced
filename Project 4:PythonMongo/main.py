import pymongo
from pymongo import MongoClient
import datetime

# syntax MongoClient(host, port), default host is localhost default port is 27017
client = MongoClient()

# Connecting to a database called myfirstdb
db = client.myfirstdb

# In mongo table is called collections
users = db.users

# create a variable to insert into database
user1 = {"username": "Sanku", "password": "mypass", "favourite food": "frankiiee", "hobbies": ["python", "ML", "AI"]}

# Whenever new entry is done to our database it returns a ID using which we can find our data
user_id = users.insert_one(user1).inserted_id
print(user_id)

'''
For Bulk Insert -->
user2 = [{"username": "Senki222", "password": 1223}{"username": "Senku333", "password": 12233555}]
insterted = users.insert_many(user2)

and then for showing the id's of those objects
print(inserted.inserted_id)
'''

# To find something in the Database
# Lets find how many entries do we have in our database
print("how many records:", users.find().count())
# and That's it

# to find data with specific condition
print("how many Sanku:", users.find({"username": "Sanku"}).count())

# Multiple Find Conditions
print("number of people with username sanku", users.find({"username": "Sanku", "favourite food": "frankiiee"}).count())
# as you can see you just need to pass multiple arguments in dictionary and you are done.

# Working with the dates
current_date = datetime.datetime.now()
old_date = datetime.datetime(2009, 8, 11)

uid = users.insert({"username": "Senku122", "date": current_date})
print("users who has date greater than old date:", users.find({"date": {"$gt": old_date}}).count())
# This will return the records which has date greater than old_date

print(users.find({"date": {"$exists": True}}).count())

# Creating indexes
result = db.users.create_index([("username", pymongo.ASCENDING)])
print(result)
