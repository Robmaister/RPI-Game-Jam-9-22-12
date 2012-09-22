'''
Created on Sep 22, 2012

@author: Robert Rouhani
'''

class Tileset(object):
    def __init__(self, filename):
        from pytmx import tmxloader
        self.tiles = tmxloader.load_pygame(filename, pixelalpha=True)
        
    def render(self, surface):
        tw = self.tiles.tilewidth
        th = self.tiles.tileheight
        gt = self.tiles.getTileImage

        for l in xrange(0, len(self.tiles.tilelayers)):
            for y in xrange(0, self.tiles.height):
                for x in xrange(0, self.tiles.width):
                    tile = gt(x, y, l)
                    if tile: surface.blit(tile, (x*tw, y*th))