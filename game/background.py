import pygame
import sys
from parameters import *


def draw_background(screen):
    # initializing images and fonts
    table = pygame.image.load('../Assets/table1.jpg').convert()
    cardback = pygame.image.load('../Assets/cards/card_back.png').convert()
    chip = pygame.image.load('../Assets/chip.png').convert()
    cardback.set_colorkey((0, 0, 0))
    chip.set_colorkey((255, 255, 255))
    names_font = pygame.font.Font('../Assets/Trocadero.ttf', 30)
    text_font = pygame.font.Font('../Assets/Marlboro.ttf', 20)

    # blit table, center card stack, and chip stack
    screen.blit(table, (0, 0))
    for y in range(20):
        screen.blit(cardback, (WIDTH / 2 - card_size / 2, HEIGHT / 1.85 - (2 * y)))
        screen.blit(chip, (700, 500 - (2.5 * y)))

    # render and blit text on-screen
    instructions = text_font.render("'ENTER' to hit\t'SPACE' to stay\t"
                                    "UP arrow to raise\tDOWN arrow to decrease bet\t"
                                    "'Q' to cash out",
                                    True, (0, 0, 0))
    bet_text = text_font.render("Bet:", True, (0, 0, 0))
    score_text = text_font.render("Score:", True, (0, 0, 0))
    player_text = names_font.render("Player", True, (75, 0, 0))
    house_text = names_font.render("House", True, (75, 0, 0))
    screen.blit(instructions, (10, 10))
    screen.blit(bet_text, (150, HEIGHT - 100))
    screen.blit(score_text, (WIDTH - 200, HEIGHT - 100))
    screen.blit(player_text, (WIDTH/2 - player_text.get_width()/2, 550))
    screen.blit(house_text, (WIDTH/2 - house_text.get_width()/2, 50))
