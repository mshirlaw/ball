#!/usr/bin/python
import pygame

class BallSprite(pygame.sprite.Sprite):
	"""A class to represent a ball sprite on the screen"""
	# Ball attributes
	color = (0,0,0)
	size = 20
	
	# Constructor
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([self.size,self.size])
		self.image.fill((255,255,255))
		self.image.set_colorkey((255,255,255))
		pygame.draw.circle(self.image,self.color,(self.size/2,self.size/2),self.size/2,0)
		self.rect=self.image.get_rect()
		
	