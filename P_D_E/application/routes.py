from turtle import pd
from application import app
from flask import render_template, url_for, request
import pandas as pd
import json
import plotly
import plotly_express as px

import sys

sys.path.append("../")
from P_D_E.application.getcounters import counter
from P_D_E.application.best_players import getbestplayers
from bluered import *


@app.route('/GetCounters', methods=['POST'])
def callback_counter(champion):
    counter_name = []
    counter_golds =[]
    iscountered_name = []
    iscountered_golds = []

    iscountered_name, iscountered_golds, counter_name, counter_golds =  counter(champion)

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

@app.route("/Counters", methods=['get','post'])
def Counters():

    champion_search = request.form.to_dict()

    counter_name = []
    counter_golds =[]
    iscountered_name = []
    iscountered_golds =[]

    if "counters" in champion_search:
        iscountered_name, iscountered_golds, counter_name, counter_golds =   counter(champion_search["counters"])
    else:
        iscountered_name, iscountered_golds, counter_name, counter_golds =   counter("")


    
    if len(counter_name) == 0:
        champs_counter_str = " "
    else:
        champs_counter_str = champion_search["counters"] + " is countered by : "

    for champs_1 in counter_name:
        champs_counter_str += champs_1 + " ."


    
    if len(iscountered_name) == 0:
        champs_countered_str = " "
    else:
        champs_countered_str = champion_search["counters"] + "  counter : "


    for champs in iscountered_name:
        champs_countered_str += champs + " ." 

    return render_template("counters.html", champion=champs_countered_str, champion_1 = champs_counter_str)


@app.route("/Dashboard")
def Dashboard():
    bestplayers = getbestplayers()
    return render_template("index.html", title = "Home")


@app.route("/blue-red")
def stats_blue_red():
    stats = stats_blue()

    print(stats)    
    return render_template("blue-red.html", title = "Home")


