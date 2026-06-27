import pygame
import sys


pygame.init()

screen = pygame.display.set_mode((500,400))
pygame.display.set_caption("get started")

run = True

while run:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	screen.fill((0,0,13))
	pygame.display.update()

pygame.quit()
sys.exit()
