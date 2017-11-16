# test_functions.py

# test each of the functions in the library

import lat_long_zoom_to_tile_URL as tiledownloader
from lat_long_zoom_to_tile_URL import Tile
from lat_long_zoom_to_tile_URL import Point


#import math

def main():
  print("test latlong to tile_id")

  # arbitrary test values
  lat = 9.05734599
  lon = 6.62475585
  zoom = 18

  pixel   = tiledownloader.lat_long_zoom_to_pixel_coords(lat, lon, zoom)
  tile    = tiledownloader.pixel_coords_to_tile_address(pixel.x, pixel.y)
  quadKey = tiledownloader.tile_coords_and_zoom_to_quadKey(tile.x, tile.y, zoom)

  print("lat {}  lon {}".format(lat, lon))
  print("pixel  x: {}  y: {}".format(pixel.x, pixel.y))
  print("tile   x: {}  y: {}".format(tile.x,  tile.y))
  print("quadkey: {}".format(quadKey))


  print("\ntest tile_id to latlong")
  tile = Tile()
  tile.x = 135896
  tile.y = 124449
  print("tile   x: {}  y: {}".format(tile.x,  tile.y))
  pixel = tiledownloader.tile_address_to_pixel_coords(tile)
  print("pixel  x: {}  y: {}".format(pixel.x, pixel.y))
  lat, lon = tiledownloader.pixel_coords_to_lat_long(pixel, zoom)
  print("lat {}  lon {}".format(lat, lon))

  print("\nNote that the two sets of lat long may not be the same!")

main()

