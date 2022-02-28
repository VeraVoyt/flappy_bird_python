# imports well-known libraries
import pygame as pg

# imports from project files
from additional.constants import (GROUND_IMAGE, GROUND_Y_COORD, PIPE_IMAGE,
                                  PIPE_STARTING_POSITION_X, PIPE_VELOCITY,
                                  DELTA_T)


class Ground(pg.sprite.Sprite):

    def __init__(self):
        """Ground on the bottom of the screen"""
        super().__init__()
        self.image = pg.image.load(GROUND_IMAGE).convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, GROUND_Y_COORD)


class Pipe(pg.sprite.Sprite):

    def __init__(self, upside_down, y_coord):
        """Pipes that move to the bird"""
        super().__init__()
        self.image = pg.image.load(PIPE_IMAGE).convert()
        self.rect = self.image.get_rect()
        self.rect.x = PIPE_STARTING_POSITION_X
        if upside_down:
            self.image = pg.transform.flip(self.image, False, True)
            self.rect.bottom = y_coord
        else:
            self.rect.top = y_coord

    def move(self):
        """Moves the pipe"""
        self.rect.right -= PIPE_VELOCITY * DELTA_T

