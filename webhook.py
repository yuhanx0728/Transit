from flask import Flask
from flask_assistant import Assistant, ask, tell
import requests
import logging
import os

logging.getLogger('flask_assistant').setLevel(logging.DEBUG)

app = Flask(__name__)
assist = Assistant(app, route='/', project_id='bustime-dc002')

@assist.action('check-bus')
def check_bus():
    url = 'http://truetime.portauthority.org/bustime/api/v3/getpredictions?key=8NAuMkVvD3kDkV6fJzFj4AhJG&rt=61D&stpid=10922&rtpidatafeed=Port Authority Bus&format=json'
    response = requests.get(url)
    raw_data = response.json()

    try:
        data = raw_data["bustime-response"]["prd"][0]
        speech = "Bus is coming in " + get_remaining_minutes(data) + " minutes at " + get_time(data)
    except:
        speech = "Probably no bus is coming right now. Check your phone app."

    return ask(speech)

def get_time(data):
    prdtm = data["prdtm"][9:]
    return (prdtm)

def get_remaining_minutes(data):
    prdtm = data["prdtm"][9:]
    prd_hour = prdtm[:2]
    prd_min = prdtm[3:]

    tmstmp = data["tmstmp"][9:]
    tm_hour = tmstmp[:2]
    tm_min = tmstmp[3:]

    if tm_hour == prd_hour:
	    return str(int(prd_min)-int(tm_min))
    else:
	    return str(int(prd_min)-int(tm_min)+60*(int(prd_hour)-int(tm_hour)))

# changed for heroku deployment
if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
'''
if __name__ == '__main__':
    app.run(debug=True)
'''