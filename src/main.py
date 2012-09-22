import pygame
import os

from pytmx import pytmx
from pygame.locals import *
from tileset import Tileset

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480), HWSURFACE|DOUBLEBUF)
    tileset = Tileset("../assets/maps/test.tmx")
    
    stopevents = QUIT, KEYDOWN
    while 1:
        for e in pygame.event.get():
            if e.type in stopevents:
                return
        tileset.render(screen)
        pygame.display.flip()

if __name__ == "__main__": main()