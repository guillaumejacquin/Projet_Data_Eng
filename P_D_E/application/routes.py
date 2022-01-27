from turtle import pd
from application import app
from flask import render_template, url_for
import pandas as pd
import json
import plotly
import plotly_express as px

import sys

sys.path.append("../")
from getcounters import counter
from main import getbestplayers
from bluered import *


@app.route('/GetCounters', methods=['POST'])
def callback_counter(champion):
    counter_name = []
    counter_golds =[]
    iscountered_name = []
    iscountered_golds = []

    iscountered_name, iscountered_golds, counter_name, counter_golds =  counter(champion)

=
@app.route("/")
def index():

    return render_template("index.html", title = "Home")

@app.route("/Best Players")
def Best_players():
    
    counter_name = []
    counter_golds =[]
    iscountered_name = []
    iscountered_golds =[]

    iscountered_name, iscountered_golds, counter_name, counter_golds =  counter("zeri")

    # print(iscountered_name, iscountered_golds, counter_name)
    # return render_template("counters.html", title = "Home")
    return render_template("best_players.html", title = "Home")

@app.route("/Counters")
def Counters():
    
    return render_template("counters.html", title = "Home")


@app.route("/Dashboard")
def Dashboard():
    bestplayers = getbestplayers()
    return render_template("index.html", title = "Home")


@app.route("/Blue-Stats")
def Stats():
    stats = stats()

    # print(stats)    
    return render_template("index.html", title = "Home")
