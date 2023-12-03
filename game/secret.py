import pygame
from parameters import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
text_font = pygame.font.Font('../Assets/Black_Crayon.ttf', 50)

def easter_egg():
    chawn = pygame.image.load('../Assets/chawn.png').convert()
    text = text_font.render("CHAWNMOWER", True, (75, 0, 75), (255, 255, 255))
    screen.blit(chawn, (0, 0))
    screen.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2))
    pygame.display.flip()