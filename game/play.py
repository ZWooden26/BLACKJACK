import pygame
import sys
import time
from parameters import *
from background import draw_background, game_over
from cards import get_suit, get_value, Cards, get_winner, get_house, get_player

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

def get_event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return 'quit'
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                return 'space'
            elif event.key == pygame.K_q:
                return 'q'


while True:
    screen.blit(background, (0, 0))
    event = get_event()
    if event == 'quit':
        pygame.quit()
        sys.exit()
    elif event == 'space':
        showcards = True
        while showcards: # andrew helped here
            for i in range (1):
                get_house()
                get_player()
            pygame.display.flip()
            pygame.time.Clock().tick(20)

    elif event == 'q':
        game_over()

    pygame.display.flip()
    pygame.time.Clock().tick(45)
