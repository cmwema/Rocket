from settings import Settings
from rocket import Rocket
import functions
import pygame
import sys


def main():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("ROCKET")

    #make rocket
    rocket = Rocket(settings=settings, screen=screen)

    while True:
        functions.check_events(rocket=rocket)

        rocket.update()

        functions.update_screen(settings=settings, screen=screen, rocket=rocket)

main()