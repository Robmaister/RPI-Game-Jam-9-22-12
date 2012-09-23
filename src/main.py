import pygame
import os

from pytmx import pytmx
from pygame.locals import *
from tileset import Tileset
from player import Player

def drawtext(font, text, screen, color=(255,255,255), bg=(0,0,0),):
    lines = text.splitlines()
    #first we need to find image size...
    width = height = 0
    for l in lines:
        width = max(width, font.size(l)[0])
        height += font.get_linesize()
    #create 8bit image for non-aa text..
    img = pygame.Surface((width, height), 0, 8)
    img.set_palette([bg, color])
    #render each line
    height = 0
    for l in lines:
        t = font.render(l, 0, color, bg)
        img.blit(t,( width -font.size(l)[0]), height)
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
        drawtext(None, 'hello',5)
        pygame.display.flip()
        pygame.display.update()
    

    
if __name__ == "__main__": main()