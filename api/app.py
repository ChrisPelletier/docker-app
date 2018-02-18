import os
import socket
from flask import Flask, request, jsonify
from pymodm import connect, MongoModel, fields

app = Flask(__name__)
mongo_uri = 'mongodb://{}:{}/docker_app'.format(os.environ['MONGODB_HOST'], os.environ['MONGODB_PORT'])
connect(mongo_uri)

class Todo(MongoModel):
    title = fields.CharField(max_length=100)
    created_on = fields.DateTimeField()
    updated_on = fields.DateTimeField()

@app.route('/api/todo',methods=["POST"])
def todo():
    if request.method=="POST":
        payload=request.get_json()
        todo=Todo(title=payload["title"]).save()
        resp=jsonify({"title":todo.title})
        resp.status_code=201
        return resp 

@app.route('/api/todos')
def todos():
    return []
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)