#!/usr/bin/python
import pygame, random
from ball_sprite import BallSprite

#initialise pygame
pygame.init()

# colors
red = (255,0,0)
black= (0,0,0)
white=(255,255,255)

# width and height to create tuple for screen size 
width=640
height=480
size = (width,height)

# initialise a window
window = pygame.display.set_mode( size )
pygame.display.set_caption( 'Moving Ball' )

# all sprites in game
all_sprites_list = pygame.sprite.Group()

# create ball sprites
for i in range(10):
	# This represents a sprite
	sp = BallSprite(black, 20)
	# Set a random location for the sprite
	sp.rect.x = random.randrange(50,width-50)
	sp.rect.y = random.randrange(50,height-50) 
	# Add the block to the list of objects
	all_sprites_list.add(sp)	

# create the player
player = BallSprite(red, 20)
player.rect.x = width/2
player.rect.y = height/2
all_sprites_list.add(player)	

# get rid of mouse cursor
pygame.mouse.set_visible(False)

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# game loop, wait for user to click exit
done=False
while done==False:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				player.x_speed=-3
			elif event.key == pygame.K_RIGHT:
				player.x_speed=3
			elif event.key == pygame.K_UP:
				player.y_speed=-3
			elif event.key == pygame.K_DOWN:
				player.y_speed=3
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				player.x_speed=0
			elif event.key == pygame.K_RIGHT:
				player.x_speed=0
			elif event.key == pygame.K_UP:
				player.y_speed=0
			elif event.key == pygame.K_DOWN:
				player.y_speed=0
		elif event.type==pygame.MOUSEMOTION:
			pos = pygame.mouse.get_pos()
			player.rect.x = pos[0]
			player.rect.y = pos[1]
	
	# move the player
	player.move()
   	print "(%d,%d)" % (player.rect.x,player.rect.y)
    	
   	# clear screen
   	window.fill(white)
	
	# draw all shapes
	all_sprites_list.draw(window)
	
   	pygame.display.flip()
    	
   	clock.tick(60)
    	
pygame.quit()
