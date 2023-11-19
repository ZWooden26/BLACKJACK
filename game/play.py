import pygame
import sys
import time
from parameters import *
from background import draw_background, get_house, get_player, get_winner
from cards import get_suit, get_value, Cards

# initialize
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blackjack")
clock = pygame.time.Clock()
# sounds

# ------- Main Loop -------
cardback = pygame.image.load('../Assets/cards/card_back.png').convert()
running = True
background = screen.copy()
draw_background(background)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                get_house()

    screen.blit(background, (0, 0))
    pygame.display.flip()

pygame.quit()
sys.exit()
