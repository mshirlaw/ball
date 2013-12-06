#!/usr/bin/python
import pygame

class BallSprite(pygame.sprite.Sprite):
	"""A class to represent a ball sprite on the screen"""
	# Ball attributes
	x_speed = 0
	y_speed = 0
	
	# Constructor
	def __init__(self, c, s):
		pygame.sprite.Sprite.__init__(self)
		self.color=c
		self.size=s
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