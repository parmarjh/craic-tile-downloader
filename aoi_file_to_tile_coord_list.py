import os, sys
import math

def lat_long_to_pixel_coordinates(infile, zoom_level, long, lat):

    try:
        from osgeo import ogr, osr
        print 'import of ogr and osr worked. \n'
    except:
        print 'Import of ogr and osr failed. \n'
        sys.exit()

    try: 
        infile_extension = infile.split(.)[-1]
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
