from pytmx import tmxloader
from pygame import surface

class Tileset(object):
    def __init__(self, filename):
        self.tiles = tmxloader.load_pygame(filename, pixelalpha=True)
        
        tw = self.tiles.tilewidth
        th = self.tiles.tileheight
        gt = self.tiles.getTileImage
        
        self.surface = surface.Surface((self.tiles.width * tw, self.tiles.height * th))
        
        #draw map
        for l in xrange(0, len(self.tiles.tilelayers)):
            for y in xrange(0, self.tiles.height):
                for x in xrange(0, self.tiles.width):
                    tile = gt(x, y, l)
                    if tile: self.surface.blit(tile, (x*tw, y*th))
        
    def render(self, screen):
        screen.blit(self.surface, (0, 0))