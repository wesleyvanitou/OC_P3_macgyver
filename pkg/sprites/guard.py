"""This is the guardian settings"""

# -*- coding: utf-8 -*-

# +++++++++IMPORT++++++++++

# Standard libraries


# Third party
import pygame

# Local applications
from ..settings import config as c, maze
# +++++++++++++++++++++++++


class Guard(pygame.sprite.Sprite):
    """ This class defines the visual
    carastetictics of the guardian

    Parameters
    ----------
    img : pygame
        resize and scale the image
    rect : pygame module
        position of the guardian
    """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.transform.scale(
            pygame.image.load(c.GUARD), c.SPR)
        x, y = maze.guard
        self.rect = self.img.get_rect()
        self.rect.x = x * c.SPR_X
        self.rect.y = y * c.SPR_Y
