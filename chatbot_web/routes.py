from chatbot_web import app
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
import sys
from chatbot_web import chatbot
import threading
import os


@app.route("/",methods=["GET", "POST"])
def home():
    dashboard=[]
    if request.method == 'POST':
        question = request.form.get('question')
        dashboard.append(question)
        print(question)
        answer = chatbot.get_response(question)
        dashboard.append(answer)
        print(answer)
        print(dashboard)
        return render_template("homepage.html", dashboard=dashboard, question=question, answer=answer)
    return render_template("homepage.html")
