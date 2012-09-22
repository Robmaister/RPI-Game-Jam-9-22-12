import pygame, os
from pygame.locals import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480), HWSURFACE|DOUBLEBUF)
    
    stopevents = QUIT, KEYDOWN
    while 1:
        for e in pygame.event.get():
            if e.type in stopevents:
                return

if __name__ == "__main__": main()

#test