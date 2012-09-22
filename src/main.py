import pygame
import os

from pytmx import pytmx
from pygame.locals import *
from tileset import Tileset

def main():
    pygame.init()
    screen = pygame.display.set_mode((480, 480), HWSURFACE|DOUBLEBUF)
    tileset = Tileset("../assets/maps/test.tmx")

    while 1:
        for e in pygame.event.get():
            if e.type == QUIT:
                return
            elif e.type == KEYDOWN:
                print "key pressed", e
        tileset.render(screen)
        pygame.display.flip()

if __name__ == "__main__": main()