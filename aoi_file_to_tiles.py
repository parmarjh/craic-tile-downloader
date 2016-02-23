import os, sys
import math
import urllib
from lat_long_zoom_to_tile_URL import *

def lat_long_to_pixel_coordinates(infile, zoom_level, long, lat):

    try:
        from osgeo import ogr, osr
        print 'import of ogr and osr worked. \n'
    except:
        print 'Import of ogr and osr failed. \n'
        sys.exit()

    try: 
        infile_extension = infile.split(".")[-1]
    except: 
        print 'yeah, your input file is not that great. \n'

    try:
	if infile_extension == 'shp':
		driver = ogr.GetDriverByName('ESRI Shapefile')
	elif infile_extension == 'geojson':
		driver = ogr.GetDriverByName('GeoJSON')
	elif infile_extension == 'kml':
		driver = ogr.GetDriverByName('KML')
	else:
		print 'Check input file format for '+infile
		print 'Supported formats .shp .geojson .kml'
		sys.exit()
	# open the data source
	datasource = driver.Open(infile, 0)
    except:
        print 'failed to load the osgeo driver for ' + infile_extension
        try:
            # Get the data layer
            layer = datasource.GetLayer()
        except:
            print 'I am an indented block'

if __name__ == "__main__":

    lat = float(sys.argv[1])
    lon = float(sys.argv[2])
    zoom = int(sys.argv[3])

    quadKey = lat_long_zoom_to_quadKey(lat,lon,zoom)
    tile_url = lat_long_zoom_to_URL(lat, lon, zoom)
    filename = "images/a{}.jpeg".format(quadKey)

    if not os.path.exists("images"):
        os.makedirs("images")

    urllib.urlretrieve(tile_url, filename)
    
