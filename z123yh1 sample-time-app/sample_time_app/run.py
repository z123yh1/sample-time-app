from flask import Flask
from datetime import datetime
date=datetime.now()
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/time')
def getTime():
    return date.strftime("%d/%m/%y")
app.run(host='0.0.0.0',
        port=8080,
        debug=True)
