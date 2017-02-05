import scanner
from itertools import product
import flight
import time

class Meet:

  def __init__(self):
    pass

  def _chooseBest(self, flightsA, flightsB):
    return 0

  def _clean(self, jobj):
    res = {}
    res["MinPrice"] = jobj["MinPrice"]
    res["Destination"] = jobj["OutboundLeg"]["DestinationId"]
    res["OutTime"] = jobj["OutboundLeg"]["DepartureDate"][0:10]
    res["InTime"] = jobj["InboundLeg"]["DepartureDate"][0:10]

    return res

  def _searchForFlight(self, flightA, flightB):
    sky = scanner.Scanner()
    flightsDano = sky._request(flightA.country, flightA.currency,
                              flightA.locale, flightA.origin, flightA.dest,
                              flightA.outtime, flightA.intime)
    flightsBrch = sky._request(flightB.country, flightB.currency,
                              flightB.locale, flightB.origin, flightB.dest,
                              flightB.outtime, flightB.intime)
    print(flightsDano)
    airportsDano = filter((lambda x: x["Type"] == "Station"), flightsDano["Places"])
    airportsBrch = filter((lambda x: x["Type"] == "Station"), flightsBrch["Places"])
    airports = airportsBrch + airportsDano
    airports_ = {}
    for x in airports:
      airports_[x["PlaceId"]] = {"IataCode":x["IataCode"], "Name":x["Name"]}
    print(airports_)

    flightsBrch = flightsBrch["Quotes"]
    flightsDano = flightsDano["Quotes"]
    cleanDano = map(self._clean, flightsDano)
    cleanBrch = map(self._clean, flightsBrch)

    pairs = list(product(cleanBrch, cleanDano))
    criteria = ["Destination", "OutTime"]
    for crit in criteria:
      pairs = filter((lambda x: x[0][crit] == x[1][crit]), pairs)

    for p in pairs:
      p[0]["Destination"] = airports_[p[0]["Destination"]]["Name"]
      p[1]["Destination"] = p[0]["Destination"]

    return pairs

  def get_flight(self, flightA, flightB):
    return self._searchForFlight(flightA, flightB)





def main():
  meet = Meet()
  flightA = flight.Flight("uk", "gbp", "en-GB", "VIE", "everywhere",
      "2017-04-05", "2017-04-10")
  flightB = flight.Flight("uk", "gbp", "en-GB", "BTS", "everywhere",
      "2017-04-05", "2017-04-10")

  meet._get_flight(flightA, flightB)

if  __name__ =='__main__':
  main()
