import scanner
from itertools import product
import flight
import time

class Meet:

  def __init__(self):
    pass

  def _chooseBest(self, flightsA, flightsB):
    return 0

  def _clean(self, jobj, airports):
    res = {}
    res["MinPrice"] = jobj["MinPrice"]
    res["DestinationId"] = jobj["OutboundLeg"]["DestinationId"]
    res["DestinationCityId"] = airports[res["DestinationId"]]["CityId"]
    res["DestinationName"] = airports[res["DestinationId"]]["Name"]
    res["DestinationCode"] = airports[res["DestinationId"]]["IataCode"]
    res["OutTime"] = jobj["OutboundLeg"]["DepartureDate"][0:10]
    res["InTime"] = jobj["InboundLeg"]["DepartureDate"][0:10]

    return res

  def _searchForFlight(self, flightA, flightB):
    sky = scanner.Scanner()
    responseDano = sky._request(flightA.country, flightA.currency,
                              flightA.locale, flightA.origin, flightA.dest,
                              flightA.outtime, flightA.intime)
    responseBrch = sky._request(flightB.country, flightB.currency,
                              flightB.locale, flightB.origin, flightB.dest,
                              flightB.outtime, flightB.intime)

    #print(responseDano)

    airportsDano = filter((lambda x: x["Type"] == "Station"), responseDano["Places"])
    airportsBrch = filter((lambda x: x["Type"] == "Station"), responseBrch["Places"])

    airports = airportsBrch + airportsDano
    airports_ = {}
    for x in airports:
      airports_[x["PlaceId"]] = {"IataCode" : x["IataCode"],
                                 "Name" : x["Name"],
                                 "CityId" : x["CityId"]}
    #print(airports_)

    flightsDano = [self._clean(x, airports_) for x in responseDano["Quotes"]]#map(self._clean, responseDano["Quotes"])
    flightsBrch = [self._clean(x, airports_) for x in responseBrch["Quotes"]]#map(self._clean, responseBrch["Quotes"])

    pairs = list(product(flightsBrch, flightsDano))
    for crit in ["DestinationCityId", "InTime","OutTime"]:
      pairs = filter((lambda x: x[0][crit] == x[1][crit]), pairs)

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
