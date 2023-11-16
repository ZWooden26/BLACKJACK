import pygame
import sys
import time
from parameters import *
from background import draw_background
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
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                house1 = Cards(get_suit(), get_value())
                house2 = Cards(get_suit(), get_value())
                screen.blit(house1.image, (HOUSEx - card_size, HOUSEy))
                screen.blit(cardback, (HOUSEx, HOUSEy))

    pygame.display.flip()

pygame.quit()
sys.exit()
