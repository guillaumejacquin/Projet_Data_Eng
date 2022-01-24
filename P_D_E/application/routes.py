from turtle import pd
from application import app
from flask import render_template, url_for
import pandas as pd
import json
import plotly
import plotly_express as px

@app.route("/")
def index():

    # first graph
    # df = px.data//
    # fig1 = //
    #graphjson

    return render_template("index.html", title = "Home")