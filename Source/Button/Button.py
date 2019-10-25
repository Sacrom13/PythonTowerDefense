############################
#### Required Libraries ####
############################

# System libs
import pygame

# Button config
from Source.Button.ButtonConfig import *

########################
#### File Structure ####
########################

# 1 - Button
# 	1.1 - Init

######################
#### 1.1 - Button ####
######################
class Button():

    ####################
    #### 1.1 - Init ####
    ####################
    def __init__(self, X, Y, Image, ImageWidth, ImageHeight):

        # Button position on screen
        self.X = X
        self.Y = Y

        # Button image
        self.Image = None

        # Button Dimensions
        self.ImageWidth = ImageWidth
        self.ImageHeight = ImageHeight


    ####################
    #### 1.2 - Draw ####
    ####################
    def Draw(self, Window):

        # Draw button on screen
        Window.blit(self.Image, (self.ImageWidth, self.ImageHeight))

    
    #####################
    #### 1.2 - Click ####
    #####################
    def Click(self, X, Y):
        """
        Checks if button is clicked
        
        Arguments:
            X {Integer} -- X position of click
            Y {Integer} -- Y position of click
        
        Returns:
            [Boolean] -- True if clicked, false otherwise
        """

        # Check if position is within image bounds
        if X >= self.X and X <= self.X + self.ImageWidth:
            if Y >= self.Y and Y <= self.Y + self.ImageHeight:
                self.Selected = True
                return True
        return False

