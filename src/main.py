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
DESC_MENU = 4

def draw_text_right(font, text, screen, color=(255,255,255)):
    lines = text.splitlines()
    height = 0
    #render each line
    for l in lines:
        t = font.render(l, 0, color)
        screen.blit(t, (screen.get_width() - font.size(l)[0], height))
        height += font.get_linesize()

def draw_text_center(font, text, screen, height, color=(255, 255, 255)):
    lines = text.splitlines()
    #render each line
    for l in lines:
        t = font.render(l, 0, color)
        screen.blit(t, (screen.get_width() / 2 - font.size(l)[0] / 2, height))
        height += font.get_linesize()
    
def start_menu():
    global levelTime
    screen.blit(start_bg, (0, 0))
    
def start_menu_key(event):
    global state
    if event.key == pygame.K_RETURN:
        state = DESC_MENU

def desc_menu():
    screen.blit(desc_bg, (0, 0))
    draw_text_center(font, levels_text[cur_level] + "\n\n\n\n\n\nPress Enter to continue", screen, 50, (0, 0, 0))

def desc_menu_key(event):
    global state
    if event.key == pygame.K_RETURN:
        state = GAME
        init()

def game():
    global state
    global levelTime
    global cur_level
    
    levelTime -= clock.get_time() / 1000.0
    if (levelTime <= 0.0):
        state = LOSE_MENU
        
    if len(goal_obstacles) == 0:
        state = DESC_MENU
        cur_level += 1
    
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
    
    need_text = "You need to collect:     "
    for o in goal_obstacles:
        need_text += "\n" + o.get_name() + "     "
    
    draw_text_right(font, "\nTime left: " + str(int(levelTime)) + "     \n" + need_text, screen, (255, 0, 0))

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
    tileset = Tileset(levels[cur_level])
    walls = tileset.get_walls()
    obstacles = tileset.get_obstacles()
    player.set_walls(walls)
    player.set_obstacles(obstacles)
    player.move_to(48, 76)
    goal_obstacles = []
    for o in obstacles:
        if o.get_obs_type() == "Goal":
            goal_obstacles.append(o)
    allsprites = pygame.sprite.RenderPlain(obstacles)
    allsprites.add(player)
    levelTime = 60.0

if __name__ == "__main__":
    pygame.init()
        
    cur_level = 0
        
    levels = []
    levels.append("../assets/maps/Level1.tmx")
    levels.append("../assets/maps/Level2.tmx")
    levels.append("../assets/maps/Level3.tmx")
    levels.append("../assets/maps/Level4.tmx")
    levels.append("../assets/maps/Level5.tmx")
    levels.append("../assets/maps/Level6.tmx")
    levels.append("../assets/maps/Level7.tmx")
    levels.append("../assets/maps/Level8.tmx")
    levels.append("../assets/maps/Level9.tmx")
    levels.append("../assets/maps/Level10.tmx")
    
    levels_text = []
    levels_text.append("Level 1\n\nToday a freak meteor hit an orbiting space station and caused\nit to fall out of orbit. We have calculated that it will hit Boxopolis and we need\nyour help to find our best astronaut and our rocket ship. We only have\n60 seconds to get our astronaut into space before the space station is too\nclose to stop.")
    levels_text.append("Level 2\n\nThe neighboring nation of Grasslandia has just declared war on\nBoxopolis, their army is already on their way to our capital and we need you to help\nus assemble our army. We need you to find our military airships, our troops\nand the general. Their army is approaching quickly so you only have\n60 seconds before they reach our capital.")
    levels_text.append("Level 3\n\nOur scientists have recent discovered a deadly disease that has\nbeen spreading through the population of Boxopolis. Our scientists have found a\ncure, but don't have the materials necessary to produce enough for the rest of the\npopulation.It is up to you to find the materials they need. The disease is spreading\nquickly so you only have 60 seconds to help the scientists with their cure.")
    levels_text.append("Level 4\n\nThe ambassador from the local neighboring country of Bearland was on his\nway to our capital to discuss our relations as countries. His motorcade was\nlost and we need your help to find him, find our diplomat and find the materials for\nthe meeting. Relations between Bearland and Boxopolis are rocky at best and if\nthis meeting doesn't happen soon they will declare war. You only\nhave 60 seconds before they declare war.")
    levels_text.append("Level 5\n\nThe Capitol of Boxopolis is being attacked by a wild dinosaur. Our leader\nhas determined that the best way to fight this dinosaur is to use our own giant\ndinosaurs along with our fearless general in his plane. We need you to find the\ndinosaur, the plane and our general. Our capitol city is being destroyed quickly\nso you only have 60 seconds before the city is destroyed.")
    levels_text.append("Level 6\n\nOur espionage teams have recovered information that points to you being\nabducted and taken to the mad doctor's office. Our leader has a plan, but he\nneeds your help before he can put his plan into action. He needs to gather our army,\nbuilding materials and the Special Forces unit to help our leader keep you hidden\nand safe. This information doesn't point to when you will be abducted\nso our leader has decided that if you don't come back within\n60 seconds you will be presumed abducted.")
    levels_text.append("Level 7\n\nA great fire approaches the capitol city. We need your help to find our\nfire brigade to help put out the fire and our armed forces to supplement our\nfire brigade. The fire comes closer every second so you only have 60 seconds\nto put out the fire.")
    levels_text.append("Level 8\n\nOur scientists have found a meteor hurtling towards Boxopolis and we only\nhave a short amount of time to stop it. We need you to find and bring back\nour best astronauts, our rocket and something to break the meteor with. The meteor\nis getting closer at a rapid pace so you only have 60 seconds before the meteor is\ntoo close to do anything about.")
    levels_text.append("Level 9\n\nLooks like the army ants are on the move. We need to be ready in case they\nattack. They move quickly so you only have 60 seconds to find supplies of\nfood, fortification materials, and extra vehicles in case civilians need to be\nevacuated.")
    levels_text.append("Level 10\n\nThe army ants attacked and we are defenseless. We need you to do everything\nin your power to help save the capitol of Boxopolis. We need every service\nperson and vehicle we can find. We need you to find the Fire brigade, our General,\nthe Special Forces unit, the air units and our army. Good luck, you only have\n60 seconds.")
    
    levelTime = 60.0
    state = START_MENU
    goal_obstacles = []
    screen = pygame.display.set_mode((1024, 768), HWSURFACE|DOUBLEBUF)
    tileset = Tileset("../assets/maps/Level1.tmx")
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
    desc_bg = pygame.Surface((1024, 768)).convert()
    desc_bg.fill((255, 255, 255))
    
    while 1:
        clock.tick(60)
        
        for e in pygame.event.get():
            if e.type == QUIT:
                sys.exit()
            elif e.type == KEYDOWN:
                {START_MENU: start_menu_key,
                 GAME: game_key,
                 WIN_MENU: win_menu_key,
                 LOSE_MENU: lose_menu_key,
                 DESC_MENU: desc_menu_key}[state](e)
        
        {START_MENU: start_menu,
         GAME: game,
         WIN_MENU: win_menu,
         LOSE_MENU: lose_menu,
         DESC_MENU: desc_menu}[state]()
        
        pygame.display.flip()
        pygame.display.update()
    
#So that's what a fire truck looks like!