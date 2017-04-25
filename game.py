
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
	"x": 150,
	"y": 300,
	"speed": 10,
	"wins": 0
}

goblin = {
	"x": 300,
	"y": 300,
	"speed": 3,
	"direction": "N"
}

monster = {
	"x": 175,
	"y": 175,
	"speed": 10
}


keys_down = {
	"right": False,
	"left": False,
	"up": False,
	"down": False
}

powerup = {
	'active': True,
	'tick_gotten': 0
}

game_paused = False

directions = ["N", "S", "E", "W", "NE", "NW", "SE", "SW"]

screen_size = (screen["height"], screen["width"])
pygame_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Goblin Chase")
background_image = pygame.image.load('images/duckhunter.png')
hero_image = pygame.image.load('images/hero.png')
goblin_image = pygame.image.load('images/goblin.png')
monster_image = pygame.image.load('images/monster.png')
chicken_image = pygame.image.load('images/chicken-leg.jpg')

# Add music files
pygame.mixer.music.load('./sounds/music.wav')
pygame.mixer.music.play(-1)
win_sound = pygame.mixer.Sound('./sounds/win.wav')
lose_sound = pygame.mixer.Sound('./sounds/lose.wav')

tick = 0
timer = 0

# //////  CREATE GAME LOOP //////
game_on = True
while game_on: 
	# update our ticker each time through the loop ~30/sec
	tick += 1
# def game_time(keys):
	for event in pygame.event.get():
	# add a quit event
		if event.type == pygame.QUIT:
			game_on = False

		elif event.type == pygame.KEYDOWN:
		# 	if event.key == keys['up' or 'down' or 'left' or 'right']:
		# 		return keys_down == True

			if event.key == keys['up']:
				keys_down['up'] == True
				
			elif event.key == keys["down"]:
				keys_down['down'] = True
				
			elif event.key == keys["left"]:
				keys_down['left'] = True
				
			elif event.key == keys["right"]:
				keys_down['right'] = True
				
		elif event.type == pygame.KEYUP:
			print ("The user let go of a key")
			if event.key == keys['up']:	
				keys_down['up'] = False
				
			if event.key == keys["down"]:
				keys_down['down'] = False
				
			if event.key == keys["left"]:
				keys_down['left'] = False
				
			if event.key == keys["right"]:
				keys_down['right'] = False
				
		
	if (not game_paused):
	# Update Hero position
		if keys_down['up']:
			hero['y'] -= hero['speed']
		elif keys_down['down']:
			hero['y'] += hero['speed']
		if keys_down ['left']:
			hero['x'] -= hero['speed']
		elif keys_down['right']:
			hero['x'] += hero['speed']


		if (goblin['direction'] == "N"):
			goblin['y'] -= goblin['speed']
		elif (goblin['direction'] == "S"):
			goblin['y'] += goblin['speed']
		elif (goblin['direction'] == "E"):
			goblin['x'] += goblin['speed']
		elif (goblin['direction'] == "W"):
			goblin['x'] -= goblin['speed']
		elif (goblin['direction'] == "NE"):
			goblin['y'] -= goblin['speed']
			goblin['x'] += goblin['speed']
		elif (goblin['direction'] == "NW"):
			goblin['y'] -= goblin['speed']
			goblin['x'] -= goblin['speed']
		elif (goblin['direction'] == "SE"):
			goblin['y'] += goblin['speed']
			goblin['x'] += goblin['speed']
		elif (goblin['direction'] == "SW"):
			goblin['y'] += goblin['speed']
			goblin['x'] -= goblin['speed']


	if (tick % 20 == 0):
		new_dir_index = randint(0, len(directions) - 1)
		goblin['direction'] = directions[new_dir_index]

	if (goblin ['x'] > screen['width']):
		goblin['x'] = 0
	elif (goblin ['x'] < 0):
		goblin['x'] = 0
	elif (goblin ['y'] > screen['height']):
		goblin ['y'] = 0
	elif goblin ['y'] < 0:
		goblin ['y'] = 0

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
		
		if (not game_paused):
			hero['wins'] += 1
			# goblin['speed'] += 5
			win_sound.play()

	distance_between = fabs(hero['x'] - monster['x']) + (hero['y'] - monster['y'])

	if (distance_between < 32):
		print ("The monster killed the Hero!")
		rand_x = randint(0, screen['width'])
		rand_y = randint(0, screen['height'])
		monster['x'] = rand_x
		monster['y'] = rand_y


	distance_between = fabs(hero['x'] - 100) + (hero['y'] - 200)

	if (distance_between < 32):
		print ("Power Up!")
		powerup['tick_gotten'] += 1
		







	# RENDER:
	# blit takes two arguments
	# 1. What?
	# 2. Where?
	#draw background
	pygame_screen.blit(background_image, [0,0]) 

	# Draw the hero wins on the screen
	font = pygame.font.Font(None, 25)
	wins_text = font.render("Wins %d" % (hero['wins']), True, (0, 0, 0))
	pygame_screen.blit(wins_text, [15,15])

	# Draw the hero powers up on screen when he gets the Turkey
	font = pygame.font.Font(None, 25)
	powers_text = font.render("Power - Ups %d" % (powerup['tick_gotten']), True, (0, 0, 0))
	pygame_screen.blit(powers_text, [315, 25])


	if (tick % 30 == 0):
		timer += 1
	timer_text = font.render("Seconds Alive: %d" % (timer), True, (0,0,0))
	pygame_screen.blit(timer_text, [15,35])

	if(game_paused):
		timer_text = font.render("Game Paused. Hit space to unpause", True, (0,0,0))
		pygame_screen.blit(timer_text, [200,300])


	#draw hero
	draw_hero = pygame_screen.blit(hero_image, [hero['x'], hero['y']])
	draw_goblin = pygame_screen.blit(goblin_image, [goblin['x'], goblin['y']])
	draw_monster = pygame_screen.blit(monster_image, [monster['x'], monster['y']])
	draw_chicken = pygame_screen.blit(chicken_image, [100, 200])

	pygame.display.flip()
	# Flip the screen and start over