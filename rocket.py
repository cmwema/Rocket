import pygame
import sys

class Rocket:
    def __init__(self, settings, screen):
        self.screen = screen
        self.settings = settings
        self.image = pygame.image.load('images/rocket.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #movement
        self.moving_up = False
        self.moving_down= False
        self.moving_left = False
        self.moving_right = False

        #start with the rocket at the center
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.rocket_speed_factor
        
        if self.moving_left and self.rect.left > 0:
            self.center -= self.settings.rocket_speed_factor

        if self.moving_down and self.rect.centery < 500:
            self.rect.centery += self.settings.rocket_speed_factor
        
        if self.moving_up and self.rect.centery > 0:
            self.rect.centery -= self.settings.rocket_speed_factor

        self.rect.centerx = self.center
