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
		# get coords of screen 
		s=pygame.display.get_surface()
		w_width=pygame.Surface.get_width(s)
		w_height=pygame.Surface.get_height(s)
		# update xcoord 
		if self.x -self.size + self.x_speed >= 0 and self.x + self.size + self.x_speed <= w_width:
			self.x = self.x + self.x_speed
		# update ycoord
		if self.y -self.size + self.y_speed >= 0 and self.y + self.size + self.y_speed <= w_height:
			self.y = self.y + self.y_speed
		
	