import json

from flask import Flask, render_template, request, redirect, url_for, Response
from task_mgt_app.app import TaskTable

app = Flask(__name__)
table_data = TaskTable()


@app.route('/')
def index():
    data = table_data.task_table()
    return render_template('index.html', csv_data=data)


@app.route("/update_value", methods=['PUT'])
def update_value():
    try:
        updated_value = json.loads(request.get_data().decode('utf-8'))
        table_data.change_value(updated_value["id"], updated_value["new_value"])
        return Response(status=200)
    except Exception as e:
        return str(e)

@app.route("/upload_csv", methods=['POST'])
def update_csv():
    try:
        updated_data = json.loads(request.get_data().decode('utf-8'))
        table_data.insert_new_data(updated_data)
        return "Data inserted successfully"
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
