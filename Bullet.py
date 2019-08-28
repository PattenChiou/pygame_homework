import pygame
from os import path
from Env import *
img_dir = path.join(path.dirname(__file__), 'img')
import random
import numpy
class Bullet(pygame.sprite.Sprite):
    speedy=10
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(path.join(img_dir, "laser_gun.png"))
        self.rect = self.image.get_rect()
        self.rect.centerx = posx
        self.rect.centery = posy
        #self.speedy = 10

    def update(self):
        self.rect.y -= self.speedy
        if self.rect.bottom < 0:
            self.kill()
class Bullet_enemy(pygame.sprite.Sprite):
    speedy=10
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(path.join(img_dir, "laser_gun.png"))
        self.rect = self.image.get_rect()
        self.rect.centerx = posx
        self.rect.centery = posy
        #self.speedy = 10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom > HEIGHT:
            self.kill()
class Bullet_boss(pygame.sprite.Sprite):
    speedy=100
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(path.join(img_dir, "laserBlue07.png"))
        self.rect = self.image.get_rect()
        self.rect.centerx = posx
        self.rect.centery = posy
        self.image_origin=self.image
        self.rot_angle=5
        self.angle=0
        #self.speedy = 10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom > HEIGHT:
            self.kill()
class Bullet_boss2(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(path.join(img_dir, "laserBlue07.png"))
        self.rect = self.image.get_rect()
        self.rect.centerx = posx
        self.rect.centery = posy
        self.image_origin=self.image
        self.rot_angle=random.randint(0,360)
        self.speedx=-10*numpy.sin(self.rot_angle)
        self.speedy=10*numpy.cos(self.rot_angle)
        self.angle=0
        #self.speedy = 10


        old_center=self.rect.center
        self.angle=self.angle+self.rot_angle
        self.image=pygame.transform.rotate(self.image_origin,self.angle)
        self.rect=self.image.get_rect()
        self.rect.center=old_center

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.bottom > HEIGHT:
            self.kill()