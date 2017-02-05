from flask import render_template
from meetInTheMiddle import app
from meetInTheMiddle.Meet import *
from flask import request
import json

meet = Meet()

@app.route('/')
def index():
    return render_template('hello.html', name='jano')

@app.route('/api/request', methods=['GET'])
def request_flights():
  data = request.args

  flightA = flight.Flight("uk", "gbp", "en-GB", data["fromA"], "everywhere",
        data["outbound"], data["inbound"])
  flightB = flight.Flight("uk", "gbp", "en-GB", data["fromB"], "everywhere",
        data["outbound"], data["inbound"])

  result = meet.get_flight(flightA, flightB)
  if (len(result) > 0):
    return json.dumps(result)
  else:
    return json.dumps([])
