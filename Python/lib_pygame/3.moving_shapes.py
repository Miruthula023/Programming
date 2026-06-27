
import pygame
import sys

x = 450
y = 300

speed = 2

screen = pygame.display.set_mode((900,600))
pygame.display.set_caption("Move the shape")

run = True

while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	screen.fill((0,0,0))
	pygame.draw.rect(screen,(225,225,0),(x,y,60,70),3)

	keys = pygame.key.get_pressed()
	if keys[pygame.K_a]:
		x -= speed
	if keys[pygame.K_d]:
		x += speed
	if keys[pygame.K_w]:
		y -= speed
	if keys[pygame.K_s]:
		y += speed

	pygame.display.update()

pygame.quit()
sys.exit()
