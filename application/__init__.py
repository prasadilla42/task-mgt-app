import pymongo
import os
# Provide the mongodb localhost url to connect python to mongodb.
mongo_client = pymongo.MongoClient("mongodb+srv://prasadilla:flasktest@tskmgtdb.rvp3u1h.mongodb.net/?retryWrites=true&w=majority")

DATABASE_NAME = "tskmgtdb"
task_management_db = mongo_client[DATABASE_NAME]