############################
#### Required Libraries ####
############################

# System libs
import pygame
import os

# Tile Config
from Source.Config.TileConfig *

########################
#### File Structure ####
########################

# 1 - Tile
# 	1.1 - Init
#   1.2 - Draw

class Tile():

    ####################
	#### 1.1 - Init ####
	####################
    def init(self, Window, X, Y, Name):
        """
        Initiates a tile of Name 'Name'
        on position X, Y on screen
        
        Arguments:
            X {Integer} -- Top Left Corner position of tile on screen
            Y {Integer} -- Top Left Corner position of tile on screen
            Name {String} -- Name of tile
        """

        # Tile Configs
        self.Configs = TileConfigs[Name]

        # Window to draw on
        self.Window = Window

        # Position of Tile on screen
        self.X = X
        self.Y = Y

        # Get Image
        self.Image = Configs['Image']

    ####################
    #### 1.2 - Draw ####
    ####################
    def Draw(self):
        """
        Draws Tile on screen
        """

        # Draw Tile
        self.Window.blit(3)

