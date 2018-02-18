import os
import socket
from flask import Flask, redirect, url_for, request, render_template
from pymodm import connect, MongoModel, fields

app = Flask(__name__)
mongo_uri = 'mongodb://{}:{}/docker_app'.format(os.environ['MONGODB_HOST'], os.environ['MONGODB_PORT'])
connect(mongo_uri)

class Todos(MongoModel):
    title = fields.CharField(max_length=100)
    created_on = fields.DateTimeField()
    updated_on = fields.DateTimeField()

@app.route('/api/todos')
def todos(self):
    return []
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)