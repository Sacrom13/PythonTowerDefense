# Required Libs
import pygame
import math
import os

# Enemy Default Definitions
from Source.Enemy.EnemyConfig import *

########################
#### File Structure ####
########################

# 1 - Enemy
# 	1.1 - Init
#   1.2 - Update
# 	1.3 - Draw
#       1.3.1 - DrawEnemy
#       1.3.2 - DrawHealthBar
#   1.4 - Move
#	1.5 - Collide
#   1.6 - Hit

###################
#### 1 - Enemy ####
###################
class Enemy:

    ####################
	#### 1.1 - Init ####
	####################
    def __init__(self, Name, Path):
        """
        Initializes an Enemy
        
        Arguments:
            Name {String} -- Name of Enemy
        """

        # Configurations
        self.Configs = EnemyConfigs[Name]

        # Path Enemies will take
        self.Path = Path

        # Enemy Position
        self.X = self.Path[0][0]
        self.Y = self.Path[0][1]

        # Enemy Speed
        self.Velocity = self.Configs['Velocity']

        # Image Selection
        self.AnimationCount = 0

        # Image Dimensions
        self.ImageWidth, self.ImageHeight = self.Configs['ImageDimensions']

        # Images
        self.Images = self.Configs['Images']

        # Enemy Health
        self.MaxHealth = self.Configs['MaxHealth']
        self.Health = self.MaxHealth

        # Health Bar
        self.HealthBarLength = self.Configs['HealthBarLength']
        self.HealthBarYOffset = self.Configs['HealthBarYOffset']

        # Movement updates for each frame
        self.Position = 0
        self.PositionUpdates = []
        self.ImageType = []

        for Position in range(len(self.Path)):

            # Starting Point
            StartPosition = self.Path[Position]

            # Final Point
            if Position == (len(self.Path) - 1):
                EndPosition = (810, self.Path[Position][1])
            else:
                EndPosition = self.Path[Position + 1]

            # Trajectory Vector
            Direction = (EndPosition[0] - StartPosition[0], EndPosition[1] - StartPosition[1])

            # Frames required to move between points
            Distance = math.sqrt(Direction[0]**2 + Direction[1]**2)
            NFrames = round(Distance/self.Velocity)

            # Unit Vector
            Direction = (Direction[0]/Distance, Direction[1]/Distance)

            # Image type for each frame
            if abs(Direction[0]) > abs(Direction[1]):

                # Right
                if(Direction[0] > 0):
                    ImageType = 2
                    
                # Left
                else:
                    ImageType = 1
            else :

                # Up
                if(Direction[1] > 0):
                    ImageType = 0

                # Down
                else:
                    ImageType = 3

            # Append
            for Frame in range(NFrames):
                self.PositionUpdates.append(Direction)
                self.ImageType.append(ImageType)


    ######################
	#### 1.2 - Update ####
	######################
    def Update(self, Window):
        """
        Does Necessary actions for each frame
        
        Arguments:
            Window {Pygame Surface} -- Surface to Draw on
        
        Returns:
            [Boolean] -- True if enemy dead, false otherwise
        """
        self.Move()
        self.Draw(Window)

        return self.Health == 0


    ####################
	#### 1.3 - Draw ####
	####################
    def Draw(self, Window):
        """
        Draws enemy and Health Bar
        
        Arguments:
            Window {Pygame Window} -- Surface to draw on 
        """
        self.DrawEnemy(Window)
        self.DrawHealthBar(Window)


    ############################
	#### 1.3.1 - Draw Enemy ####
	############################
    def DrawEnemy(self, Window):
        """
        Draws Enemy

        Arguments:
            Window {Pygame Window} -- Surface to draw on
        """
        # Select Image
        Image = self.Images[self.ImageType[self.Position]][self.AnimationCount]

        # Animation Loop
        self.AnimationCount += 1
        if self.AnimationCount == len(self.Images[self.ImageType[self.Position]]):
            self.AnimationCount = 0
        
        # Calculate Position
        DrawX = self.X - self.ImageWidth/2
        DrawY = self.Y - self.ImageHeight/2

        # Draw
        Window.blit(Image, (DrawX, DrawY))


    #################################
	#### 1.3.2 - Draw Health Bar ####
	#################################
    def DrawHealthBar(self, Window):
        """
        Draws Health Bar
        
        Arguments:
            Window {Pygame Window} -- Surface to draw on
        """

        # Green Health Bar Length
        Length = self.Health * round(self.HealthBarLength / self.MaxHealth)

        # Calculate Position
        DrawX = self.X - (self.HealthBarLength/2)
        DrawY = self.Y - (self.ImageHeight/2) - self.HealthBarYOffset

        # Draw Red
        pygame.draw.rect(Window, (255, 0, 0), (DrawX, DrawY, self.HealthBarLength, 10), 0)

        # Draw Green
        pygame.draw.rect(Window, (0, 255, 0), (DrawX, DrawY, Length, 10), 0)
    

    ####################
	#### 1.4 - Move ####
	####################x
    def Move(self):
        """
        Move Enemy
        """

        # Calculate new Position
        self.X += self.Velocity * self.PositionUpdates[self.Position][0]
        self.Y += self.Velocity * self.PositionUpdates[self.Position][1]

        # New position in Updates Vector
        self.Position += 1
        if(self.Position == len(self.PositionUpdates)):
            self.Position = 0


    #######################
	#### 1.5 - Collide ####
	#######################
    def Collide(self, X, Y):
        """
        Checks if point (x,y) is colliding with enemy
        
        Arguments:
            X {Integer} -- Position to check
            Y {Integer} -- Position to Check
        
        Returns:
            [Boolean] -- True if enemy hit, False otherwise
        """

        # Check if position is within image bounds
        if X >= self.X and X <= self.X + self.ImageWidth:
            if Y >= self.Y and Y <= self.Y + self.ImageHeight:
                return True
        return False


    ###################
	#### 1.6 - Hit ####
	###################
    def Hit(self):
        """
        Removes Health
        """

        # Decrement Health
        self.Health = max(self.Health-1, 0)