import googlemaps
gmaps = googlemaps.Client(key = 'AIzaSyCK16wTwgKVNO6cYhURe59ruqrmrWa68aA')

address = '4913 portmarnoch ct, California, San Jose'
coor = gmaps.geocode(address)
lat = coor[0]["geometry"]["location"]['lat']
lng = coor[0]["geometry"]["location"]['lng'] 