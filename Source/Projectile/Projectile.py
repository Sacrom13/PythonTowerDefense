# Required Libs
import pygame
import os
import math

# Projectile Definitions
from Source.Projectile.ProjectileConfig import *

# Enemies
from Source.Enemy.Enemy import *

########################
#### File Structure ####
########################

# 1 - Projectile
# 	1.1 - Init
#   1.2 - Update
# 	1.3 - Draw
#       1.3.1 - DrawEnemy
#       1.3.2 - DrawHealthBar
#   1.4 - Move

########################
#### 1 - Projectile ####
########################
class Projectile:

    ####################
    #### 1.1 - Init ####
    ####################
    def __init__(self, Target, X, Y, Name):
        """
        Initializes a Projectile
        
        Arguments:
            Target {Enemy} -- Enemy projectile was fired at
            X {Integer} -- Screen Position
            Y {Integer} -- Screen Position
            Name {String} -- Projectile Name
        """

        # Projectile Configurations
        self.Configs = ProjectileConfigs[Name]
        
        # Projectile Position
        self.X = X
        self.Y = Y

        # Projectile Dimensions
        self.ImageWidth, self.ImageHeight = self.Configs['ImageDimensions']

        # Image
        self.Image = self.Configs['Image']

        # Target Enemy
        self.Target = Target

        # Projectile Speed
        self.Speed = self.Configs['Speed']

    ######################
    #### 1.2 - Update ####
    ######################
    def Update(self, Window):
        """
        Does necessary actions for each frame
        
        Arguments:
            Window {Pygame Window} -- Surface to draw on
        
        Returns:
            [Boolean] -- True if projectile hit enemy, false otherwise
        """

        # Move Projectile
        self.Move()

        # Draw Projectile
        self.Draw(Window)
        
        # Check if Projectile collided with enemy
        if self.Target.Collide(self.X, self.Y):
            self.Target.Hit()
            return True
        else:
            return False

    ####################
    #### 1.3 - Draw ####
    ####################
    def Draw(self, Window):
        """
        Draws Projectile
        
        Arguments:
            Window {Pygame Window} -- Surface to Draw on
        """

        # Select Image
        Image = self.Image
        if self.Target.X < self.X:
            Image = pygame.transform.flip(Image, True, False)

        # Calculate Position
        DrawX = self.X - self.ImageWidth/2
        DrawY = self.Y - self.ImageHeight/2

        # Draw
        Window.blit(Image, (DrawX, DrawY))

    ####################
    #### 1.4 - Move ####
    ####################
    def Move(self):
        """
        Moves Projectile
        """

        # Projectile and Enemy Positions
        CurrentPosition = (self.X, self.Y)
        TargetPosition = (self.Target.X, self.Target.Y)

        # Trajectory Vector
        Direction = (TargetPosition[0] - CurrentPosition[0], TargetPosition[1] - CurrentPosition[1])

        # Distance between both points
        Distance = math.sqrt(Direction[0]**2 + Direction[1]**2)

        # Unit Vector
        Direction = (Direction[0]/Distance, Direction[1]/Distance)

        # Move
        self.X += self.Speed * Direction[0]
        self.Y += self.Speed * Direction[1]