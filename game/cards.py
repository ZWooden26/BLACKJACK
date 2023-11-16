import pygame
import sys
from parameters import *
import random

pygame.init()

# lists of all possible values and suits to choose from
values = ['02', '03', '04', '05', '06', '07', '08', '09', '10', 'J', 'Q', 'K', 'A']
suits = ['clubs', 'diamonds', 'spades', 'hearts']

# random card generator
def get_value():
    num = random.randint(0, len(values)-1)
    return values[num]
def get_suit():
    num = random.randint(0, len(suits)-1)
    return suits[num]


class Cards(pygame.sprite.Sprite):
    def __init__(self, suit='spades', value='A'):
        super().__init__()
        self.suit = suit
        self.value = value
        self.image = pygame.image.load(f"../Assets/cards/card_{self.suit}_{self.value}.png").convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
