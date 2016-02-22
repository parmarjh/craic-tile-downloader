# tile-downloader

Takes a latitude, longitude, and tile zoom level for a given tile server and outputs a tile URL.  

## Inputs

Lat and long must be in decimal degrees, and in that order (lat first).  If lat is not between -85 and 85 degrees, I don't know what will happen, but almost certainly nothing useful (if you live at one of the poles you're out of luck with this simple tool).  Zoom level must be a positive integer less than 20.  

## Usage:

    python lat_long_zoom_to_tile_URL.py {lat} {long} {zoom} {tileserver}

Example:

    python lat_long_zoom_to_tile_URL.py -2.694940 27.349241 13 OSM

That'll get you the URL of an OpenStreetMap (OSM) tile in a little town in the Congo (Shabunda, South Kivu, Democratic Republic of the Congo).

## What happens when you run it

The script takes the lat, long, and zoom level you've given it as arguments, and goes through as many as four steps:

1. It calculates a pixel coordinate of the point defined by the lat and long at the particular zoom level.
2. It calculates the integer tile coordinates (x, y) of the tile containing that point
3. Where necessary, it converts the tile coordinates into another representation such as a Quad Key
4. If the tile server in question is known to the script (and, where appropriate, an API key is present in the cfg folder), it generates an actual URL for the relevant tile.

The tile that gets selected is whatever one, at the given zoom level, contains the precise lat and long entered as arguments.  It doesn't matter where the actual point falls within the tile, you get the URL of the containing tile.  This will *not* be the same area, or necessarily the same upper left origin, for different zoom levels.

## Projection, datum, coordinate systems, etc.

This script is not going there.  Dead simple, bog-standard EPSG 4326, WGS 84.  If you don't know what those mean, suffice it to say that the coordinates you get from Google Earth, or from the GPS on your smartphone, provided they are in decimal degrees, will work.  If you're doing anything more complicated than that, it's time to start reading the Wikipedia article on map projections!

## Nota Bene: be a good citizen

A lot of tile servers have Terms of Service that do not allow direct URL access to tiles, and particularly do not allow the caching of such ("scraping").  Do, please, verify whether you have permission to download tiles from a given server. 

Perhaps even more critically, projects like OpenStreetMap give all their data away for free, but are non-profits and do not have the resources to run tileservers to serve massive requests; if you're going to create a lot of demand on an OSM tileserver, please download the OSM data and spin up your own tile server!  
