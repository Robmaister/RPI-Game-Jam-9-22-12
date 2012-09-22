import pygame
import resources
from pygame.math import Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self, (x, y), speed):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = resources.load_image("../assets/images/player.bmp")
        self.rect.move_ip(x, y)
        self.speed = speed
        
        
    def update(self):
        pass
    
    def move_forward(self):
        self.rect.move_ip(0, -self.speed)  
        
    def move_backwards(self):
        self.rect.move_ip(0, self.speed)
        
    def move_left(self):
        self.rect.move_ip(-self.speed, 0)
        
    def move_right(self):
        self.rect.move_ip(self.speed, 0)     