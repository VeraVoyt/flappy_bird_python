# imports well-known libraries
import pygame as pg
import random
import sys

# imports from project files
from additional.constants import (BACKGROUND_IMAGE, SCREEN_WIDTH,
                                  PIPES_DISTANCE, PIPE_GAP_CENTER_MIN,
                                  PIPE_GAP_CENTER_MAX, PIPE_HALF_GAP)
from lib.obstacles import Ground, Pipe
from lib.bird import Bird


class Controller:

    def __init__(self):
        """Main controlling object"""
        self.background = pg.image.load(BACKGROUND_IMAGE).convert()
        self.ground = Ground()
        self.bird = Bird()
        self.pipes = []

    # updates the situation
    def update(self, pressed_keys):
        """Moves all objects"""
        # check flapping
        if pg.K_UP in pressed_keys:
            flapped = True
        else:
            flapped = False

        # move the bird
        self.bird.move(flapped)

        # add new pipes if needed
        if len(self.pipes) == 0 or self.pipes[-1].rect.right < SCREEN_WIDTH - PIPES_DISTANCE:
            gap_center_y = random.randint(PIPE_GAP_CENTER_MIN, PIPE_GAP_CENTER_MAX)
            upper_pipe = Pipe(True, gap_center_y - PIPE_HALF_GAP)
            lower_pipe = Pipe(False, gap_center_y + PIPE_HALF_GAP)
            self.pipes.append(upper_pipe)
            self.pipes.append(lower_pipe)

        # move the pipes
        for pipe in self.pipes:
            pipe.move()

        # check collision
        obstacles = pg.sprite.Group(self.pipes + [self.ground])
        if pg.sprite.spritecollide(self.bird, obstacles, False):
            pg.quit()
            sys.exit()



    def draw(self, surface):
        """Draws everything on the screen"""
        # draw background
        surface.blit(self.background, (0,0))

        # draw pipes
        for pipe in self.pipes:
            surface.blit(pipe.image, pipe.rect)

        # draw ground
            surface.blit(self.ground.image, self.ground.rect)

        # draw bird
        surface.blit(self.bird.image, self.bird.rect)


