import pygame

class Ship():
    def __init__(self, ai_settings, screen):
        '''
        Initialize ship and set starting pos
        '''
        self.screen = screen
        self.ai_settings = ai_settings

        # load ship image & get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # start each new ship at bottom center
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # stoe decimal for ship's center
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        '''
        Update ship's pos based on movement flag
        '''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.ship_speed_factor

        # Update rect object from self.center
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
		
    def center_ship(self):
        """Center the ship on the screen."""
        self.centerx = self.screen_rect.centerx