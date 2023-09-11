import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''
    Create bullet object at ship's location
    '''
    def __init__(self, ai_settings, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen

        # Create bullet rect at (0, 0), then set correct pos
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # store bullet's pos
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor


    def update(self):
        '''
        Move the bullet up towards aliens
        '''
        # update decimal pos of bullet
        self.y -= self.speed_factor
        # update rect pos
        self.rect.y = self.y

    def draw_bullet(self):
        '''
        Draw the bullets
        '''
        pygame.draw.rect(self.screen, self.color, self.rect)