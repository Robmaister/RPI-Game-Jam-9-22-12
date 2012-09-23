import pygame
import resources
from pygame.math import Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self, (x, y), speed, collide_lambda):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = resources.load_image("../assets/images/player.bmp")
        self.rect.move_ip(x, y)
        self.speed = speed
        self.walls = []
        self.obstacles = []
        self.collide_obstacle = collide_lambda
        
    def set_walls(self, walls):
        self.walls = walls  
        
    def set_obstacles(self, obstacles):
        self.obstacles = obstacles 
    
    def update(self):
        pass

    def move_forward(self):
        self.move(0, -self.speed)  
        
    def move_backwards(self):
        self.move(0, self.speed)
        
    def move_left(self):
        self.move(-self.speed, 0)
        
    def move_right(self):
        self.move(self.speed, 0)
        
    def move(self, x, y):
        self.rect.move_ip(x, y)
        
        for i in self.rect.collidelistall(self.walls):
            r = self.walls[i]
            if x > 0: # Moving right; Hit the left side of the wall
                self.rect.right = r.left
            if x < 0: # Moving left; Hit the right side of the wall
                self.rect.left = r.right
            if y > 0: # Moving down; Hit the top side of the wall
                self.rect.bottom = r.top
            if y < 0: # Moving up; Hit the bottom side of the wall
                self.rect.top = r.bottom
        
        obstacle_to_remove = None
        for o in self.obstacles:
            if self.rect.colliderect(o.get_rect()):
                if x > 0: # Moving right; Hit the left side of the wall
                    self.rect.right = o.get_rect().left
                if x < 0: # Moving left; Hit the right side of the wall
                    self.rect.left = o.get_rect().right
                if y > 0: # Moving down; Hit the top side of the wall
                    self.rect.bottom = o.get_rect().top
                if y < 0: # Moving up; Hit the bottom side of the wall
                    self.rect.top = o.get_rect().bottom
                obstacle_to_remove = self.collide_obstacle(o)
        if obstacle_to_remove is not None:
            self.obstacles.remove(obstacle_to_remove)
            
    def move_to(self, x, y):
        self.rect.left = x
        self.rect.top = y