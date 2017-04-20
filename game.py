
# Include pygame which we got from pip
import pygame

# in order to use pygame, we have to run the init method
pygame.init()

# Creat a screen with a size.
screen = {
	"height": 512,
	"width": 480
}

screen_size = (screen["height"], screen["width"])
pygame_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Goblin Chase")

# create the game loop
game_on = True
while game_on: 

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_on = False