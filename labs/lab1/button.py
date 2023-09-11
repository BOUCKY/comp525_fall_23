import pygame.font

class Button():
    '''
    Filled rectangle with label
    '''
    def __init__(self, ai_settings, screen, msg):
        '''
        Initialize button attr
        '''
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # set dimensions & properties of button
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # build button's rect & center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # button msg only needs to be prepped once
        self.prep_msg(msg)

    def prep_msg(self, msg):
        '''
        Turns msg into rendered img & center on button
        '''
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        '''
        Draw blank button then draw message
        '''
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)