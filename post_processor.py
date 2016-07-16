#
# Rename, resize, and convert image to PNG
#

import os
from PIL import Image

image_dir = 'images/'
result_dir = 'final/'
size = 50, 50


# load name map
image_map = {}
with open(image_dir + 'image_map.txt') as map_file:
    for line in map_file:
        (img_name, sha1) = line.strip().split(',')
        image_map[sha1.strip()] = img_name.strip()


for dirpath, dirnames, filenames in os.walk('images/full'):
    for fname in filenames:
        if fname in image_map:
            img_name = image_map[fname]

        try:
            im = Image.open(dirpath + '/' + fname)  # open original
            # im.thumbnail(size, Image.ANTIALIAS)     # resize

            # save with new name and convert to png
            im.save(image_dir + result_dir + img_name)  # rename and convert

        except IOError as e:
            print e
            print "cannot create thumbnail for '%s'" % img_name