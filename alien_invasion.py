import pygame

#import self-definition module
import game_functions as gf
from ship     import Ship
from settings import Settings

def run_game():
	#Init game and creat a screen mode
	pygame.init()

	#Creat screen surface
	settings = Settings()
	screen = pygame.display.set_mode(settings.screen_size)
	pygame.display.set_caption("Hello, My little Cheng")
	
	#creat ship surface
	ship = Ship(screen,settings)

	while True:
		gf.check_events(ship)
		ship.update()
		gf.update_screen(settings, screen, ship)
		
run_game()
