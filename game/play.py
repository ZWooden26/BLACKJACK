import pygame
import sys
import time
from parameters import *
from background import draw_background, game_over
from cards import Cards, get_winner, get_house, get_player, add_card

# initialize
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blackjack")
clock = pygame.time.Clock()
# sounds

# fonts
text_font = pygame.font.Font('../Assets/Marlboro.ttf', 20)

# ------- Main Loop -------
cardback = pygame.image.load('../Assets/cards/card_back.png').convert()
running = True
background = screen.copy()
draw_background(background)


def get_event():
    action = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            action = 'quit'
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                action = 'hit'
            elif event.key == pygame.K_q:
                action = 'cashout'
            elif event.key == pygame.K_UP:
                action = 'raise'
            elif event.key == pygame.K_DOWN:
                action = 'lower'
            elif event.key == pygame.K_s:
                action = 'stay'
    return action


while True:
    screen.blit(background, (0, 0))
    event = get_event()
    if event == 'quit':
        pygame.quit()
        sys.exit()

    elif event == 'hit':
        showcards = True
        house = get_house()
        player = get_player()
        house_hand = text_font.render(f"{house[-1]}", True, (0, 40, 0))
        player_hand = text_font.render(f"{player[-1]}", True, (0, 40, 0))

        while showcards:
            # continuously blit cards, Andrew Galvan-Arrien helped me with this section of code
            house[0].show_card(HOUSEx - card_size, HOUSEy)
            screen.blit(cardback, (HOUSEx, HOUSEy))
            player[0].show_card(PLAYERx - card_size, PLAYERy)
            player[1].show_card(PLAYERx, PLAYERy)
            screen.blit(house_hand, (HOUSEx - house_hand.get_width()/2, HOUSEy + card_size))
            screen.blit(player_hand, (PLAYERx - player_hand.get_width()/2, PLAYERy - player_hand.get_height()))
            pygame.display.flip()
            pygame.time.Clock().tick(10)
            event = get_event()
            if event == 'hit':
                running = True
                new = add_card()
                newsum = text_font.render(f"{player[-1] + new[1]}", True, (0, 40, 0))
                while running:
                    new[0].show_card(PLAYERx + card_size, PLAYERy)
                    screen.blit(newsum, (PLAYERx - player_hand.get_width() / 2, PLAYERy - player_hand.get_height()))
                    pygame.display.flip()
                    event = get_event()
                    if event:
                        running = False
            elif event == 'quit':
                pygame.quit()
                sys.exit()
            elif event:
                showcards = False

    elif event == 'cashout':
        over = True
        while over:
            game_over(score=20)
            pygame.display.flip()
            event = get_event()
            if event:
                over = False

    pygame.display.flip()
    pygame.time.Clock().tick(45)
