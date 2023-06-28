from flask import Flask
from flask_socketio import SocketIO
from flask_mail import Mail
import pymysql
import config
import openai

app = Flask(__name__)
app.config.update(config.props)
mail = Mail(app)
socketIO = SocketIO(app)

openai.api_key = config.props["API_KEY"]

db = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    database='devarx'
)

from routes import *

if __name__ == '__main__':
   socketIO.run(app, debug=True)
