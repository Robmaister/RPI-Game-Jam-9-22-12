import pygame
import os

from pytmx import pytmx
from pygame.locals import *
from tileset import Tileset
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((480, 480), HWSURFACE|DOUBLEBUF)
    tileset = Tileset("../assets/maps/test.tmx")
    player = Player((0, 0), 1)
    clock = pygame.time.Clock()
    allsprites = pygame.sprite.RenderPlain((player))

    while 1:
        clock.tick(60)
        for e in pygame.event.get():
            if e.type == QUIT:
                return
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            player.move_forward()
        if key[pygame.K_s]:
            player.move_backwards()
        if key[pygame.K_a]:
            player.move_left()
        if key[pygame.K_d]:
            player.move_right()
        
        allsprites.update()
        tileset.render(screen)
        allsprites.draw(screen)
        pygame.display.flip()

    
if __name__ == "__main__": main()