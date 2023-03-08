from application import task_management_db
import pandas as pd

# Open a cursor to perform database operations
collection = task_management_db['mycollection']
column_names = ["createdby", "email", "taskdate", "description", "companyname", "taskstatus"]

df = pd.read_csv('tasks.csv', names=column_names, header=None)

# Convert DataFrame to a dictionary
data_dict = df.to_dict('records')

# Insert data into MongoDB
collection.insert_many(data_dict)


print("db created sucessfully")
