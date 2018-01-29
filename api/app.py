from flask import Flask
from redis import Redis, RedisError
from pymodm import connect
import os
import socket
from models import User
import config

connect(config.MONGO_DB_URL + config.DATABASE_NAME)

redis = Redis(host="redis", port=6379, db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

@app.route('/')
def hello():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>cannot connect to Redis, counter disabled</i>"
    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname} <br/>" \
           "<b>Visits:</b> {visits}"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), visits=visits)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)