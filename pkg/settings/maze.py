# -*- coding: utf-8 -*-

""" Maze generator

Maze.py generates all the crucial elements of the maze.

It randomly picks the a text file in maze folder and
generates all the necessary coordinates for the elements
of the game.

All the configurations are manage by the config.py file.
"""


# +++++++++IMPORT++++++++++

# Standard libraries
import os
from random import sample

# Third party
# Local applications
from ..settings import config as c
# +++++++++++++++++++++++++


class Maze:
    """
    This class will generates the all the parameters
    needed for the game.

    Methods
    ------
    load()
        return all the parameters needed for the game.
        the text file is automatically load via the
        config.py file.

    _item()
        generates a dictionnary {name, coordinates}
        of all the items.

    surface(a, b)
        return a the surface of the game in pixel.
        a, b are index compensator to get the right
        dimension.

    """

    def __init__(self):
        """
        Parameters
        ---------
        path : list
            all the path tuples
        wall : list
            all the wall tuples
        item : dict
            key, value of the itemsa
        size : tuple
            the length, width of the maze. +1 is needed
            for the correct lenght.
        srf : tuple
           game surface in pixel. a, b adjust to
           the correct legnth.
        hero : tuple
            hero  coordinates
        guard : tuple
            guardian coordinates
        """
        self.path = []
        self.wall = []
        self.item = {}

        self.size = None
        self.srf = None
        self.hero = None
        self.guard = None

        self._load()
        self._items()

    def _load(self):
        """
        Generates all the coordinates needed for the game

        Paraneters
        ----------
        path : list
            all the path tuples
        wall : list
            all the wall tuples
        path : list
            all the path tuples
        wall : list
            all the wall tuples
        """
        with open(c.MAZE) as labyrinth:
            for y, row in enumerate(labyrinth):
                for x, col in enumerate(row.strip()):
                    self.size = (x, y)
                    if col in ".PG":
                        self.path.append(self.size)
                        if col in "P":
                            self.hero = self.size
                        if col in "G":
                            self.guard = self.size
                    else:
                        self.wall.append(self.size)

    def _items(self):
        """ This function will select 3 coordinates for the
        items exlcuding the player and guardian one.

        Parameters
        ----------
        location :
            list comprehesion that picks 3 randoms
            coordinates from the maze's path excluding
            the player and guardian one.

        item: dict
            stores all 'name: coord' of the items.
        """
        # Scan the item directory and pick the images name
        with os.scandir(c.ITEMSDIR) as items:
            itemlist = []
            for item in items:
                item = os.path.splitext(item.name)[0]
                itemlist.append(item)

        location = sample([
            i for i in self.path
            if i not in [self.hero, self.guard]], k=c.NB_ITEMS)

        for key, value in zip(itemlist, location):
            self.item[value] = key

    def surface(self, a, b):
        """
            Calculate the surface or the screen of the maze.
            a, b factor compensate the 0 index.

            Parameters
            ----------
            srf: tuple
                generate the surface of the windows and/or
                background. a, b are '[0]' adjustment.
        """

        self.srf = (
            (self.size[0] + a) * c.SPR_X,
            (self.size[1] + b) * c.SPR_Y)
        return self.srf
