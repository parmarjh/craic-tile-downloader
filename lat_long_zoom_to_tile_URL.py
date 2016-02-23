import os, sys
import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

class Tile:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

def lat_long_zoom_to_pixel_coords(lat, lon, zoom):
    p = Point()
    sinLat = math.sin(lat * math.pi/180.0)
    x = ((lon + 180) / 360) * 256 * math.pow(2,zoom)
    y = (0.5 - math.log((1 + sinLat) / (1 - sinLat)) / 
          (4 * math.pi)) * 256 * math.pow(2,zoom)
    p.x = int(math.floor(x))
    p.y = int(math.floor(y))
    print "\nThe pixel coordinates are x = {} and y = {}".format(p.x, p.y)
    return p

def pixel_coords_to_tile_address(x,y):
    t = Tile()
    t.x = int(math.floor(x / 256))
    t.y = int(math.floor(y / 256))
    print"\nThe tile coordinates are x = {} and y = {}".format(t.x, t.y)
    return t

def tile_coords_and_zoom_to_quadKey(x, y, zoom):
    quadKey = ''
    for i in range(zoom, 0, -1):
        digit = 0
        mask = 1 << (i - 1)
        if(x & mask) != 0:
            digit += 1
        if(y & mask) != 0:
            digit += 2
        quadKey += str(digit)
    print "\nThe quadkey is {}".format(quadKey)
    return quadKey

def lat_long_zoom_to_quadKey(lat, lon, zoom):
    pixel = lat_long_zoom_to_pixel_coords(lat, lon, zoom)
    tile = pixel_coords_to_tile_address(pixel.x, pixel.y)
    quadKey = tile_coords_and_zoom_to_quadKey(tile.x, tile.y, zoom)
    return quadKey

def lat_long_zoom_to_URL(lat, lon, zoom):
    pixel = lat_long_zoom_to_pixel_coords(lat, lon, zoom)
    tile = pixel_coords_to_tile_address(pixel.x, pixel.y)
    quadKey = tile_coords_and_zoom_to_quadKey(tile.x, tile.y, zoom)
    try:
        api_key = ("Anz84uRE1RULeLwuJ0qKu5amcu5rugRXy1vKc27"
                   "wUaKVyIv1SVZrUjqaOfXJJoI0")
    except:
        print "Sumthin wrong with yer API key"

    tile_url = ("http://t0.tiles.virtualearth.net/tiles/a{}.jpeg?"
                "g=854&mkt=en-US&token={}".format(quadKey, api_key))
    print "\nThe tile URL is: {}".format(tile_url)
    return tile_url

if __name__ == "__main__":

    lat = float(sys.argv[1])
    lon = float(sys.argv[2])
    zoom = int(sys.argv[3])

    URL = lat_long_zoom_to_URL(lat, lon, zoom)



