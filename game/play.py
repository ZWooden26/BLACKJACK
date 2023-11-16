import pygame
import sys
from parameters import *
from background import draw_background
from cards import get_suit, get_value, Cards

# initialize
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blackjack woohoo")

# sounds

# ------- Main Loop -------
running = True
background = screen.copy()
draw_background(background)

while running:
    screen.blit(background, (0, 0))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()
