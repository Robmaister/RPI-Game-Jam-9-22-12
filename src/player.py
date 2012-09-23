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

class Player(pygame.sprite.Sprite):
    def __init__(self, (x, y), speed, collide_lambda, fps=10):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = resources.load_image("../assets/images/player/front1.bmp", -1)
        self.rect.move_ip(x, y)
        self.speed = speed
        self.walls = []
        self.obstacles = []
        self.collide_obstacle = collide_lambda
        self._start = pygame.time.get_ticks()
        self._delay = 1000 / fps
        self._last_update = 0
        self._frame = 0
        self.anim_paused = True
        self.forward_images = []
        self.backward_images = []
        self.left_images = []
        self.right_images = []
        self.forward_images.append(resources.load_image_no_rect("../assets/images/player/front1.bmp", -1))
        self.forward_images.append(resources.load_image_no_rect("../assets/images/player/front2.bmp", -1))
        self.forward_images.append(resources.load_image_no_rect("../assets/images/player/front3.bmp", -1))
        self.backward_images.append(resources.load_image_no_rect("../assets/images/player/back1.bmp", -1))
        self.backward_images.append(resources.load_image_no_rect("../assets/images/player/back2.bmp", -1))
        self.backward_images.append(resources.load_image_no_rect("../assets/images/player/back3.bmp", -1))
        self.left_images.append(resources.load_image_no_rect("../assets/images/player/left1.bmp", -1))
        self.left_images.append(resources.load_image_no_rect("../assets/images/player/left2.bmp", -1))
        self.right_images.append(resources.load_image_no_rect("../assets/images/player/right1.bmp", -1))
        self.right_images.append(resources.load_image_no_rect("../assets/images/player/right2.bmp", -1))
        self._images = self.forward_images
        self.update_anim(pygame.time.get_ticks())
        
    def set_walls(self, walls):
        self.walls = walls  
        
    def set_obstacles(self, obstacles):
        self.obstacles = obstacles 

    def update_anim(self, t):
        if not self.anim_paused:
            if t - self._last_update > self._delay:
                self._frame += 1
                if self._frame >= len(self._images): self._frame = 0
                self.image = self._images[self._frame]
                self._last_update = t
            
    def pause(self):
        self.anim_paused = True
        
    def play(self):
        self.anim_paused = False

    def move_forward(self):
        self.move(0, -self.speed)
        self._images = self.backward_images
        self.play()
        
    def move_backwards(self):
        self.move(0, self.speed)
        self._images = self.forward_images
        self.play()
        
    def move_left(self):
        self.move(-self.speed, 0)
        self._images = self.left_images
        self.play()
        
    def move_right(self):
        self.move(self.speed, 0)
        self._images = self.right_images
        self.play()
        
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