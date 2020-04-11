"""This is the guardian settings"""

# -*- coding: utf-8 -*-

# +++++++++IMPORT++++++++++

# Standard libraries


# Third party
import pygame

# Local applications
from ..settings import config as c, maze
# +++++++++++++++++++++++++


class Items(pygame.sprite.Sprite):
    """Generates randomly placed items for
    the player to catch.
    Parameters
    ----------
    images: pygame
        load and propely scale the items
    rect: tuple
        return the items coordinates in pixels"""

    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)

        for key, name in maze.item.items():
            self.images = pygame.transform.scale(
                pygame.image.load(c.ITEMS.format(name)), c.SPR)
            self.rect = self.images.get_rect()
            self.rect.x = key[0] * c.SPR_X
            self.rect.y = key[1] * c.SPR_Y
            # Take the display's screen to blit the items.
            screen.blit(self.images, self.rect)
