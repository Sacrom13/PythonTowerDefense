############################
#### Required Libraries ####
############################

# System libs
import pygame

# Button default definitions
from Source.Config.ButtonConfig import *

########################
#### File Structure ####
########################

# 1 - Button
# 	1.1 - Init
#   1.2 - Draw
#   1.3 - Click

####################
#### 1 - Button ####
####################
class Button():

    ####################
    #### 1.1 - Init ####
    ####################
    def __init__(self, Position, Image, ImageDimensions):
        """
        Initializes a Button
        
        Arguments:
            X {Integer Tuple} -- Position of button in form (x, y)
            Image {Pygame Image} -- Button image
            ImageDimensions {Integer Tuple} -- Image dimensions in form (Width, Height)
        """

        # Button position on screen
        self.Position = Position

        # Button image
        self.Image = None

        # Button dimensions
        self.ImageDimensions = ImageDimensions


    ####################
    #### 1.2 - Draw ####
    ####################
    def Draw(self, Window):
        """
        Draws a button
        
        Arguments:
            Window {Pygame Surface} -- Window to draw on
        """

        # Draw button on screen
        Window.blit(self.Image, self.ImageDimensions)

    
    #####################
    #### 1.3 - Click ####
    #####################
    def Click(self, Position):
        """
        Checks if a button was clicked
        
        Arguments:
            Position {Integer Tuple} -- Position of click in form (x, y)
        
        Returns:
            [Boolean] -- True if clicked, false otherwise
        """

        # Check if position is within image bounds
        if Position[0] >= self.Position[0] and Position[0] <= self.Position[0] + self.ImageDimensions[0]:
            if Position[1] >= self.Position[1] and Position[1] <= self.Position[1] + self.ImageDimensions[1]:
                return True
        return False