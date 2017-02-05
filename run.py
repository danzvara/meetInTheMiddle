from os import environ
from meetInTheMiddle import app

app.run(port=environ.get('PORT'), debug=True)
