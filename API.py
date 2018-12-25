import requests
#url = 'http://truetime.portauthority.org/bustime/api/v3/getrtpidatafeeds?key=8NAuMkVvD3kDkV6fJzFj4AhJG'
url = 'http://truetime.portauthority.org/bustime/api/v3/getpredictions?key=8NAuMkVvD3kDkV6fJzFj4AhJG&rt=61D&stpid=10922&rtpidatafeed=Port Authority Bus&format=json'
response = requests.get(url)
data = response.json()
prdtm = data["bustime-response"]["prd"][0]["prdtm"][9:]
prd_hour = prdtm[:2]
prd_min = prdtm[3:]
tmstmp = data["bustime-response"]["prd"][0]["tmstmp"][9:]
tm_hour = tmstmp[:2]
tm_min = tmstmp[3:]

if tm_hour == prd_hour:
	print(str(int(prd_min)-int(tm_min)))
else:
	print(str(int(prd_min)-int(tm_min)+60*(int(prd_hour)-int(tm_hour))))