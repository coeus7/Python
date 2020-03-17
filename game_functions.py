import pygame
import sys

def check_keydown_events(event,ship):
	if event.key == pygame.K_RIGHT:
		ship.move_right = True
	elif event.key == pygame.K_LEFT:
		ship.move_left  = True

def check_keyup_events(event,ship):
	ship.move_right = False
	ship.move_left  = False

def check_events(ship):
	"""Monitor the user action"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event,ship)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event,ship)

def update_screen(settings, screen,ship):
	#Fill backgroud color
	#screen.fill(ai_setting.bg_color)
	screen.blit(settings.bg,(0,0))
	ship.blitme()
	#Flush the screen surface
	pygame.display.flip()
