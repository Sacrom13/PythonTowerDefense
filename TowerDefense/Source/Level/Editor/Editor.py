############################
#### Required Libraries ####
############################

# System libs
import pygame
import os

# Editor Config
from Source.Config.EditorConfig import *

# Tiles
from Source.Level.Editor.Tile import *
from Source.Config.TileConfig import *

# Level Config
from Source.Config.LevelConfig import *

########################
#### File Structure ####
########################

# 1 - Editor
# 	1.1 - Init
#   1.2 - Run
#   1.3 - Update
#   1.4 - Draw
#   1.4.1 - DrawBackground
#   1.4.2 - DrawGrid
#   1.4.2 - DrawSidebar
#   1.4.3 - DrawSelectedTile
#   1.4.4 - DrawTileSelection

class Editor():

    ####################
	#### 1.1 - Init ####
	####################
    def __init__(self, ScreenDimensions, Window, FrameRate, Font):

        ################################
        #### General Configurations ####
        ################################

        # Screen Resolution
        self.ScreenDimensions = ScreenDimensions

        # Background Resolution
        self.BackgroundDimensions = LevelConfigs['BackgroundDimensions']

        # Window
        self.Window = Window

        # Sidebar Texture
        self.SidebarTexture = LevelConfigs['SidebarTexture']

        # FrameRate
        self.FrameRate = FrameRate

        # Font to write text with
        self.Font = Font


        ###############
        #### Tiles ####
        ###############      

        # Tiles
        self.Tiles = []  

        # Tile Dimensions
        self.TileDimensions = EditorConfigs['TileDimensions']

        # Check if dimensions are valid
        if (self.BackgroundDimensions[0] % self.TileDimensions[0] != 0) or (self.BackgroundDimensions[1] % self.TileDimensions[1] != 0):
            print("Error:")
            print("\t- Tile dimensions ", self.TileDimensions, " are not a multiple of background dimensions ", self.BackgroundDimensions, ".", sep="")
            print("\t- Check Source/Config/TileConfig and Source/Config/LevelConfig\n")
            exit(-1)

        # Add a bunch of white tiles as default background
        for x in range(0, self.BackgroundDimensions[0], self.TileDimensions[0]):
            for y in range(0, self.BackgroundDimensions[1], self.TileDimensions[1]):
                self.Tiles.append(Tile(self.Window, (x, y), 'White'))

        # Add each type of tile in selection
        self.SelectionTiles = []

        X = self.BackgroundDimensions[0] + EditorConfigs['TileSelectionOffset'][0]
        Y = EditorConfigs['TileSelectionOffset'][1]
        Position = X, Y

        Counter = 0
        for Name, Configs in TileConfigs.items():

            if Name is not 'Default':
                
                self.SelectionTiles.append(Tile(self.Window, Position, Name))

                X += self.TileDimensions[0]
                Counter += 1

                if Counter == EditorConfigs['TilesPerRow']:
                    Y += self.TileDimensions[1]
                    X = self.BackgroundDimensions[0] + EditorConfigs['TileSelectionOffset'][0]
                    Counter = 0

                Position = X, Y

        # Pick a random tile to be selected at start
        self.SelectedTile = self.SelectionTiles[0]
                
        
        

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

                # Check if Button has been pressed
                MousePos = pygame.mouse.get_pos()
                if Event.type == pygame.MOUSEBUTTONDOWN:
                    self.HandleButtonPress(MousePos)

            # Cap amount of fps
            Clock.tick(self.FrameRate)
            self.Update()


    ######################
	#### 1.3 - Update ####
	######################
    def Update(self):

        # Draw
        self.Draw()

        # Update pygame window
        pygame.display.update()


    ######################
	#### 1.4 - Draw ####
	######################
    def Draw(self):
        """
        Draws everything required by the game
        """

        # Draw background
        self.DrawBackground()

        # Draw Grid
        self.DrawGrid()

        # Draw sidebar
        self.DrawSideBar()


    ################################
    #### 1.4.1 - DrawBackground ####
    ################################
    def DrawBackground(self):
        """
        Draws level background
        """

        # Draw tiles
        for T in self.Tiles:
            T.Draw()

    
    ##########################
    #### 1.4.1 - DrawGrid ####
    ##########################
    def DrawGrid(self):
        """
        Draws Grid for better understanding of tiles
        """

        for x in range(self.TileDimensions[0], self.BackgroundDimensions[0], self.TileDimensions[0]):
            pygame.draw.line(self.Window, (0,0,0), (x, 0), (x, self.BackgroundDimensions[1]))

        for y in range(self.TileDimensions[1], self.BackgroundDimensions[1], self.TileDimensions[1]):
            pygame.draw.line(self.Window, (0,0,0), (0, y), (self.BackgroundDimensions[0], y))


    #############################
    #### 1.4.3 - DrawSideBar ####
    #############################
    def DrawSideBar(self):
        """
        Draw sidebar texture to right of background
        """
        
        # Draw sidebar
        self.Window.blit(self.SidebarTexture, (self.BackgroundDimensions[0], 0))

        # Draw info on sidebar
        for T in self.SelectionTiles:
            T.Draw()

        # Highlight around selected tile

        # Calculate points
        TopLeft = self.SelectedTile.Position
        TopRight = (self.SelectedTile.Position[0] + self.TileDimensions[0], self.SelectedTile.Position[1])
        BottomLeft = (self.SelectedTile.Position[0], self.SelectedTile.Position[1] + self.TileDimensions[1])
        BottomRight = (self.SelectedTile.Position[0] + self.TileDimensions[0], self.SelectedTile.Position[1] + self.TileDimensions[1])

        pygame.draw.line(self.Window, (0,0,0), (TopLeft), (TopRight))
        pygame.draw.line(self.Window, (0,0,0), (BottomLeft), (BottomRight))
        pygame.draw.line(self.Window, (0,0,0), (TopLeft), (BottomLeft))
        pygame.draw.line(self.Window, (0,0,0), (TopRight), (BottomRight))



    #################################
    #### 1.5 - HandleButtonPress ####
    #################################
    def HandleButtonPress(self, MousePos):

        ####################
        #### Background ####
        ####################

        if MousePos[0] < self.BackgroundDimensions[0]:

            # Check all tiles until clicked one is found
            for T in self.Tiles:

                # Check if tile was clicked
                if T.Clicked(MousePos):

                    # Remove clicked tile from list
                    self.Tiles.remove(T)

                    # Add new tile at the same position, with correct color
                    self.Tiles.append(Tile(self.Window, T.Position, self.SelectedTile.Name))

                    # don't need to check any further tiles once clicked tile has been found
                    break


        #################
        #### Sidebar ####
        #################

        if MousePos[0] > self.BackgroundDimensions[0]:

            # Check all tiles until clicked one is found
            for T in self.SelectionTiles:

                # Check if tile was clicked
                if T.Clicked(MousePos):

                    # Update selected tile
                    self.SelectedTile = T

                    # don't need to check any further tiles once clicked tile has been found
                    break

        
        

        