import os, sys
from math import ceil
import math
import urllib
from lat_long_zoom_to_tile_URL import *

def aoi_and_zoom_to_lat_long_points(infile, zoom):

    try:
        from osgeo import ogr, osr
        print 'import of ogr and osr worked. \n'
    except:
        print 'Import of ogr and osr failed. Please install them. \n'
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
        print 'Something is wrong with the data layer.'
        sys.exit()

    # Get layer definition
    layer_defn = layer.GetLayerDefn()

    # Get layer extent
    extent = layer.GetExtent()
    xmin = extent[0]
    xmax = extent[1]
    ymin = extent[2]
    ymax = extent[3]

    # average latitude of the area of interest
    y_average = ymin+((ymax-ymin)/2)
    # TODO might be better to implement this per row rather than per AOI;
    # if the AOI is big enough the conversion of long value to x coords
    # might get sufficiently out of whack to bring up the wrong tile (not
    # sure how much it varies from, say, top to bottom of South Kivu
	
    #get feature geometry
    input_feature= layer.GetFeature(0)
    in_geometry= input_feature.GetGeometryRef()

    # get Zoomlevel
    zoomlevel = float(zoom)
	
    # Calculate GridWidth and GridHeight from given inputs
	
    ground_resolution_x = (360)/(256*math.pow(2,zoomlevel))
    ground_resolution_y = (
            (math.cos(y_average*math.pi/180)*360)/(256*math.pow(2,zoomlevel)))
    gridWidth = float(256)*ground_resolution_x
    gridHeight = float(256)*ground_resolution_y
	
    # get rows
    rows = ceil((ymax-ymin)/gridHeight)
    # get columns
    cols = ceil((xmax-xmin)/gridWidth)

    # start grid cell envelope
    ringXleftOrigin = xmin
    ringXrightOrigin = xmin + gridWidth
    ringYtopOrigin = ymax
    ringYbottomOrigin = ymax-gridHeight



def lat_long_zoom_to_tile_download(lat, lon, zoom):
    
    quadKey = lat_long_zoom_to_quadKey(lat,lon,zoom)
    tile_url = lat_long_zoom_to_URL(lat, lon, zoom)
    filename = "images/a{}.jpeg".format(quadKey)

    if not os.path.exists("images"):
        os.makedirs("images")

    urllib.urlretrieve(tile_url, filename)

if __name__ == "__main__":
    
#
# example run : $ python grid.py polygon.shp 18 480 640
#

    if len( sys.argv ) != 3: 
        print ("[ ERROR ] you must supply two arguments: "
               "input-shapefile-name.shp zoomlevel")
        sys.exit( 1 )

    ( sys.argv[1], sys.argv[2])
