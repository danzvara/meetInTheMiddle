from flask import render_template
from meetInTheMiddle import app
from Meet import *
from flask import request
import json

meet = Meet()

@app.route('/')
def index():
    flightA = flight.Flight("uk", "gbp", "en-GB", "London", "everywhere",
        "2017-03-27", "2017-04-04")
    flightB = flight.Flight("uk", "gbp", "en-GB", "Bratislava", "everywhere",
        "2017-03-27", "2017-04-04")

    return render_template('hello.html', name='jano')

@app.route('/api/request', methods=['POST'])
def request_flights():
  data = request.json

  flightA = flight.Flight("uk", "gbp", "en-GB", data["fromA"], "everywhere",
        data["outbound"], data["inbound"])
  flightB = flight.Flight("uk", "gbp", "en-GB", data["fromB"], "everywhere",
        data["outbound"], data["inbound"])

  return json.dumps(meet.get_flight(flightA, flightB))
