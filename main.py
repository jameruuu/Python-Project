import pygame
from tic_tac import main

run = True
width = 400
height = 300
pygame.init()
screen = pygame.display.set_mode((width, height))
font = pygame.font.SysFont(None, 48)
text = font.render("Tic Tac Toe", True, (255, 255, 255))
screen.blit(text, ((width - text.get_width()) // 2, (height - text.get_height()) // 2))
pygame.display.flip()

# Run the Tic Tac Toe game
victor = main(screen, width, height, font)