from geo import *
from apis import get_latlon
from input_output import *
import os
from timeFunctions import pauseTime
from planet import api

# folder locations
indir = "/home/jasondavis/planet_api/data"
outdir = "/media/jasondavis/old_harddrive/planet/output/tiftemp"
tempdir = "/home/jasondavis/planet_api/intermediate"
inaoi = "/home/jasondavis/planet_api/data/aoi.txt"
print "The working directory is " + os.getcwd()

# Define location which will become our aoi
#location = "san_francisco"


# Get coordinates from a string value location and output these coordinates as a tuple
#t = get_latlon("Tulare, CA")
#print t

aoi = {
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              -121.70654296874999,
              40.830436877649255
            ],
            [
              -121.70654296874999,
              41.672911819602085
            ],
            [
              -120.22338867187499,
              41.672911819602085
            ],
            [
              -120.22338867187499,
              40.830436877649255
            ],
            [
              -121.70654296874999,
              40.830436877649255
            ]
          ]
        ]
      }
    }
  ]
}
# Define api key
client = api.Client("5709a2a42720402e8c27104dbdecadb8")

#collect all scenes here
scenes = []

# get `count` number of scenes, for this example, use 1 to verify paging
# Define cloud filter (0.1 = less than 10% cloud cover)
filters = {'cloud_cover.estimated.lt': 0.2}

# Create planet object of all scenes with the given aoi
scene = client.get_scenes_list(scene_type= 'ortho', intersects=aoi, **filters)

# we'll use 50 `pages` of results
for s in scene.iter(pages=50):
	j = scenes.extend(s.get()['features'])

ids = [f['id'] for f in scenes]
print 'fetching tiffs for'
print '\n'.join(ids)

# receive callback and write downloaded file to output directory

callback = api.write_to_file(directory=outdir)
callbacks = client.fetch_scene_geotiffs(ids, callback=callback)

for index, cb in enumerate(callbacks):
	body = cb.await()
	print 'downloaded', body.name, 'size=%s bytes' % len(body), str(index+1)+'/'+str(len(callbacks))


