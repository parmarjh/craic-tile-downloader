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

def lat_long_to_pixel_coords(zoom, long, lat):
    p = Point()
    sinLat = math.sin(lat * math.pi/180.0)
    p.x = ((long + 180) / 360) * 256 * math.pow(2,zoom)
    p.y = (0.5 - math.log((1 + sinLat) / (1 - sinLat)) / 
          (4 * math.pi)) * 256 * math.pow(2,zoom)
    return p

def pixel_coords_to_tile_address(x,y):
    t = Tile()
    t.x = int(math.floor(x / 256))
    t.y = int(math.floor(y / 256))
    return t

def tile_coords_to_quadKey(zoom, x, y):
    quadKey = ''
    for i in range(zoom, 0, -1):
        digit = 0
        mask = 1 << (i - 1)
        if(x & mask) != 0:
            digit += 1
        if(y & mask) != 0:
            digit += 2
        quadKey += str(digit)
    return quadKey

if __name__ == "__main__":
    zoom = int(sys.argv[1])
    latitude = float(sys.argv[2])
    longitude = float(sys.argv[3])

    pixel = lat_long_to_pixel_coords(zoom, longitude, latitude)
    tile = pixel_coords_to_tile_address(pixel.x, pixel.y)
    quadKey = tile_coords_to_quadKey(zoom, tile.x, tile.y)

    print tile.x
    print tile.y
    print quadKey

