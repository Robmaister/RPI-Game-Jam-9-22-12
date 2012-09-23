#! /usr/bin/env python
#
#Copyright (c) 2012 Robert Rouhani <robert.rouhani@gmail.com>, Nick Richard <richan2@rpi.edu>, Hayden Lee <leeh14@rpi.edu>
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in
#all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

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