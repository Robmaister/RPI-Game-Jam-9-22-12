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

def drawtext(font, text, screen, color=(255,255,255)):
    lines = text.splitlines()
    height = 0
    #render each line
    height = 0
    for l in lines:
        t = font.render(l, 0, color)
        screen.blit(t, (screen.get_width() - font.size(l)[0], height))
        height += font.get_linesize()
    
def start_menu():
    global levelTime
    screen.blit(start_bg, (0, 0))
    
def start_menu_key(event):
    global state
    if event.key == pygame.K_RETURN:
        state = GAME
        init()

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
    drawtext(font, str(int(levelTime)), screen)    

def game_key(event):
    pass
    
def win_menu():
    screen.blit(win_bg, (0, 0))
    
def win_menu_key(event):
    global state
    if event.key == pygame.K_RETURN:
        state = START_MENU

def lose_menu():
    screen.blit(lose_bg, (0, 0))
    
def lose_menu_key(event):
    global state
    if event.key == pygame.K_RETURN:
        state = START_MENU
    
def collide_obstacle(obstacle):
    global levelTime, goal_obstacles
    key = pygame.key.get_pressed()
    if key[pygame.K_e]:
        if obstacle.get_obs_type() == "Goal":
            goal_obstacles.remove(obstacle)
            allsprites.remove(obstacle)
            return obstacle
    elif obstacle.get_obs_type() == "Obstacle":
        levelTime -= 2.0
    
def init():
    global goal_obstacles, allsprites, tileset, walls, obstacles, player, levelTime
    walls = tileset.get_walls()
    obstacles = tileset.get_obstacles()
    player.set_walls(walls)
    player.set_obstacles(obstacles)
    player.move_to(32, 32)
    goal_obstacles = []
    for o in obstacles:
        if o.get_obs_type() == "Goal":
            goal_obstacles.append(o)
    allsprites = pygame.sprite.RenderPlain(obstacles)
    allsprites.add(player)
    levelTime = 60.0
    tileset = Tileset("../assets/maps/test.tmx")

if __name__ == "__main__":
    pygame.init()
        
    levels = []
    levels.append("../assets/maps/test.tmx")
    
    levelTime = 60.0
    state = START_MENU
    goal_obstacles = []
    screen = pygame.display.set_mode((1024, 768), HWSURFACE|DOUBLEBUF)
    tileset = Tileset("../assets/maps/test.tmx")
    walls = []
    obstacles = []
    player = Player((32, 32), 1, lambda o: collide_obstacle(o))
    clock = pygame.time.Clock()

    allsprites = pygame.sprite.RenderPlain(obstacles)
    allsprites.add(player)
    font = pygame.font.Font(None,36)
    
    init()

    start_bg, start_rect = resources.load_image("../assets/images/bg/start.bmp")
    win_bg, win_rect = resources.load_image("../assets/images/bg/win.bmp")
    lose_bg, lose_rect = resources.load_image("../assets/images/bg/lose.bmp")
    
    while 1:
        clock.tick(60)
        
        for e in pygame.event.get():
            if e.type == QUIT:
                sys.exit()
            elif e.type == KEYDOWN:
                {START_MENU: start_menu_key,
                 GAME: game_key,
                 WIN_MENU: win_menu_key,
                 LOSE_MENU: lose_menu_key}[state](e)
        
        {START_MENU: start_menu,
         GAME: game,
         WIN_MENU: win_menu,
         LOSE_MENU: lose_menu}[state]()
        
        pygame.display.flip()
        pygame.display.update()
    
