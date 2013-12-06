#!/usr/bin/python
import pygame
from ball import Ball

#initialise pygame
pygame.init()

# width and height to create tuple for screen size 
width=640
height=480
size = (width,height)

# background color
white=(255,255,255)

# initialise a window
window = pygame.display.set_mode( size )
pygame.display.set_caption( 'Moving Ball' )

# create the player
player = Ball()
player.size=10
player.x = width/2
player.y = height/2

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
			player.x = pos[0]
			player.y = pos[1]
	
	# move the ball
	player.move_ball()
   	print "(%d,%d)" % (player.x,player.y)
    	
   	# clear screen
   	window.fill(white)
	
	player.draw_ball(window)
	
   	pygame.display.flip()
    	
   	clock.tick(60)
    	
pygame.quit()
