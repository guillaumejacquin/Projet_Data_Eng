from turtle import pd
from application import app
from flask import render_template, url_for
import pandas as pd
import json
import plotly
import plotly_express as px

@app.route("/")
def index():

    return render_template("index.html", title = "Home")

@app.route("/Best Players")
def Best_players():
    

    return render_template("best_players.html", title = "Home")

@app.route("/Counters")
def Counters():
    

    return render_template("counters.html", title = "Home")

@app.route("/Dashboard")
def Dashboard():
    

    return render_template("index.html", title = "Home")