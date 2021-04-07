import sys
import pygame

def check_keydown_events(event, rocket):
    if event.key == pygame.K_d:
        rocket.moving_right = True

    elif event.key == pygame.K_s:
        rocket.moving_down = True

    elif event.key == pygame.K_w:
        rocket.moving_up = True
    elif event.key == pygame.K_a:
        rocket.moving_left = True

def check_keyup_events(event, rocket):
    if event.key == pygame.K_d:
        rocket.moving_right = False
    elif event.key == pygame.K_s:
        rocket.moving_down = False
    elif event.key == pygame.K_w:
        rocket.moving_up = False
    elif event.key == pygame.K_a:
        rocket.moving_left = False

def check_events(rocket):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, rocket)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, rocket)

def update_screen(settings, screen, rocket):
    screen.fill(settings.bg_color)
    rocket.blitme()
    pygame.display.flip()

