# -*- coding: utf-8 -*-
"""
This is the core of the game. The ui.py regroups all the
elements needed for the game to work.

"""


# +++++++++IMPORT++++++++++

# A. Standard libraries
import time
# B. Third party
import pygame

# C. Local applications
# c.i Settings
from pkg.settings import config as c, maze

# c.c Characters
from pkg.sprites.guard import Guard
from pkg.sprites.hero import Hero, HeroSpr
from pkg.sprites.items import Items
# +++++++++++++++++++++++++


class Display:
    """
        Setup of the game's display.

        Here we'll initialize the maze to recuperates all the
        elements necessary to building it.

        The '__init__(self)' will generates the maze structure
        and background design.

        Methods
        -------

        game: pygame
            The 'game' method creates the visual environement to
            display the game. Not that all the parameters are
            constants located in 'config.py' file.
    """

    def __init__(self):
        """
            Parameters
            ----------

            hero: class
                Initialize the characteristics of the hero
            guard: class
                Initialize the characteristics of the Guardian
            screen: display
                Generate the game's window
            bg: pygame display
                Generate the surface where all the elements
                will be display
            # maze generator: loop
                Generator paths and walls
        """

        self.guard = Guard()
        self.hero = Hero()

        pygame.init()
        pygame.display.set_caption("Mac Guyver: The ecsape")

        self.screen =\
            pygame.display.set_mode(maze.surface(1, 1))

        self.bg =\
            pygame.Surface(maze.surface(1, 1))

        # Generate the background

        # TODO: D. After the exam look for better
        # background image implementation.
        for coord in maze.path:
            self.bg.blit(
                c.TILES,
                (coord[0] * c.SPR_X,
                 coord[1] * c.SPR_Y), c.tiles(17, 11))

        for coord in maze.wall:
            self.bg.blit(
                c.TILES,
                (coord[0] * c.SPR_X,
                 coord[1] * c.SPR_Y), c.tiles(13, 3))

    def game(self):
        """ Core of the game.
           GAME
           ----
           This is where the game will be displayed.

               Items generator
               ---------------
               The items will be generated trhough a zip loop
               with each value of the maze.item keys and a
               random list of items.

               core
               ----
               The for loop goes trhough the the event.key
               inside the hero's' controller to test the
               direction and output the result.
        """

        # GAME
        # ----
        running = True
        while running:
            herospr = HeroSpr(maze.hero)
            self.screen.blit(self.bg, (0, 0))
            self.screen.blit(self.guard.img, self.guard.rect)
            self.screen.blit(herospr.img, herospr.rect)

            # Items generator
            Items(self.screen)

            # core
            # ----
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    print("Quit the game")
                elif event.type == pygame.KEYDOWN:
                    maze.hero = self.hero.move(
                        self.hero.controller(event.key, maze.hero))
                    if maze.hero == maze.guard:
                        if len(self.hero.grabbed) == c.NB_ITEMS:
                            self.screen.blit(c.WIN, (0, 0))
                            running = False
                        elif len(self.hero.grabbed) != c.NB_ITEMS:
                            self.screen.blit(c.GAMEOVER, (0, 0))
                            running = False
            pygame.display.update()
        time.sleep(1)
        pygame.quit()
