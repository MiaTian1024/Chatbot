from flask import Flask

app=Flask(__name__)

from chatbot_web import routes
from chatbot_web import chatbot

