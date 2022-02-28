# imports well-known libraries
import pygame as pg

# imports from project files
from additional.constants import (BIRD_IMAGE, BIRD_STARTING_POSITION, DELTA_T,
                                  G, GROUND_Y_COORD, BIRD_FLAP_SPEED)


class Bird(pg.sprite.Sprite):

    def __init__(self):
        """Bird, that flies between the pipes"""
        super().__init__()
        self.image = pg.image.load(BIRD_IMAGE).convert()
        self.rect = self.image.get_rect()
        self.rect.center = BIRD_STARTING_POSITION
        self.velocity = 0

    def move(self, flapped):
        """Moves along the y axis"""
        if self.rect.bottom < GROUND_Y_COORD * 1.01:
            self.rect.y += self.velocity * DELTA_T
            self.velocity += G * DELTA_T
            if flapped:
                self.velocity = - BIRD_FLAP_SPEED

        if self.rect.bottom >= GROUND_Y_COORD * 1.01:
            self.rect.bottom = GROUND_Y_COORD * 1.01
            self.velocity = 0

