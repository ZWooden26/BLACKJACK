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

# chip for blitting and table piece
chip = pygame.image.load('../Assets/chip.png').convert()
chip.set_colorkey((255, 255, 255))
table_piece = pygame.image.load('../Assets/table_snip.jpg').convert()

# ------- Main Loop -------
cardback = pygame.image.load('../Assets/cards/card_back.png').convert()
hit = 0
background = screen.copy()
draw_background(background)
player_values = []
house_values = []
new_cards = []
new_house = []
previous = None


def get_event():
    # retrieves event and returns a string to compare in main loop if statements
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
                action = 'deal'
            elif event.key == pygame.K_BACKSPACE:
                action = 'start'
    return action


while True:
    screen.blit(background, (0, 0))
    event = get_event()
    if event == 'quit':
        # exit pygame
        pygame.quit()
        sys.exit()

    elif event == 'raise':
        # restrict usage to only when appropriate
        if previous == 'raise' or previous == 'lower' or previous == 'start' or previous == 'stay':
            bet += 5
            score -= 5
            if score < 0:
                score = 0
                bet -= 5
            for x in range(bet):
                screen.blit(chip, (WIDTH/2 + 100, HEIGHT/2 - (2.5*x)))
            for x in range(score):
                screen.blit(chip, (700, 500 - (2.5 * x)))
            bet_text = text_font.render(f'{bet}', True, (0, 40, 0), (255, 255, 255))
            score_text = text_font.render(f'{score}', True, (0, 40, 0), (255, 255, 255))
            screen.blit(bet_text, (150, HEIGHT - 75))
            screen.blit(score_text, (WIDTH - 200, HEIGHT - 75))
            pygame.display.update(150, HEIGHT - 75, bet_text.get_width(), bet_text.get_height())
            pygame.display.update(WIDTH - 200, HEIGHT - 75, score_text.get_width() + 15, score_text.get_height())
            pygame.display.update(WIDTH/2 + 100, HEIGHT/2 - 100, chip_size, 100 + chip_size)
            pygame.display.update(700, HEIGHT/2, chip_size, HEIGHT/2)
            previous = 'raise'
        else:
            pass

    elif event == 'lower':
        # restrict use to only when appropriate
        if previous == 'raise' or previous == 'lower' or previous == 'start' or previous == 'stay':
            bet -= 5
            score += 5
            if bet < 0:
                bet = 0
                score -= 5
            for x in range(bet):
                screen.blit(chip, (WIDTH/2 + 100, HEIGHT/2 - (2.5*x)))
            for x in range(score):
                screen.blit(chip, (700, 500 - (2.5 * x)))
            bet_text = text_font.render(f'{bet}', True, (0, 40, 0), (255, 255, 255))
            score_text = text_font.render(f'{score}', True, (0, 40, 0), (255, 255, 255))
            screen.blit(bet_text, (150, HEIGHT - 75))
            screen.blit(score_text, (WIDTH - 200, HEIGHT - 75))
            pygame.display.update(150, HEIGHT - 75, bet_text.get_width() + 15, bet_text.get_height())
            pygame.display.update(WIDTH - 200, HEIGHT - 75, score_text.get_width() + 15, score_text.get_height())
            pygame.display.update(WIDTH / 2 + 100, HEIGHT / 2 - 100, chip_size, 100 + chip_size)
            pygame.display.update(700, HEIGHT / 2, chip_size, HEIGHT / 2)
            previous = 'lower'
        else:
            pass

    elif event == 'start':
        pygame.display.flip()
        previous = 'start'

    elif event == 'deal':
        # restrict usage
        if previous == 'stay' or previous == 'raise' or previous == 'lower':
            # clear lists on re-start
            player_values = []
            house_values = []
            new_cards = []
            new_house = []

            # fresh hands and blit on screen
            house = get_house()
            player = get_player()
            player_values.append(player[-1])
            house_values.append(house[-1])
            player_hand = text_font.render(f"{player[-1]}", True, (0, 40, 0), (255, 255, 255))
            house_hand = text_font.render(f"{house[-1]}", True, (0, 40, 0), (255, 255, 255))
            house[0].show_card(HOUSEx - card_size, HOUSEy)
            screen.blit(cardback, (HOUSEx, HOUSEy))
            player[0].show_card(PLAYERx - card_size, PLAYERy)
            player[1].show_card(PLAYERx, PLAYERy)
            screen.blit(player_hand, (PLAYERx - player_hand.get_width() / 2, PLAYERy - player_hand.get_height()))
            pygame.display.update(HOUSEx - 2*card_size, HOUSEy, card_size * 4, card_size * 2)
            pygame.display.update(PLAYERx - card_size, PLAYERy, card_size * 2, card_size)
            pygame.display.update(PLAYERx - player_hand.get_width() / 2, PLAYERy - player_hand.get_height(),
                                  player_hand.get_width(), player_hand.get_height())
            #pygame.display.flip()
            previous = 'deal'
        else:
            pass

    elif event == 'hit':
        # restrict usage
        if previous == 'deal' or previous == 'hit':
            # add cards to player hand and update value
            new = add_card()
            new_cards.append(new[0])
            player_values.append(new[1])
            newsum = text_font.render(f"{sum(player_values)}", True, (0, 40, 0), (255, 255, 255))
            screen.blit(newsum, (PLAYERx - newsum.get_width() / 2, PLAYERy - newsum.get_height()))
            for x in range(len(new_cards)):
                new_cards[x].show_card(PLAYERx + ((x+1) * card_size * ((-1)**(x))), PLAYERy)
                pygame.display.update(PLAYERx + ((x+1) * card_size * ((-1)**(x))), PLAYERy, card_size, card_size)
            pygame.display.update(PLAYERx - newsum.get_width()/2, PLAYERy - newsum.get_height(), newsum.get_width(),
                                  newsum.get_height())
            event = get_event()
            previous = 'hit'
        else:
            pass

    elif event == 'stay':
        # restrict usage
        if previous == 'hit' or previous == 'deal':
            # show house hand
            house[1].show_card(HOUSEx, HOUSEy)
            screen.blit(house_hand, (HOUSEx - house_hand.get_width() / 2, HOUSEy + card_size))
            pygame.display.update(HOUSEx, HOUSEy, card_size, card_size)
            pygame.display.update(HOUSEx - house_hand.get_width() / 2, HOUSEy + card_size, house_hand.get_width(),
                                  house_hand.get_height())
            pygame.time.Clock().tick(1)

            # hit on any value less than 17 and update screen
            if sum(house_values) < 17:
                new = add_card()
                new_house.append(new[0])
                house_values.append(new[1])
                newsum = text_font.render(f"{sum(house_values)}", True, (0, 40, 0), (255, 255, 255))
                screen.blit(newsum, (HOUSEx - newsum.get_width() / 2, HOUSEy + card_size))
                pygame.display.update(HOUSEx - newsum.get_width() / 2, HOUSEy + card_size, 100, 50)
                for x in range(len(new_house)):
                    new_house[x].show_card(HOUSEx + ((x + 1) * card_size * ((-1) ** (x))), HOUSEy)
                    pygame.display.update(HOUSEx + ((x + 1) * card_size * ((-1) ** (x))), HOUSEy, card_size, card_size)
                pygame.time.Clock().tick(1)
                # hit again if needed
                if sum(house_values) < 17:
                    new = add_card()
                    new_house.append(new[0])
                    house_values.append(new[1])
                    newsum = text_font.render(f"{sum(house_values)}", True, (0, 40, 0), (255, 255, 255))
                    screen.blit(newsum, (HOUSEx - newsum.get_width() / 2, HOUSEy + card_size))
                    pygame.display.update(HOUSEx - newsum.get_width() / 2, HOUSEy + card_size, 100, 50)
                    for x in range(len(new_house)):
                        new_house[x].show_card(HOUSEx + ((x + 1) * card_size * ((-1) ** (x))), HOUSEy)
                        pygame.display.update(HOUSEx + ((x + 1) * card_size * ((-1) ** (x))), HOUSEy, card_size,
                                              card_size)
                    pygame.time.Clock().tick(1)
                else:
                    pass
            else:
                pass
            # clear cards
            pygame.display.update(PLAYERx - (4*card_size), PLAYERy - 50, 8 * card_size, card_size + 50)

            # compare player and house values, determine winner, and update screen to reflect game outcome
            winner = get_winner(sum(house_values), sum(player_values))
            final_score = get_score(score, bet, winner)
            score_text = text_font.render(f'{final_score}', True, (0, 40, 0), (255, 255, 255))
            screen.blit(score_text, (WIDTH - 200, HEIGHT - 75))
            pygame.display.update(WIDTH - 200, HEIGHT - 75, score_text.get_width() + 15, score_text.get_height())
            pygame.display.update(WIDTH / 2 + 100, HEIGHT / 2 - 100, chip_size, 100 + chip_size)
            score = final_score
            for x in range(score):
                screen.blit(chip, (700, 500 - (2.5 * x)))
                pygame.display.update(700, int(500 - (2.5 * x)), chip_size, chip_size)
            bet = 0
            pygame.display.update(150, HEIGHT - 75, bet_text.get_width() + 15, bet_text.get_height())

            # game over if you have no money left
            if score == 0:
                event = 'cashout'
            previous = 'stay'
        else:
            pass

    elif event == 'cashout':
        # restrict usage
        if previous == 'start' or previous == 'stay':
            # display game over screen with player's remaining cash
            game_over(score)
            pygame.display.flip()
            previous = 'cashout'
        else:
            pass
