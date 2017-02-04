from meetInTheMiddle import app
from Meet import *
import json

@app.route('/')
def index():
    meet = Meet()
    flightA = flight.Flight("uk", "gbp", "en-GB", "LON", "everywhere", "anytime", "anytime")
    flightB = flight.Flight("uk", "gbp", "en-GB", "BTS", "everywhere", "anytime", "anytime")

    
    return json.dumps(meet._get_flight(flightA, flightB))


