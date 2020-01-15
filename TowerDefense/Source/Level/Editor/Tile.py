############################
#### Required Libraries ####
############################

# System libs
import pygame
import os

# Tile Config
from Source.Config.TileConfig import *

########################
#### File Structure ####
########################

# 1 - Tile
# 	1.1 - Init
#   1.2 - Draw
#   1.3 - Clicked

class Tile():

    ####################
	#### 1.1 - Init ####
	####################
    def __init__(self, Window, Position, Name):
        """
        Initiates a tile of Name 'Name'
        on position X, Y on screen
        
        Arguments:
            Position {Integer Tuple} -- Coordinates of the tile's top left corner 
            Name {String} -- Name of tile
        """

        # Default Configs
        self.DefaultConfigs = TileConfigs['Default']

        # Tile Dimensions
        self.TileDimensions = self.DefaultConfigs['ImageDimensions']

        # Tile Configs
        self.Configs = TileConfigs[Name]

        # Window to draw on
        self.Window = Window

        # Position of Tile on screen
        self.Position = Position

        # Get Image
        self.Image = self.Configs['Image']

        self.Name = Name


    ####################
    #### 1.2 - Draw ####
    ####################
    def Draw(self):
        """
        Draws Tile on screen
        """
        # Draw Tile
        self.Window.blit(self.Image, self.Position)
        

    #######################
    #### 1.3 - Clicked ####
    #######################
    def Clicked(self, MousePos):
        """
        Check if Tile was clicked
        """

        # Check if click is within image bounds
        if MousePos[0] > self.Position[0] and MousePos[0] < self.Position[0] + self.TileDimensions[0]:
            if MousePos[1] > self.Position[1] and MousePos[1] < self.Position[1] + self.TileDimensions[1]:
                return True

        return False
        

