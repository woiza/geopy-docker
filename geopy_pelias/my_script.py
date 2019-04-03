from geopy.geocoders import Pelias
from geopy import distance
from pyroutelib2.loadOsm import LoadOsm
from pyroutelib2.route import Router


geolocator = Pelias(domain='pelias_api:4000',scheme='http',timeout=100)

location = geolocator.geocode("1901 Main St, Portland")
a = (location.latitude, location.longitude)

location = geolocator.geocode("1 NE Prescott St, Portland")
b = (location.latitude, location.longitude)

# By default, it uses the open API, this can be changed directly in the file `loadOsm.py`.
# Here, we use bicycle to calculate routes.
data = LoadOsm("cycle")
router = Router(data)

node_a = data.findNode(a[0], a[1])
node_b = data.findNode(b[0], b[1])

result, route = router.doRoute(node_a, node_b)
lats = []
lons = []
if result == 'success':
    for i in route:
        node = data.rnodes[i]
        lats.append(node[0])
        lons.append(node[1])
        print("%d: %f,%f" % (i, node[0], node[1]))
else:
    print("Error calculating the route.")

distance_route = 0

for i in range(len(lons)-1):
    p1=(lats[i],lons[i])
    p2=(lats[i+1],lons[i+1])
    distance_route += distance.geodesic(p1,p2, ellipsoid='GRS-80').km

print("Total distance on the route : %.2fkm" % distance_route)
