#!/usr/bin/python
import pygame

# Function to draw box
def draw_ball(window,x,y):
	black=(0,0,0)
	pygame.draw.ellipse(window,black,[x,y,30,30],0)

#initialise pygame
pygame.init()

# width and height to create tuple for screen size 
width=640
height=480
size = (width,height)

# background color
white=(255,255,255)

# x and y velocity
x_speed = 0
y_speed = 0
	
# initial position
x_coord = width/2 - 15
y_coord = height/2 - 15

# initialise a window
window = pygame.display.set_mode( size )
pygame.display.set_caption( 'Moving Ball' )

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
				x_speed=-3
			elif event.key == pygame.K_RIGHT:
				x_speed=3
			elif event.key == pygame.K_UP:
				y_speed=-3
			elif event.key == pygame.K_DOWN:
				y_speed=3
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				x_speed=0
			elif event.key == pygame.K_RIGHT:
				x_speed=0
			elif event.key == pygame.K_UP:
				y_speed=0
			elif event.key == pygame.K_DOWN:
				y_speed=0
		
	# update x position
	if (x_coord + x_speed) < 0:
		x_coord=0
	elif (x_coord + x_speed) > width-30:
		x_coord=width-30
	else:
		x_coord = x_coord + x_speed

	#update y position
	if (y_coord + y_speed) < 0:
		y_coord=0
	elif (y_coord + y_speed) > height-30:
		y_coord=height-30
	else:
		y_coord = y_coord + y_speed
   	
   	print "(%d,%d)" % (x_coord,y_coord)
    	
   	# clear screen
   	window.fill(white)
    	
   	# draw player
   	draw_ball(window,x_coord,y_coord)
    	
   	pygame.display.flip()
    	
   	clock.tick(60)
    	
pygame.quit()
