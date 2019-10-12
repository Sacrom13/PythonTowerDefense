############################
#### Required Libraries ####
############################

# System libs
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
        Initializes an enemy
        
        Arguments:
            Name {String} -- Name of enemy
            Path {List} -- Points enemy will follow
        """

        # Configurations
        self.Configs = EnemyConfigs[Name]

        # Path enemy will take
        self.Path = Path

        # Enemy position
        self.X = self.Path[0][0]
        self.Y = self.Path[0][1]

        # Enemy speed
        self.Velocity = self.Configs['Velocity']

        # Image selection
        self.AnimationCount = 0

        # Image dimensions
        self.ImageWidth, self.ImageHeight = self.Configs['ImageDimensions']

        # Images
        self.Images = self.Configs['Images']

        # Enemy health
        self.MaxHealth = self.Configs['MaxHealth']
        self.Health = self.MaxHealth

        # Health bar
        self.HealthBarLength = self.Configs['HealthBarLength']
        self.HealthBarYOffset = self.Configs['HealthBarYOffset']

        # Movement updates for each frame
        self.Position = 0
        self.PositionUpdates = []
        self.ImageType = []

        for Position in range(len(self.Path)):

            # Starting point
            StartPosition = self.Path[Position]

            # Final point
            if Position == (len(self.Path) - 1):
                EndPosition = (810, self.Path[Position][1])
            else:
                EndPosition = self.Path[Position + 1]

            # Trajectory vector
            Direction = (EndPosition[0] - StartPosition[0], EndPosition[1] - StartPosition[1])

            # Frames required to move between points
            Distance = math.sqrt(Direction[0]**2 + Direction[1]**2)
            NFrames = round(Distance/self.Velocity)

            # Unit vector
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
        Does necessary actions for each frame
        
        Arguments:
            Window {Pygame Surface} -- Window to draw on
        
        Returns:
            [Boolean] -- True if enemy dead, false otherwise
        """

        # Move enemy
        self.Move()

        # Draw required images
        self.Draw(Window)

        # Return if enemy is dead
        return self.Health == 0


    ####################
	#### 1.3 - Draw ####
	####################
    def Draw(self, Window):
        """
        Draws enemy and health bar
        
        Arguments:
            Window {Pygame Surface} -- Window to draw on 
        """

        # Draw enemy
        self.DrawEnemy(Window)

        # Draw health bar
        self.DrawHealthBar(Window)


    ############################
	#### 1.3.1 - Draw Enemy ####
	############################
    def DrawEnemy(self, Window):
        """
        Draws enemy

        Arguments:
            Window {Pygame Surface} -- Window to draw on
        """
        # Select image
        Image = self.Images[self.ImageType[self.Position]][self.AnimationCount]

        # Animation loop
        self.AnimationCount += 1
        if self.AnimationCount == len(self.Images[self.ImageType[self.Position]]):
            self.AnimationCount = 0
        
        # Calculate position
        DrawX = self.X - self.ImageWidth/2
        DrawY = self.Y - self.ImageHeight/2

        # Draw
        Window.blit(Image, (DrawX, DrawY))


    #################################
	#### 1.3.2 - Draw Health Bar ####
	#################################
    def DrawHealthBar(self, Window):
        """
        Draws health bar
        
        Arguments:
            Window {Pygame Surface} -- Window to draw on
        """

        # Green health bar length
        Length = self.Health * round(self.HealthBarLength / self.MaxHealth)

        # Calculate position
        DrawX = self.X - (self.HealthBarLength/2)
        DrawY = self.Y - (self.ImageHeight/2) - self.HealthBarYOffset

        # Draw red
        pygame.draw.rect(Window, (255, 0, 0), (DrawX, DrawY, self.HealthBarLength, 10), 0)

        # Draw green
        pygame.draw.rect(Window, (0, 255, 0), (DrawX, DrawY, Length, 10), 0)
    

    ####################
	#### 1.4 - Move ####
	####################x
    def Move(self):
        """
        Move enemy
        """

        # Calculate new position
        self.X += self.Velocity * self.PositionUpdates[self.Position][0]
        self.Y += self.Velocity * self.PositionUpdates[self.Position][1]

        # New position in update vector
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
            Y {Integer} -- Position to check
        
        Returns:
            [Boolean] -- True if enemy hit, false otherwise
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
        Removes health
        """

        # Decrement Health, but not if already 0
        self.Health = max(self.Health - 1, 0)