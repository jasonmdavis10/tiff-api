import geojson
from geojson import Point

def build_geojson(tuple):
	'''
	Builds a geojson object from a set of lat lon coordinates
	Args:
		lat (float): coordinates lattitude
		lon (float): coorinates longitude
	Returns:
		a geojson object that can be fed to the planet functions
	'''
	jsonObj = Point(tuple)
	return jsonObj

def dump_json(aoi):
	'''
	Takes a geojson object and returns it, properly formatted as json
	Args:
		coornidates (geojson)
	Returns:
		a geojson object that can be fed to planet functions
	'''
	dump = geojson.dumps(aoi)
	return dump




'''
from geojson import Polygon

# polygon
Polygon([[(2.38, 57.322), (23.194, -20.28), (-120.43, 19.15), (2.38, 57.322)]])
{"coordinates": [[[(2.38, 57.322), (23.194, -20.28), (-120.43, 19.15), (2.38, 57.322)]]], "type": "Polygon"}

'''
	

#Next step is to take a geojson object and reformat it into an object that can be used by planet labs function.
#Basically need to parse and reformat the json.
