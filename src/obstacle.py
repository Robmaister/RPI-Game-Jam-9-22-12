#! /usr/bin/env python
#
#Copyright (c) 2012 Robert Rouhani <robert.rouhani@gmail.com>, Nick Richard <richan2@rpi.edu>, Hayden Lee <leeh14@rpi.edu>
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in
#all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

import pygame
import resources

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