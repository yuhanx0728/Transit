import requests
apiKey = "" # hidden
url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=Murray%20Avenue%20at%20Hobart%20Street&inputtype=textquery&key="+apiKey
r = requests.get(url)
placeID = (r.json()['candidates'][0]['place_id'])
url = "https://maps.googleapis.com/maps/api/place/details/json?placeid="+placeID+"&key="+apiKey
r = requests.get(url)
print(r.json())