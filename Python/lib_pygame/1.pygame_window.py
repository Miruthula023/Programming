import pygame

import sys

pygame.init()

screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("window")

run = True

while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	screen.fill((0,0,0))
	pygame.display.update()


pygame.quit()
sys.exit()
