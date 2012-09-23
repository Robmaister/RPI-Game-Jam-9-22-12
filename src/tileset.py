import pygame
import obstacle
from pytmx import tmxloader
from pygame import surface

class Tileset(object):
    def __init__(self, filename):
        self.tiles = tmxloader.load_pygame(filename, pixelalpha=True)
        
        tw = self.tiles.tilewidth
        th = self.tiles.tileheight
        gt = self.tiles.getTileImage
        
        self.surface = surface.Surface((self.tiles.width * tw, self.tiles.height * th))
        self.tile_width = tw
        self.tile_height = th
        #draw map
        for y in xrange(0, self.tiles.height):
            for x in xrange(0, self.tiles.width):
                tile = gt(x, y, 0)
                if tile: self.surface.blit(tile, (x*tw, y*th))
        
    def render(self, screen):
        screen.blit(self.surface, (0, 0))
        
    def get_walls(self):
        walls = []
        tw = self.tiles.tilewidth
        th = self.tiles.tileheight
        for y in xrange(0, self.tiles.height):
            for x in xrange(0, self.tiles.width):
                wall = self.tiles.getTileGID(x, y, 1)
                if (wall): walls.append(pygame.Rect(x * tw, y * th, tw, th))
        return walls
                
    def get_obstacles(self):
        obstacles = []
        for o in self.tiles.getObjects():
            obstacles.append(obstacle.Obstacle(o.x, o.y, o.name, o.type))
        return obstacles