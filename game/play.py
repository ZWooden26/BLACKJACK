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

# chip for blitting
chip = pygame.image.load('../Assets/chip.png').convert()
chip.set_colorkey((255, 255, 255))

# ------- Main Loop -------
cardback = pygame.image.load('../Assets/cards/card_back.png').convert()
hit = 0
background = screen.copy()
draw_background(background)
player_values = []
house_values = []
new_cards = []
new_house = []


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
        for x in range(bet):
            screen.blit(chip, (WIDTH/2 + 100, HEIGHT/2 - (2.5*x)))
        for x in range(score):
            screen.blit(chip, (700, 500 - (2.5 * x)))
        bet_text = text_font.render(f'{bet}', True, (0, 40, 0))
        score_text = text_font.render(f'{score}', True, (0, 40, 0))
        screen.blit(bet_text, (150, HEIGHT - 75))
        screen.blit(score_text, (WIDTH - 200, HEIGHT - 75))
        pygame.display.update(150, HEIGHT - 75, bet_text.get_width(), bet_text.get_height())
        pygame.display.update(WIDTH - 200, HEIGHT - 75, score_text.get_width() + 15, score_text.get_height())
        pygame.display.update(WIDTH/2 + 100, HEIGHT/2 - 100, chip_size, 100 + chip_size)
        pygame.display.update(700, HEIGHT/2, chip_size, HEIGHT/2)

    elif event == 'lower':
        bet -= 5
        score += 5
        if bet < 0:
            bet = 0
            score -= 5
        for x in range(bet):
            screen.blit(chip, (WIDTH/2 + 100, HEIGHT/2 - (2.5*x)))
        for x in range(score):
            screen.blit(chip, (700, 500 - (2.5 * x)))
        bet_text = text_font.render(f'{bet}', True, (0, 40, 0))
        score_text = text_font.render(f'{score}', True, (0, 40, 0))
        screen.blit(bet_text, (150, HEIGHT - 75))
        screen.blit(score_text, (WIDTH - 200, HEIGHT - 75))
        pygame.display.update(150, HEIGHT - 75, bet_text.get_width() + 15, bet_text.get_height())
        pygame.display.update(WIDTH - 200, HEIGHT - 75, score_text.get_width() + 15, score_text.get_height())
        pygame.display.update(WIDTH / 2 + 100, HEIGHT / 2 - 100, chip_size, 100 + chip_size)
        pygame.display.update(700, HEIGHT / 2, chip_size, HEIGHT / 2)

    elif event == 'start':
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
        player_hand = text_font.render(f"{player[-1]}", True, (0, 40, 0))
        house_hand = text_font.render(f"{house[-1]}", True, (0, 40, 0))
        house[0].show_card(HOUSEx - card_size, HOUSEy)
        screen.blit(cardback, (HOUSEx, HOUSEy))
        player[0].show_card(PLAYERx - card_size, PLAYERy)
        player[1].show_card(PLAYERx, PLAYERy)
        screen.blit(player_hand, (PLAYERx - player_hand.get_width() / 2, PLAYERy - player_hand.get_height()))
        pygame.display.update(HOUSEx - card_size, HOUSEy - card_size / 2, card_size * 2, card_size * 2)
        pygame.display.update(PLAYERx - card_size, PLAYERy, card_size * 2, card_size)
        pygame.display.flip()
        event = get_event()

    if event == 'hit':
        # add cards to player hand and update value
        new = add_card()
        new_cards.append(new[0])
        player_values.append(new[1])
        newsum = text_font.render(f"{sum(player_values)}", True, (0, 40, 0))
        screen.blit(newsum, (PLAYERx - newsum.get_width() / 2, PLAYERy - newsum.get_height()))
        for x in range(len(new_cards)):
            new_cards[x].show_card(PLAYERx + ((x+1) * card_size * ((-1)**(x))), PLAYERy)
            pygame.display.update(PLAYERx + ((x+1) * card_size * ((-1)**(x))), PLAYERy, card_size, card_size)
        pygame.display.update(PLAYERx - newsum.get_width()/2, PLAYERy - newsum.get_height(), newsum.get_width(),
                              newsum.get_height())
        event = get_event()

    elif event == 'stay':
        # show house and hit on any value less than 17
        house[1].show_card(HOUSEx, HOUSEy)
        screen.blit(house_hand, (HOUSEx - house_hand.get_width() / 2, HOUSEy + card_size))
        pygame.display.update(HOUSEx, HOUSEy, card_size, card_size)
        pygame.display.update(HOUSEx - house_hand.get_width() / 2, HOUSEy + card_size, house_hand.get_width(),
                              house_hand.get_height())
        pygame.time.Clock().tick(5)
        if sum(house_values) < 17:
            new = add_card()
            new_house.append(new[0])
            house_values.append(new[1])
            newsum = text_font.render(f"{sum(house_values)}", True, (0, 40, 0))
            screen.blit(newsum, (HOUSEx - newsum.get_width() / 2, HOUSEy + card_size))
            for x in range(len(new_house)):
                new_house[x].show_card(HOUSEx + ((x + 1) * card_size * ((-1) ** (x))), HOUSEy)
                pygame.display.update(HOUSEx + ((x + 1) * card_size * ((-1) ** (x))), HOUSEy, card_size, card_size)
            pygame.display.update(HOUSEx - newsum.get_width() / 2, HOUSEy + card_size, newsum.get_width(),
                                  newsum.get_height())
            pygame.time.Clock().tick(5)
        else:
            pass

        event = get_event()

    elif event == 'cashout':
        hit = 0
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
