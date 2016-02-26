from PIL import Image, ImageChops
import os
outdir = "/media/jasondavis/old_harddrive/planet/output/jpegs"

image = '/media/jasondavis/old_harddrive/planet/output/jpegs/20150817_222926_0b09_visual.jpg'
def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)


im = Image.open(image)
im = trim(im)
im.show()
