import requests

def form_aoi():
	"""
	Create a geojson object that the lat-lon coordinates will be appended to to make a final aoi
	
	Args:
		spatial object type (str): (point, polygon, etc.)
	Returns:
		geojson object (without coordinates) that can be appended to.
	"""

## append the top function with the data returned from the bottom function. This will give the user a place to craft custom geojson objects that can be fed to the planet api function. 

def get_latlon(query):
	"""
	Get latitude and longitude from Google api for a place
	
	Args:
		query (str): place to geocode
	Returns:
		location in latlon
	"""
	result = requests.get("http://maps.googleapis.com/maps/api/geocode/json?address={}".format(query))
	location = result.json()['results'][0]['formatted_address']
	aoi = result.json()['results'][0]
	aoi1 = result.json()['results']
	#t = (aoi['lng'], aoi['lat'])
	return aoi==aoi1

	


def get_height_ahn2(wkt_geom):
	"""
	Get AHN2 height for wkt geometry

	Args:
		wkt_geom: geometry as WKT

	Returns:
		height in mNAP
	"""
	result = requests.get("https://nxt.staging.lizard.net/api/v2/raster-aggregates/?page_size=0&agg=curve&geom={}&raster_names=dem%2Fnl&srs=EPSG:4326&start=2015-01-14T21:01:01&stop=2015-01-21T21:01:01&window=3600000".format(wkt_geom), verify=False)
    	height = result.json()['data'][0]



def get_scene_metadata(self, scene_id, scene_type='ortho'):
        """
        Get metadata for a given scene.

        :pa)ram str scene_id: The scene ID
        :param str scene_type: The type: either 'ortho' or 'landsat'
        :return: :py:class:`JSON` body
        """
        # todo: accept/return multiple scenes
        return self._get('scenes/%s/%s' % (scene_type, scene_id)).get_body()

def get_scenes_list(self, scene_type='ortho', order_by=None, count=None,
                        intersects=None, workspace=None, **filters):
        '''Get scenes matching the specified parameters and filters.

        :param str scene_type: The type of scene, defaults to 'ortho'
        :param str order_by: Results order 'acquired asc' or 'acquired desc'.
           Defaults to 'acquired desc'
        :param int count: Number of results per page. Defaults to 50.
        :param intersects: A geometry to filter results by. Can be one of:
           WKT or GeoJSON text or a GeoJSON-like dict.
        :param filters: Zero or more metadata filters in the form of
           param.name.comparison -> value.
        :returns: :py:class:`Scenes` body
        '''
        params = {
            'order_by': order_by,
            'count': count,
            'intersects': intersects
        }
        if workspace:
            params['workspace'] = workspace
        params.update(**filters)
        return self._get('scenes/%s/' % scene_type,
                         models.Scenes, params=params).get_body()










