'''
File: alien_invasion.py
Contributor: Alexis Boucouvalas
Created: 9.7.2023

Extra Stuff:
This module is the main entrypoint for the alien invasion game.
'''

import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button

def run_game():
    '''
    it runs the game
    '''
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    pygame.display.set_caption('Alien Invasion')

    play_button = Button(ai_settings, screen, 'Play')

    stats = GameStats(ai_settings)

    ship = Ship(ai_settings, screen)

    bullets = Group()

    aliens = Group()

    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:
        # watch for keyboard & mouse movements
        gf.check_events(ai_settings, screen, stats, play_button, ship, bullets)
        
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)
  
run_game()