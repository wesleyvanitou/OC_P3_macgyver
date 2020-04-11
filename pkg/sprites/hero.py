# -*- coding: utf-8 -*-

"""
hero.py creates all the behavior of the player.
It requires the 'pygame' module for the 'controller'
to work.

Once the input is found, the result goes to the
'move' method to be analyze and return the
behavior of the hero (move or stay there). If
an item is found, it puts it into a list a the
top left of the screen.
"""

# +++++++++IMPORT++++++++++

# Standard libraries
# Third party
import pygame
# Local applications
from ..settings import config as c, maze

# +++++++++++++++++++++++++


class Hero():
    """Contains the hero's behavior for the game

    Methods
    -------
    controller(key, hero)
        returns the new coordinates of the player
        and take the event.key and the last hero
        coordinates
    move(hero)
        intiates the mouvement of the hero (maze.hero)
        and the storage of the items.

    """

    def __init__(self):
        """
        Parameters
        ----------
        grab : list
            stores the items when catches by the player
        stuck : tuple
            it stores the last player mouvement and
            prevent it to go to the wall by assiging
            player to its value
        """
        self.grabbed = []
        self.stuck = maze.hero

    def controller(self, key, hero):
        """ The controller checks if the 'event.key'
        is in the ←, ↓, ↑, →  keys and output the new
        coordinates.

        Parameters
        ----------
        stuck : tuple
            stores the last player's move. Use to stick
            to the path.
        """
        x, y = hero
        self.stuck = hero
        if key == pygame.K_LEFT:
            hero = (x - 1, y)
        elif key == pygame.K_DOWN:
            hero = (x, y + 1)
        elif key == pygame.K_UP:
            hero = (x, y - 1)
        elif key == pygame.K_RIGHT:
            hero = (x + 1, y)
        return hero

    def move(self, hero):
        """Move the hero in the maze.

        Parameters
        ----------
        maze.path :
            path of the game
        maze.hero :
            last hero coordinates
        maze.item :
        """
        if hero in maze.path:
            maze.hero = hero
            if maze.hero in maze.item:
                grab = maze.item.pop(hero)
                self.grabbed.append(grab)
                maze.item[len(self.grabbed) - 1, 0] = grab
        elif hero in maze.wall:
            maze.hero = self.stuck

        return maze.hero


class HeroSpr(pygame.sprite.Sprite):
    """Display of the hero in the game.

    Attributes
    ----------
    hero : tuple
        coordinates uses to display the hero
    """

    def __init__(self, hero):
        """Setup the hero's display

        Parameters
        ----------
        hero : tuple
            take the last hero's parameters from the loops
        img : pygame image
        """
        self.hero = hero
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.transform.scale(
            pygame.image.load(c.HERO), c.ITEM_SIZE)

        x, y = self.hero[0] * c.SPR_X, self.hero[1] * c.SPR_Y
        self.rect = self.img.get_rect().move(x, y)

# TODO: Perfect the gane with sprites and update class
