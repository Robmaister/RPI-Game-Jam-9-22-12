import pygame
import resources
from pygame.math import Vector2

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, name, obs_type):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = resources.load_image("../assets/images/objs/" + name + ".bmp", -1)
        self.rect.move_ip(x, y)
        self.obs_type = obs_type
        self.name = name
        
    def get_rect(self):
        return self.rect
    
    def get_obs_type(self):
        return self.obs_type
    
    def get_name(self):
        return self.name