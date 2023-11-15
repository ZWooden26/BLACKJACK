import pygame
import sys
from parameters import *

def draw_background(screen):
    # initializing images and fonts
    table = pygame.image.load('../Assets/table1.jpg').convert()
    cardback = pygame.image.load('../Assets/cards/card_back.png').convert()
    chip = pygame.image.load(' ').convert()
    table.set_colorkey((0, 0, 0))
    cardback.set_colorkey((0, 0, 0))
    chip.set_colorkey((0, 0, 0))
    title_font = pygame.font.Font('../Assets/Trocadero.ttf', 100)
    names_font = pygame.font.Font('../Assets/Trocadero.ttf', 50)
    text_font = pygame.font.Font('../Assets/Marlboro.ttf', 30)

    # render and blit text on-screen
    title = title_font.render('BLACKJACK', True, (0, 0, 0))
    instructions = text_font.render("'ENTER' to hit\n'SPACE' to stay\n"
                                    "UP arrow to raise\nDOWN arrow to decrease bet\n"
                                    "Home icon to cash out and go home",
                                    True, (0, 0, 0))
    bet_text = text_font.render("Bet:", True, (0, 0, 0))
    score_text = text_font.render("Score:", True, (0, 0, 0))
    player_text = names_font.render("Player", True, (0, 0, 0))
    house_text = names_font.render("House", True, (0, 0, 0))
    screen.blit(title, (WIDTH/2 - title.get_width()/2, 10))
    screen.blit(instructions, (10, 10))
    screen.blit(bet_text, (150, HEIGHT - 100))
    screen.blit(score_text, (WIDTH - 150, HEIGHT - 100))
    screen.blit(player_text, (WIDTH/2 - player_text.get_width()/2, 500))
    screen.blit(house_text, (WIDTH/2 - house_text.get_width()/2, 200))

    # blit center card stack
    for y in range(20):
        screen.blit(cardback, (WIDTH/2 - card_size/2, HEIGHT/2 + (2*y)))
