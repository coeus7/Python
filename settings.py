import pygame

class Settings():
	"""Save all the setting parameter"""
	def __init__(self):
		self.screen_size = (1280,720)
		self.bg_color = (230,230,230)
		self.bg = pygame.image.load("images/bg1.jpg")
		self.speed = 15