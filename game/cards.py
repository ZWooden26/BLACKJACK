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
        if self.value == 'J' or self.value == 'Q' or self.value == 'K':
            card_number = 10
        elif self.value == 'A':
            card_number = 11
        else:
            card_number = int(self.value)
        return card_number

    def show_card(self, x, y):
        screen.blit(self.image, (x, y))


cards = pygame.sprite.Group()


# generate house cards
def get_house():
    house1 = Cards(get_suit(), get_value())
    house2 = Cards(get_suit(), get_value())
    h1 = house1.card_num()
    h2 = house2.card_num()
    htotal = h1 + h2
    house = (house1, house2, htotal)
    return house


# generate player cards
def get_player():
    player1 = Cards(get_suit(), get_value())
    player2 = Cards(get_suit(), get_value())
    p1 = player1.card_num()
    p2 = player2.card_num()
    ptotal = p1 + p2
    player = (player1, player2, ptotal)
    return player


def add_card():
    new_card = Cards(get_suit(), get_value())
    val = new_card.card_num()
    new = (new_card, val)
    return new


# evaluate player vs house to determine payout
def get_winner(house_value, player_value):
    if player_value == 21:
        if house_value != 21:
            winner = 'blackjack'
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

def get_score(score, bet, winner):
    if winner == 'blackjack':
        score += (bet * 3)
    elif winner == 'player':
        score += (bet * 2)
    elif winner == 'push':
        score += bet
