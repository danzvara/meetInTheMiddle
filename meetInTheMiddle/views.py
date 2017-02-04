from flask import render_template
from meetInTheMiddle import app
from Meet import *
import json

@app.route('/')
def index():
    meet = Meet()
    flightA = flight.Flight("uk", "gbp", "en-GB", "LON", "everywhere", "anytime", "anytime")
    flightB = flight.Flight("uk", "gbp", "en-GB", "BTS", "everywhere", "anytime", "anytime")

    return render_template('hello.html', name='jano')
