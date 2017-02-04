import scanner
import flight

class Meet:

  def __init__(self):
    pass

  def _chooseBest(self, flightsA, flightsB):
    return 0

  def _clean(self, jobj):
    res = {}
    res["MinPrice"] = jobj["MinPrice"]
    res["Destination"] = jobj["OutboundLeg"]["DestinationId"]

    return res

  def _get_flight(self, flightA, flightB):
    sky = scanner.Scanner()
    flightsDano = sky._request(flightA.country, flightA.currency,
                              flightA.locale, flightA.origin, flightA.dest,
                              flightA.outtime, flightA.intime)["Quotes"]
    flightsBrch = sky._request(flightB.country, flightB.currency,
                              flightB.locale, flightB.origin, flightB.dest,
                              flightB.outtime, flightB.intime)["Quotes"]
    cleanDano = map(self._clean, flightsDano)
    cleanBrch = map(self._clean, flightsBrch)

    common = filter(lambda x: x["Destination"] in
        map((lambda x: x["Destination"]), cleanBrch), cleanDano)

    print(common)
    return common

    #bestFlights = _chooseBest(flightsDano, flightsBrch)

def main():
  meet = Meet()
  flightA = flight.Flight("uk", "gbp", "en-GB", "KSC", "everywhere", "anytime", "anytime")
  flightB = flight.Flight("uk", "gbp", "en-GB", "BTS", "everywhere", "anytime", "anytime")

  meet._get_flight(flightA, flightB)

if  __name__ =='__main__':
  main()
