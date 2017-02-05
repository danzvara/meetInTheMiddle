import requests

class Scanner:

  robin = 0
  apiKeys = ["im235201764412234487664519535179",
             "prtl6749387986743898559646983194",
             "im368752173193336741801399219284",
             "me665017323012124034343892326870"]

  def __init__(self):
    pass

  def _getKey(self):
    self.robin += 1
    return self.apiKeys[(self.robin - 1) % len(self.apiKeys)]

  def _request(self, country, currency, locale, origin,
              dest, outtime, intime):
    apiKey = self._getKey()
    url = "http://partners.api.skyscanner.net/apiservices/browsequotes/v1.0"
    url += ("/" + country + "/" + currency + "/" + locale + "/"
        + origin + "/" + dest + "/" + outtime + "/" +
           intime + "?apiKey=" +
           apiKey)
    response = requests.get(url)
    json_res = response.json()
    return json_res

  def _place_request(self, query):
    apiKey = self._getKey()
    url = "http://partners.api.skyscanner.net/apiservices/autosuggest/v1.0"
    url += ("/uk/gbp/en-GB?query=" + query + "&apiKey=" + apiKey)
    response = requests.get(url)
    data = response.json()
    place = data["Places"][0]["CityId"]
    return place
