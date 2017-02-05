from meetInTheMiddle import scanner, flight
from itertools import product


class Meet:
  def __init__(self):
    self.sky = scanner.Scanner()

  def _chooseBest(self, flightsA, flightsB):
    return sorted(self._searchForFlight(flightsA, flightsB, True),
                  key=lambda x: x[0]["Price"] + x[1]["Price"])

  def _clean(self, jobj, airports, carriers):
    res = {}
    res["Price"] = jobj["MinPrice"]
    res["OriginCode"] = airports[jobj["OutboundLeg"]["OriginId"]]["IataCode"]
    res["DestinationId"] = jobj["OutboundLeg"]["DestinationId"]
    res["DestinationCityId"] = airports[res["DestinationId"]]["CityId"]
    res["DestinationName"] = airport]s[res["DestinationId"]["Name"]
    res["DestinationCode"] = airports[res["DestinationId"]]["IataCode"]
    res["OutTime"] = jobj["OutboundLeg"]["DepartureDate"][0:10]
    res["InTime"] = jobj["InboundLeg"]["DepartureDate"][0:10]
    if (len(jobj["OutboundLeg"]["CarrierIds"]) > 0
        and len(jobj["InboundLeg"]["CarrierIds"]) > 0):
      res["OutCarrierId"] = jobj["OutboundLeg"]["CarrierIds"][0]
      res["InCarrierId"] = jobj["InboundLeg"]["CarrierIds"][0]
      res["OutCarrier"] = carriers[res["OutCarrierId"]]
      res["InCarrier"] = carriers[res["InCarrierId"]]

    return res

  def _searchForFlight(self, flightA, flightB, selected):
    sky = scanner.Scanner()

    countries = ["FR-sky", "DE-sky", "NL-sky", "IT-sky", "SK-sky", "PL-sky"]

    if (flightA.origin == "Prague, Czechia"):
      flightA.origin = "Prague"
    if (flightB.origin == "Prague, Czechia"):
      flightB.origin = "Prague"
    flightA.origin = self.sky._place_request(flightA.origin)
    flightB.origin = self.sky._place_request(flightB.origin)

    responseDano = sky._request(flightA.country, flightA.currency,
                                flightA.locale, flightA.origin, flightA.dest,
                                flightA.outtime, flightA.intime)
    responseBrch = sky._request(flightB.country, flightB.currency,
                                flightB.locale, flightB.origin, flightB.dest,
                                flightB.outtime, flightB.intime)

    airportsDano = filter((lambda x: x["Type"] == "Station"), responseDano["Places"])
    airportsBrch = filter((lambda x: x["Type"] == "Station"), responseBrch["Places"])

    carriersDano = responseDano["Carriers"]
    carriersBrch = responseBrch["Carriers"]
    carriers = {}
    for c in carriersDano:
      carriers[c["CarrierId"]] = c["Name"]
    for c in carriersBrch:
      carriers[c["CarrierId"]] = c["Name"]

    airports = list(airportsBrch) + list(airportsDano)
    airports_ = {}
    for x in airports:
      airports_[x["PlaceId"]] = {"IataCode" : x["IataCode"],
                                 "Name" : x["Name"],
                                 "CityId" : x["CityId"]}

    flightsDano = [self._clean(x, airports_, carriers) for x in responseDano["Quotes"]]
    flightsBrch = [self._clean(x, airports_, carriers) for x in responseBrch["Quotes"]]

    pairs = list(product(flightsBrch, flightsDano))
    for crit in ["DestinationCityId", "InTime", "OutTime"]:
      pairs = filter((lambda x: x[0][crit] == x[1][crit]), pairs)

    return pairs

  def get_flight(self, flightA, flightB):
    return self._chooseBest(flightA, flightB)

