from os import environ
from meetInTheMiddle import app

p = int(environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=p)
