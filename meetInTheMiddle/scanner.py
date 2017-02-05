import requests
from random import randint

class Scanner:

  robin = 0
  apiKeys = ["im235201764412234487664519535179",
             "prtl6749387986743898559646983194",
             "im368752173193336741801399219284",
             "me665017323012124034343892326870"]

  def __init__(self):
    self.robin = randint(0, len(self.apiKeys) - 1)

  def _getKey(self):
    return self.apiKeys[(self.robin - 1) % len(self.apiKeys)]

  def _request(self, country, currency, locale, origin,
              dest, outtime, intime):
    apiKey = self._getKey()
    url = "http://partners.api.skyscanner.net/apiservices/browsequotes/v1.0"
    url += ("/" + country + "/" + currency + "/" + locale + "/"
        + origin + "/" + dest + "/" + outtime + "/" +
           intime + "?apiKey=" +
           apiKey)
    print(url)
    try:
      response = requests.get(url)
      response.raise_for_status()
      json_res = response.json()
      print("Quotes: ", len(json_res["Quotes"]))
      return json_res
    except requests.exceptions.HTTPError as err:
      print(err.errno)
      self.robin += 1
      return self._request(country, currency, locale, origin,
                           dest, outtime, intime)


  def _place_request(self, query):
    apiKey = self._getKey()
    url = "http://partners.api.skyscanner.net/apiservices/autosuggest/v1.0"
    url += ("/uk/gbp/en-GB?query=" + query + "&apiKey=" + apiKey)
    print(url)
    try:
      response = requests.get(url)
      response.raise_for_status()
      data = response.json()
      place = data["Places"][0]["CityId"]
      return place
    except requests.exceptions.HTTPError as err:
      print(err.errno)
      self.robin += 1
      return self._place_request(query)
