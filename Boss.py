import pygame
from Env import *
from os import path
class Boss(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load(path.join(img_dir, "ship.png"))
        self.image = pygame.transform.scale(image, (50, 30))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speedx=8
        self.speedy=8

    def update(self):
        self.keyEventHandling()
        self.rect.y += self.speedy
        if self.now-self.last_shot>SHOT_DELAY:
            self.shoot_boss()
            self.last_shot=self.now

    def shoot_boss(self):
        sound_pew.play()
        bullet = Bullet_enemy(self.rect.centerx,self.rect.centery)
        bullets_enemies.add(bullet)
        all_sprites.add(bullet)