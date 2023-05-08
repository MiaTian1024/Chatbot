from chatbot_web import app
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for


@app.route("/")
def home():
    return render_template("homepage.html")