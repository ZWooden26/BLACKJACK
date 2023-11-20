import pygame
from parameters import *
import random

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

cardback = pygame.image.load('../Assets/cards/card_back.png').convert()

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

    def card_num(self):
        if self.value == 'J' or 'Q' or 'K':
            card_number = 10
        elif self.value == 'A':
            card_number = 11
        else:
            card_number = int(self.value)
        return card_number


cards = pygame.sprite.Group()


# generate house cards
def get_house():
    house1 = Cards(get_suit(), get_value())
    house2 = Cards(get_suit(), get_value())
    h1 = house1.card_num()
    h2 = house2.card_num()
    screen.blit(house1.image, (HOUSEx - card_size, HOUSEy))
    screen.blit(cardback, (HOUSEx, HOUSEy))
    return h1 + h2


# generate player cards
def get_player():
    player1 = Cards(get_suit(), get_value())
    player2 = Cards(get_suit(), get_value())
    p1 = player1.card_num()
    p2 = player2.card_num()
    screen.blit(player1.image, (PLAYERx - card_size, PLAYERy))
    screen.blit(player2.image, (PLAYERx, PLAYERy))
    return p1 + p2


# evaluate player vs house to determine payout
def get_winner(house_value, player_value):
    if player_value == 21:
        if house_value != 21:
            winner = 'player'
        elif house_value == 21:
            winner = 'push'
    elif player_value < 21:
        if house_value > 21:
            winner = 'player'
        elif house_value < player_value:
            winner = 'player'
        elif house_value > player_value:
            winner = 'house'
        elif house_value == player_value:
            winner = 'push'
    else:
        if house_value <= 21:
            winner = 'house'
        else:
            winner = 'push'
    return winner
