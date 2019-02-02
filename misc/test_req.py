import requests
APIKey = "8NAuMkVvD3kDkV6fJzFj4AhJG" # hidden
rt = "61C"
stpid = 1092
url = 'http://truetime.portauthority.org/bustime/api/v3/getpredictions?key='+APIKey+'&rt='+rt+'&stpid='+str(int(stpid))+'&rtpidatafeed=Port Authority Bus&format=json'
r = requests.get(url)
print(r.json())