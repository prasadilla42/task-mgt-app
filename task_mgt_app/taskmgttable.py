from bson import ObjectId
from flask import redirect, url_for

from application import task_management_db


class TaskTable(object):
    """
    class to create task table insert and modifications
    """
    def __init__(self):
        self.task_mgt_collection = task_management_db['mycollection']

    def task_table(self):
        """
        return collection table
        """
        return self.task_mgt_collection.find()

    def change_value(self, rowid, new_value):
        self.task_mgt_collection.update_one(
            {"_id": ObjectId(rowid)},
            {"$set": {"taskstatus": new_value}}
        )
        return redirect(url_for('index'))

    def insert_new_data(self, data):
        self.task_mgt_collection.insert_many(data)
        return redirect(url_for('index'))
