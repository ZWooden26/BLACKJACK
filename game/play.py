import pygame
import sys
import time
from parameters import *
from background import draw_background, game_over
from cards import Cards, get_winner, get_house, get_player, add_card, get_score

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
            elif event.key == pygame.K_TAB:
                action = 'start'
    return action


while True:
    screen.blit(background, (0, 0))
    event = get_event()
    if event == 'quit':
        pygame.quit()
        sys.exit()

    elif event == 'raise':
        bet += 5
        score -= 5
        if score < 0:
            score = 0
            bet -= 5
        bet_text = text_font.render(f'{bet}', True, (0, 40, 0))
        score_text = text_font.render(f'{score}', True, (0, 40, 0))
        screen.blit(bet_text, (150, HEIGHT - 75))
        screen.blit(score_text, (WIDTH - 200, HEIGHT - 75))
        pygame.display.update(150, HEIGHT - 75, bet_text.get_width(), bet_text.get_height())
        pygame.display.update(WIDTH - 200, HEIGHT - 75, score_text.get_width() + 15, score_text.get_height())

    elif event == 'lower':
        bet -= 5
        score += 5
        if bet < 0:
            bet = 0
            score -= 5
        bet_text = text_font.render(f'{bet}', True, (0, 40, 0))
        score_text = text_font.render(f'{score}', True, (0, 40, 0))
        screen.blit(bet_text, (150, HEIGHT - 75))
        screen.blit(score_text, (WIDTH - 200, HEIGHT - 75))
        pygame.display.update(150, HEIGHT - 75, bet_text.get_width() + 15, bet_text.get_height())
        pygame.display.update(WIDTH - 200, HEIGHT - 75, score_text.get_width() + 15, score_text.get_height())

    elif event == 'start':
        house = get_house()
        player = get_player()
        house_hand = text_font.render(f"{house[-1]}", True, (0, 40, 0))
        player_hand = text_font.render(f"{player[-1]}", True, (0, 40, 0))
        house[0].show_card(HOUSEx - card_size, HOUSEy)
        screen.blit(cardback, (HOUSEx, HOUSEy))
        player[0].show_card(PLAYERx - card_size, PLAYERy)
        player[1].show_card(PLAYERx, PLAYERy)
        # screen.blit(house_hand, (HOUSEx - house_hand.get_width() / 2, HOUSEy + card_size))
        screen.blit(player_hand, (PLAYERx - player_hand.get_width() / 2, PLAYERy - player_hand.get_height()))
        pygame.display.update(HOUSEx - card_size, HOUSEy - card_size / 2, card_size * 2, card_size * 2)
        pygame.display.update(PLAYERx - card_size, PLAYERy, card_size * 2, card_size)
        pygame.display.flip()
        event = get_event()

    if event == 'hit':
        new = add_card()
        newsum = text_font.render(f"{player[-1] + new[1]}", True, (0, 40, 0))
        new[0].show_card(PLAYERx + card_size, PLAYERy)
        screen.blit(newsum, (PLAYERx - newsum.get_width()/2, PLAYERy - newsum.get_height()))
        pygame.display.update(PLAYERx + card_size, PLAYERy, card_size, card_size)
        pygame.display.update(PLAYERx - newsum.get_width()/2, PLAYERy - newsum.get_height(), newsum.get_width(), newsum.get_height())
        event = get_event()

    elif event == 'cashout':
        over = True
        #winner = get_winner(house[-1], newsum)
        #final = get_score(score, 5, winner)
        #score_text =
        while over:
            game_over(score)
            pygame.display.flip()
            event = get_event()
            if event:
                over = False

    pygame.time.Clock().tick(45)
