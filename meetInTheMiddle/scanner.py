import requests
import json

class Scanner:

  def __init__(self):
    pass

  def _request(self, country, currency, locale, origin,
              dest, outtime, intime):
    apiKey = "prtl6749387986743898559646983194"
    url = "http://partners.api.skyscanner.net/apiservices/browsequotes/v1.0"
    url += ("/" + country + "/" + currency + "/" + locale + "/"
        + origin + "/" + dest + "/" + outtime + "/" +
           intime + "?apiKey=" +
           apiKey)
    response = requests.get(url)
    json_res = response.json()
    return json_res

  def _place_request(self, query):
    apiKey = "prtl6749387986743898559646983194"
    url = "http://partners.api.skyscanner.net/apiservices/autosuggest/v1.0"
    url += ("/uk/gbp/en-GB?query=" + query + "&apiKey=" + apiKey)
    response = requests.get(url)
    data = response.json()
    place = data["Places"][0]["CityId"]
    return place
