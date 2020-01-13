############################
#### Required Libraries ####
############################

# System libs
import pygame
import os

# Editor Config
from Source.Config.EditorConfig import *

########################
#### File Structure ####
########################

# 1 - Editor
# 	1.1 - Init
#   1.2 - Run
#   1.3 - Update
#   1.4 - Draw
#   1.4.1 - DrawBackground
#   1.4.2 - DrawSideground

class Editor():

    ####################
	#### 1.1 - Init ####
	####################
    def __init__(self, ScreenDimensions, Window, FrameRate, Font):

        # Screen Resolution
        self.ScreenDimensions = ScreenDimensions

        # Window
        self.Window = Window

        # Tiles
        self.Background = []
        
        # FrameRate
        self.FrameRate = FrameRate

        # Font to write text with
        self.Font = Font

        # Tile Dimensions
        self.TileDimensions = EditorConfigs['TileDimensions']
        

    ###################
	#### 1.2 - Run ####
	###################
    def Run(self):

        # Level loop
        Run = True

        # FrameRate counter
        Clock = pygame.time.Clock()

        # Editor Loop
        while Run:

            for Event in pygame.event.get():

                # Get out of level loop if user closes game
                if Event.type == pygame.QUIT:
                    Run = False			

            # Cap amount of fps
            Clock.tick(self.FrameRate)
            self.Update()

            # Update pygame window
            pygame.display.update()


    ######################
	#### 1.3 - Update ####
	######################
    def Update(self):

        # Draw background
        self.Window.fill((255,255,255))


    ######################
	#### 1.4 - Draw ####
	######################
    def Draw(self):
        """
        Draws everything required by the game
        """

        # Draw background
        self.DrawBackground()

        # Draw sidebar
        self.DrawSideBar()


    ################################
    #### 1.4.1 - DrawBackground ####
    ################################
    def DrawBackground(self):
        """
        Draws level background
        """

        # Draw background
        self.Window.blit(self.Background, (0,0))


    #############################
    #### 1.4.2 - DrawSideBar ####
    #############################
    def DrawSideBar(self):
        """
        Draw sidebar texture to right of background
        """

        # Draw sidebar
        self.Window.blit(self.SidebarTexture, (self.BackgroundDimensions[0], 0))