# -*- coding: utf-8 -*-

# +++++++++IMPORT++++++++++

# Standard libraries


# Third party
import pygame

# Local applications
from ..settings import config as c, maze
# +++++++++++++++++++++++++


class Items(pygame.sprite.Sprite):
    # TODO:
    # The loop doesn't generate the 3 images
    # in the maze. Only the last loop apprear.
    # Find a way to extract the # items.
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        for key, name in maze.item.items():

            self.images = pygame.transform.scale(
                pygame.image.load(c.ITEMS.format(name)), c.SPR)
            self.all = self.images.get_rect()
            self.all.x = key[0] * c.SPR_X
            self.all.y = key[1] * c.SPR_Y
