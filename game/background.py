import pygame
import sys
from parameters import *

def draw_background(screen):
    # initializing images
    table = pygame.image.load('../Assets/table1.jpg').convert()
    cardback = pygame.image.load('../Assets/cards/card_back.png').convert()
    chip = pygame.image.load(' ').convert()
    table.set_colorkey((0, 0, 0))
    cardback.set_colorkey((0, 0, 0))
    chip.set_colorkey((0, 0, 0))

    # initializing fonts
    title_font = pygame.font.Font('../Assets/Trocadero.ttf')
    text_font = pygame.font.Font('../Assets/Marlboro.ttf')

    # render text on-screen
    title = title_font.render('BLACKJACK', True, (0, 0, 0))
    instructions = text_font.render("'ENTER' to hit\n"
                                    "'SPACE' to stay\n"
                                    "")

    # blit center card stack
    for y in range(20):
        screen.blit(cardback, (WIDTH/2, HEIGHT/2 + y))

