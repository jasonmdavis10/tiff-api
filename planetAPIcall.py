# Copyright 2015 Planet Labs, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os.path
from planet import api
import os
import sys
import tempfile
from apis import get_latlon
from apis import get_scene_metadata
from input_output import read_txt

# folder locations
indir = "/home/jasondavis/planet_api/data"
outdir = "/home/jasondavis/planet_api/output"
tempdir = "/home/jasondavis/planet_api/intermediate"
print os.getcwd()

# in cities file location 
in_cities = '/home/jasondavis/planet_api/data/cities.txt'

# read the text file with cities 
cities = read_txt(in_cities)

# main loop over cities
'''
for city in cities:
	city = city.strip() #preventing whitespace
	print city
	aoi = get_latlon(city)
	print aoi
'''
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
              -118.51638793945312,
              35.63999910372582
            ],
            [
              -118.51638793945312,
              35.72979186282795
            ],
            [
              -118.35948944091795,
              35.72979186282795
            ],
            [
              -118.35948944091795,
              35.63999910372582
            ],
            [
              -118.51638793945312,
              35.63999910372582
            ]
          ]
        ]
      }
    }
  ]
}
# geojson AOI, WKT also supported

# will pick up api_key via environment variable PL_API_KEY
# but can be specified using `api_key` named argument
client = api.Client("5709a2a42720402e8c27104dbdecadb8")

#

#collect all scenes here
scenes = []

print 'loading scenes'

# get `count` number of scenes, for this example, use 1 to verify paging
filters = {'cloud_cover.estimated.lt': 0.1}
scene = client.get_scenes_list(scene_type= 'ortho', intersects=aoi, **filters)

# we'll use 3 `pages` of results
#for s in scene.iter(pages=1):
#	j = scenes.extend(s.get()['features'])

ids = [f['id'] for f in scenes]

print 'fetching tiffs for'
print '\n'.join(ids)
results = client.fetch_scene_thumbnails(ids, callback=api.write_to_file(outdir))

# results are async objects and we have to ensure they all process
#map(lambda r: r.await(), results)

#callback = api.write_to_file(directory='/home/jasondavis/planet_api/output') # change this
#callbacks = client.fetch_scene_geotiffs(ids, callback=callback)
#for cb in callbacks:
 #   body = cb.await()
 #   print 'downloaded', body.name, 'size=%s bytes' % len(body)
