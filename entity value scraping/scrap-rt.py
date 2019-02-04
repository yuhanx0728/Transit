import csv

with open('scrap-result.csv', mode='w') as result:
    result_writer = csv.writer(result, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    with open('bus-route.csv', mode='r') as route:
    	route_reader = csv.reader(route, delimiter=',')
    	for rows in route_reader:
		    result_writer.writerow([rows[2], rows[2]])