#########################################################################
#																		#
#					Moving Balls ~ mshirlaw								#
#																		#
#########################################################################

#!/usr/bin/python
import pygame, random

class BallSprite(pygame.sprite.Sprite):
	"""A class to represent a ball sprite on the screen"""
	# Ball attributes
	x_speed = 0
	y_speed = 0
	update_speed=0
	min_speed=0
	yd=0
	lives = 0
	score=0

	# Constructor
	def __init__(self, c, s):
		pygame.sprite.Sprite.__init__(self)
		self.color=c
		self.size=s
		self.score=0
		self.lives=5
		self.update_speed=2
		self.min_speed=2
		self.yd=1
		self.image = pygame.Surface([self.size,self.size])
		self.image.fill((255,255,255))
		self.image.set_colorkey((255,255,255))
		pygame.draw.circle(self.image,self.color,(self.size/2,self.size/2),self.size/2,0)
		self.rect=self.image.get_rect()
		
	# Move method
	def move(self):
		# get coords of screen 
		s=pygame.display.get_surface()
		w_width=pygame.Surface.get_width(s)
		w_height=pygame.Surface.get_height(s)
		# update xcoord 
		if self.rect.x + self.x_speed >= 0 and self.rect.x + self.size + self.x_speed <= w_width:
			self.rect.x = self.rect.x + self.x_speed
		# update ycoord
		if self.rect.y + self.y_speed >= 0 and self.rect.y + self.size + self.y_speed <= w_height:
			self.rect.y = self.rect.y + self.y_speed
	
	# To allow the sprites to move down the screen
	def update(self):
		s=pygame.display.get_surface()
		w_width=pygame.Surface.get_width(s)
		w_height=pygame.Surface.get_height(s)
		self.rect.y += self.update_speed*self.yd
		if self.rect.y > w_height:
			self.rect.y=-w_height/10
			self.rect.x=random.randrange(0,width)
			self.update_speed = random.randint(self.min_speed,6)
		elif self.rect.y < 0-w_height/10:
			self.rect.y=w_height
			self.rect.x=random.randrange(0,width)
			self.update_speed = random.randint(self.min_speed,6)

	# flip vertical direction and increase min speed
	def change(self,ydir):
		self.yd=ydir
		if self.min_speed<5:
			self.min_speed+=1

class TitleSprite(pygame.sprite.Sprite):
	"""A class to represent text on the screen"""
	w=0
	h=0
	main=True
	def __init__(self, w_width, w_height, flag):
		pygame.sprite.Sprite.__init__(self)
		self.w=w_width
		self.h=w_height
		self.main=flag
		self.font = pygame.font.Font(None, 50)
		self.text = "Moving Balls"
		self.renderTitle()

	def renderTitle(self):
		self.image = self.font.render( self.text, 1, (255,255,255))
		self.rect  = self.image.get_rect()
		if self.main:
			self.rect.move_ip( (5,self.h-self.image.get_height()))
		else:
			self.font = pygame.font.Font(None, 30)
			self.rect.move_ip( (self.w-5-self.image.get_width(),self.h-self.image.get_height()))

	def update(self,new_title):
		self.text=new_title
		self.renderTitle()


#initialise pygame
pygame.init()

# colors
red = (255,0,0)
black= (0,0,0)
white=(255,255,255)
green = (0,255,0)
PLAYER_SPEED=4

# width and height to create tuple for screen size 
width=640
height=480
size = (width,height)

# initialise a window
window = pygame.display.set_mode( size )
pygame.display.set_caption( "Moving Balls" )

# all sprites in game
all_sprites_list = pygame.sprite.Group()

# all enemies in game
enemy_list = pygame.sprite.Group()

# all titles in game
title_list = pygame.sprite.Group()

# create ball sprites
for i in range(50):
	# This represents a sprite
	sp = BallSprite(green, 20)
	# Set a random location for the sprite
	sp.rect.x = random.randrange(0,width)
	sp.rect.y = random.randrange(0,height-height/5) 
	# Add the block to the list of objects
	all_sprites_list.add(sp)
	enemy_list.add(sp)

# create the player
player = BallSprite(red, 20)
player.rect.x = width/2
player.rect.y = height - height/10
all_sprites_list.add(player)	

# create a title
title = TitleSprite(width,height,True)
title_list.add(title)	
scoreSprite = TitleSprite(width,height,False)
title_list.add(scoreSprite)	

		
# get rid of mouse cursor
pygame.mouse.set_visible(False)

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# game loop, wait for user to click exit
game_over=False
while game_over==False:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_over = True
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				player.x_speed=-PLAYER_SPEED
			elif event.key == pygame.K_RIGHT:
				player.x_speed=PLAYER_SPEED
			elif event.key == pygame.K_UP:
				player.y_speed=-PLAYER_SPEED
			elif event.key == pygame.K_DOWN:
				player.y_speed=PLAYER_SPEED
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				player.x_speed=0*PLAYER_SPEED
			elif event.key == pygame.K_RIGHT:
				player.x_speed=0*PLAYER_SPEED
			elif event.key == pygame.K_UP:
				player.y_speed=0*PLAYER_SPEED
			elif event.key == pygame.K_DOWN:
				player.y_speed=0*PLAYER_SPEED
	
	# move the player
	player.move()
   	#print "(%d,%d)" % (player.rect.x,player.rect.y)
    
    # See if the player has collided with anything
	enemy_hit_list = pygame.sprite.spritecollide(player,enemy_list,True)  
   	
   	# Remove the enemy and decrement lives
   	for enemy in enemy_hit_list:
   		player.lives=player.lives-1
   		print "Hit an enemy! You have %d lives left!" % player.lives
   		if player.lives == 0:
   			print "You died, game over!"
   			game_over=True
   	
   	# clear screen
   	window.fill(black)

	#move enemies down screen 
	enemy_list.update()
	
	# draw all shapes
	all_sprites_list.draw(window)	
	title_list.draw(window)
	
	# update score
	player.score=player.score+1
	scoreSprite.update("Score: "+str(player.score))

	# flip vertical direction
	if player.score==500:
		for enemy in enemy_list:
			enemy.change(-1)
	elif player.score==1000:
		for enemy in enemy_list:
			enemy.change(1)
	elif player.score==1500:
		for enemy in enemy_list:
			enemy.change(-1)
	elif player.score==2000:
		for enemy in enemy_list:
			enemy.change(1)

   	pygame.display.flip()
    	
   	clock.tick(60)
    	
pygame.quit()
