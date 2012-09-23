import pygame
import resources
import os
import sys

from pytmx import pytmx
from pygame.locals import *
from tileset import Tileset
from player import Player

START_MENU = 0
GAME = 1
WIN_MENU = 2
LOSE_MENU = 3

def drawtext(text, font, screen):        
    rendered_text = font.render(text,True,(255,255,255))
    textRect = rendered_text.get_rect()
    textRect.right = screen.get_rect().right
    textRect.right = screen.get_rect().right
    screen.blit(rendered_text, textRect)
    
def start_menu():
    global state
    global levelTime
    key = pygame.key.get_pressed()
    if key[pygame.K_RETURN]:
        state = GAME
    screen.blit(start_bg, (0, 0))
    levelTime = 60.0

def game():
    global state
    global levelTime
    
    levelTime -= clock.get_time() / 1000.0
    if (levelTime <= 0.0):
        state = LOSE_MENU
        
    if len(goal_obstacles) == 0:
        state = WIN_MENU
    
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
    drawtext(str(int(levelTime)), font, screen)    
    
def win_menu():
    global state
    key = pygame.key.get_pressed()
    if key[pygame.K_RETURN]:
        state = START_MENU
    screen.blit(win_bg, (0, 0))

def lose_menu():
    global state
    key = pygame.key.get_pressed()
    if key[pygame.K_RETURN]:
        state = START_MENU
    screen.blit(lose_bg, (0, 0))
    
def collide_obstacle(obstacle):
    global levelTime
    key = pygame.key.get_pressed()
    if key[pygame.K_e]:
        if obstacle.get_obs_type() == "Goal":
            goal_obstacles.remove(obstacle)
            allsprites.remove(obstacle)
            return obstacle
    else:
        levelTime -= 2.0
    

if __name__ == "__main__":
    pygame.init()
        
    levels = []
    levels.append("../assets/maps/test.tmx")
    
    levelTime = 60.0
    state = START_MENU
    goal_obstacles = []
    screen = pygame.display.set_mode((1024, 768), HWSURFACE|DOUBLEBUF)
    tileset = Tileset("../assets/maps/test.tmx")
    walls = tileset.get_walls()
    obstacles = tileset.get_obstacles()
    player = Player((32, 32), 1, lambda o: collide_obstacle(o))
    player.set_walls(walls)
    player.set_obstacles(obstacles)
    clock = pygame.time.Clock()
    allsprites = pygame.sprite.RenderPlain(obstacles)
    allsprites.add(player)
    font = pygame.font.Font(None,17)

    for o in obstacles:
        if o.get_obs_type() == "Goal":
            goal_obstacles.append(o)
    
    start_bg, start_rect = resources.load_image("../assets/images/bg/start.bmp")
    win_bg, win_rect = resources.load_image("../assets/images/bg/win.bmp")
    lose_bg, lose_rect = resources.load_image("../assets/images/bg/lose.bmp")
    
    while 1:
        clock.tick(60)
        
        for e in pygame.event.get():
            if e.type == QUIT:
                sys.exit()
        
        {START_MENU: start_menu,
         GAME: game,
         WIN_MENU: win_menu,
         LOSE_MENU: lose_menu}[state]()
        
        pygame.display.flip()
        pygame.display.update()
    