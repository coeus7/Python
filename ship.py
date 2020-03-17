import pygame

class Ship():
	"""Init the location of ship"""
	def __init__(self,screen,settings):
		self.screen = screen
		self.settings = settings

		#load ship picture and get its sharp
		self.image = pygame.image.load('images/ship.png')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		#set ship to center of screen
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		self.center = float(self.rect.centerx)

		#Indicate ship location
		self.move_left  = False
		self.move_right = False

	def blitme(self):
		"""blit ship"""
		self.screen.blit(self.image,self.rect)

	def update(self):
		if self.move_right and self.rect.right <= self.screen_rect.right:
			self.center += self.settings.speed
		elif self.move_left and self.rect.left >= self.screen_rect.left:
			self.center -= self.settings.speed

		self.rect.centerx = self.center