import requests

class Scanner:

  def __init__(self):
    pass

  def _request(self):
    url = "http://partners.api.skyscanner.net/apiservices/browsequotes/v1.0/{country}/{currency}/{locale}/EDI/LHR/anytime/anytime?apiKey=prtl6749387986743898559646983194"
    response = requests.get(url)
    print(response.json())


scanner = Scanner()
scanner._request()
