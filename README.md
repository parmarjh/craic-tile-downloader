# tile-downloader

Takes a tile zoom level, latitude, and longitude for a given tile server and outputs a tile URL.

Usage:

    python lat_long_zoom_to_tile_URL.py {zoom} {lat} {long} {tileserver}

Example:

    python lat_long_zoom_to_tile_URL.py 13 -2.694940 27.349241 OSM

That'll get you the URL of an OpenStreetMap tile in a little town in the Congo (Shabunda, South Kivu, Democratic Republic of the Congo).

_Nota Bene_: A lot of tile servers have Terms of Service that do not allow direct URL access to tiles, and particularly do not allow the caching of such ("scraping").  Do, please, verify whether you have permission to download tiles from a given server. 

Perhaps even more critically, projects like OpenStreetMap give all their data away for free, but are non-profits and do not have the resources to run tileservers to serve massive requests; if you're going to create a lot of demand on an OSM tileserver, please download the OSM data and spin up your own tile server!  
