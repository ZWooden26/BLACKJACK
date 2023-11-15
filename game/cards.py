import pygame
import sys
from parameters import *
import random

values = ['02', '03', '04', '05', '06', '07', '08', '09', '10', 'J', 'Q', 'K', 'A']
suits = ['clubs', 'diamonds', 'spades', 'hearts']

def get_card(self):
    num = random.randint(0, len(values))
    value = values[num]
    num = random.randint(0, len(suits))
    suit = suits[num]
class Cards(pygame.sprite.Sprite):
    def __init__(self, suit, value):
        super().__init__(suit, value)
        self.suit = suit
        self.value = value
        self.image = pygame.image.load(f"../Assets/cards/card_{self.suit}_{self.value}.png").convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        