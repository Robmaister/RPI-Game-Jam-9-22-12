import pygame
import os
import operator

from pytmx import pytmx
from pygame.locals import *
from tileset import Tileset
from player import Player

def drawtext(font, text, screen, color=(255,255,255)):
    lines = text.splitlines()
    height = 0
    #render each line
    height = 0
    for l in lines:
        t = font.render(l, 0, color)
        screen.blit(t, (screen.get_width() - font.size(l)[0], height))
        height += font.get_linesize()
        
def main():
    pygame.init()
    screen = pygame.display.set_mode((1024, 768), HWSURFACE|DOUBLEBUF)
    tileset = Tileset("../assets/maps/test.tmx")
    walls = tileset.get_walls()
    player = Player((32, 32), 1)
    player.set_walls(walls)
    clock = pygame.time.Clock()
    allsprites = pygame.sprite.RenderPlain((player))
    levelTime = 60.0
    font = pygame.font.Font(None,36)

    while 1:
        clock.tick(60)
        levelTime -= clock.get_time() / 1000.0

        if (levelTime <= 0.0):
            return
        
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

        drawtext(font,str(int(levelTime)) + "\n Hello World!", screen)

        pygame.display.flip()
        pygame.display.update()
    

    
if __name__ == "__main__": main()