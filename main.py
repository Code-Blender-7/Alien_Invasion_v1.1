import sys
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
from pygame.sprite import Group
import game_functions as gf
from button import Button
from game_stats import GameStats


def run_game():
        pygame.init()
        ai_settings = Settings()
        bullets = Group()
        aliens = Group()


        screen = pygame.display.set_mode(
                (ai_settings.screen_width,ai_settings.screen_breadth))
        pygame.display.set_caption("Alien Invasion v1.1")
        ship = Ship(ai_settings,screen)

        gf.create_fleet(ai_settings , screen , ship ,aliens)

        stats = GameStats(ai_settings)
        
        play_button = Button(ai_settings, screen, "Play?")

	
        while True:
                gf.check_events(ai_settings , screen , stats , play_button ,  ship , aliens ,  bullets)

                if stats.game_active:
                        ship.update()
                        gf.update_bullets(ai_settings , screen , ship , aliens, bullets)
                        gf.update_aliens(ai_settings , stats , screen , ship , aliens, bullets)
                gf.update_screen(ai_settings, screen, stats ,  ship, aliens, bullets , play_button)


run_game()
