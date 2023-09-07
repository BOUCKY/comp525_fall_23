'''
File: alien_invasion.py
Contributor: Alexis Boucouvalas
Created: 9.7.2023

Extra Stuff:
This module is the main entrypoint for the alien invasion game.
'''

import sys
import pygame

def run_game():
    '''
    it runs the game
    '''
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption('Alien Invasion')

    while True:
        print('Hello')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.flip()
  
run_game()