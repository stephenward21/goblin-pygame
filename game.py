
# INSTRUCTION IN DAY 4 IN SCHOOLOLOGY
# Include pygame which we got from pip
import pygame
# bring in the math module so we can 
from math import fabs
# in order to use pygame, we have to run the init method

# get the random module
from random import randint

pygame.init()

# Creat a screen with a size.
screen = {
	"height": 516,
	"width": 445
}

keys = {
	"right": 275,
	"left": 276,
	"up": 273,
	"down": 274
}

hero = {
	"x": 100,
	"y": 100,
	"speed": 10,
	"wins": 0
}

goblin = {
	"x": 150,
	"y": 150,
	"speed": 7
}

monster = {
	"x": 175,
	"y": 175,
	"speed": 10
}

chicken_power = {
	"x": 125,
	"y": 125,
	"speed": 2,
	"power": 0
}

keys_down = {
	"right": False,
	"left": False,
	"up": False,
	"down": False
}


screen_size = (screen["height"], screen["width"])
pygame_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Goblin Chase")
background_image = pygame.image.load('images/duckhunter.png')
hero_image = pygame.image.load('images/hero.png')
goblin_image = pygame.image.load('images/goblin.png')
monster_image = pygame.image.load('images/sloth.jpg')
chicken_image = pygame.image.load('images/chicken-leg.jpg')

# Add music files
pygame.mixer.music.load('./sounds/music.wav')
pygame.mixer.music.play(-1)
win_sound = pygame.mixer.Sound('./sounds/win.wav')
lose_sound = pygame.mixer.Sound('./sounds/lose.wav')

# //////  CREATE GAME LOOP //////
game_on = True
while game_on: 
	for event in pygame.event.get():
	# add a quit event
		if event.type == pygame.QUIT:
			game_on = False

		elif event.type == pygame.KEYDOWN:
			if event.key == keys["up"]:
				keys_down['up'] = True
				
			elif event.key == keys["down"]:
				keys_down['down'] = True
				
			elif event.key == keys["left"]:
				keys_down['left'] = True
				
			elif event.key == keys["right"]:
				keys_down['right'] = True
				
		elif event.type == pygame.KEYUP:
			print ("The user let go of a key")
			if event.key == keys["up"]:
				keys_down['up'] = False
				goblin['y'] -= goblin ['speed']
			if event.key == keys["down"]:
				keys_down['down'] = False
				goblin['y'] += goblin ['speed']
			if event.key == keys["left"]:
				keys_down['left'] = False
				goblin['x'] -= goblin ['speed']
			if event.key == keys["right"]:
				keys_down['right'] = False
				goblin['x'] += goblin['speed']


	# Update Hero position
	if keys_down['up']:
		hero['y'] -= hero ['speed']
	elif keys_down['down']:
		hero['y'] += hero ['speed']
	if keys_down ['left']:
		hero['x'] -= hero ['speed']
	elif keys_down['right']:
		hero['x'] += hero['speed']


	# if keys_down['up']:
	# 	goblin['y'] -= goblin ['speed']
	# elif keys_down['down']:
	# 	goblin['y'] += goblin ['speed']
	# if keys_down ['left']:
	# 	goblin['x'] -= goblin ['speed']
	# elif keys_down['right']:
	# 	goblin['x'] += goblin['speed']

	# COLLISSION DETECTION!!
	distance_between = fabs(hero['x'] - goblin['x']) + (hero['y'] - goblin['y'])
	
	if (distance_between < 32):
		# the hero and goblin are touching!
		print ("Collision!!")
		# Generate a random X > 0, X < screen['width']
		# Generate a random Y > 0, Y < screen['height']
		rand_x = randint(0, screen['width'])
		rand_y = randint(0, screen['height'])
		goblin['x'] = rand_x
		goblin['y'] = rand_y
		

		hero['wins'] += 1

		win_sound.play()

	distance_between = fabs(hero['x'] - monster['x']) + (hero['y'] - monster['y'])

	if (distance_between < 56):
		print ("The monster killed the Hero!")
		rand_x = randint(0, screen['width'])
		rand_y = randint(0, screen['height'])
		monster['x'] = rand_x
		monster['y'] = rand_y


	distance_between = fabs(hero['x'] - chicken_power['x']) + (hero['y'] - chicken_power['y'])

	if (distance_between < 30):
		print ("Power Up!")
		rand_x = randint(0, screen['width'])
		rand_y = randint(0, screen['height'])
		chicken_power['x'] = rand_x
		chicken_power['y'] = rand_y

		chicken_power['power'] += 1







	# RENDER:
	# blit takes two arguments
	# 1. What?
	# 2. Where?
	#draw background
	pygame_screen.blit(background_image, [0,0]) 

	# Draw the hero wins on the screen
	font = pygame.font.Font(None, 25)
	wins_text = font.render("Wins %d" % (hero['wins']), True, (0, 0, 0))
	pygame_screen.blit(wins_text, [40,40])

	# Draw the hero powers up on screen when he gets the Turkey
	font = pygame.font.Font(None, 25)
	powers_text = font.render("Power - Ups %d" % (chicken_power['power']), True, (0, 0, 0))
	pygame_screen.blit(powers_text, [60,60])

	#draw hero
	draw_hero = pygame_screen.blit(hero_image, [hero['x'], hero['y']])
	draw_goblin = pygame_screen.blit(goblin_image, [goblin['x'], goblin['y']])
	draw_monster = pygame_screen.blit(monster_image, [monster['x'], monster['y']])
	draw_chicken = pygame_screen.blit(chicken_image, [chicken_power['x'], chicken_power['y']])

	pygame.display.flip()
	# Flip the screen and start over