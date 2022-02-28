# imports well-known libraries
import pygame as pg
import sys

# imports from project files
from lib.controller import Controller
from additional.constants import SCREEN_SIZE, FPS


def check_events():
    """Checks whether it's time to exit"""
    pressed = []
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            pressed.append(event.key)
    return pressed

# initialize library pygame
pg.init()

# make the game screen
screen = pg.display.set_mode(SCREEN_SIZE)

# fps controller
fps_checker = pg.time.Clock()

# create game controller
game_controller = Controller()

while True:
    pressed_keys = check_events()
    game_controller.update(pressed_keys)
    game_controller.draw(screen)
    pg.display.update()
    fps_checker.tick(FPS)
