#!/usr/bin/python
import pygame

class Ball():
	"""A class to represent a ball on the screen"""
	# Ball attributes
	color = (0,0,0)
	x = 0
	y = 0
	x_speed = 0
	y_speed = 0
	size = 10
	
	# Draw method
	def draw_ball(self,window):
		pygame.draw.circle(window,self.color,[self.x,self.y],self.size)
	
	# Move method
	def move_ball(self):
		self.x = self.x + self.x_speed
		self.y = self.y + self.y_speed
		
	