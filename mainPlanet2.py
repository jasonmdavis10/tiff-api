from geo import *
from apis import get_latlon
from input_output import *
import os
from timeFunctions import pauseTime
from planet import api

# folder locations
indir = "/home/jasondavis/planet_api/data"
outdir = "/home/jasondavis/planet_api/output"
tempdir = "/home/jasondavis/planet_api/intermediate"
inaoi = "/home/jasondavis/planet_api/data/aoi.txt"
print "The working directory is " + os.getcwd()

# Define location which will become our aoi
#location = "san_francisco"


filters = {
    # Your filters here, for example:
    # Cloud cover less than 1%
    "cloud_cover.estimated.lte": 1,
}

url = "https://api.planet.com/v0/scenes/ortho/"

key = "YOUR-KEY-HERE"

r = requests.get(url, params=filters, auth=(key, ''))
r.raise_for_status()
data = r.json()
scenes_data = data["features"]
for scene in scenes_data:
    thumb_link = scene["properties"]["links"]["thumbnail"]
    download_image(thumb_link, key)


