############################
#### Required Libraries ####
############################

# System Libs
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
        Initializes a projectile
        
        Arguments:
            Target {Enemy} -- Enemy projectile was fired at
            X {Integer} -- Screen position
            Y {Integer} -- Screen position
            Name {String} -- Projectile name
        """

        # Projectile configurations
        self.Configs = ProjectileConfigs[Name]
        
        # Projectile position
        self.X = X
        self.Y = Y

        # Projectile dimensions
        self.ImageWidth, self.ImageHeight = self.Configs['ImageDimensions']

        # Image
        self.Image = self.Configs['Image']

        # Target enemy
        self.Target = Target

        # Projectile speed
        self.Speed = self.Configs['Speed']

    ######################
    #### 1.2 - Update ####
    ######################
    def Update(self, Window):
        """
        Does necessary actions for each frame
        
        Arguments:
            Window {Pygame Surface} -- Window to draw on
        
        Returns:
            [Boolean] -- True if projectile hit enemy or enemy died, false otherwise
        """

        # Check if enemy died
        if self.Target == None:
            return True

        # Move projectile
        self.Move()

        # Draw projectile
        self.Draw(Window)

        # Check if projectile collided with enemy
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
        Draws projectile
        
        Arguments:
            Window {Pygame Surface} -- Window to draw on
        """

        # Select image
        Image = self.Image
        if self.Target.X < self.X:
            Image = pygame.transform.flip(Image, True, False)

        # Calculate position
        DrawX = self.X - self.ImageWidth/2
        DrawY = self.Y - self.ImageHeight/2

        # Draw
        Window.blit(Image, (DrawX, DrawY))

    ####################
    #### 1.4 - Move ####
    ####################
    def Move(self):
        """
        Moves projectile
        """

        # Projectile and enemy positions
        CurrentPosition = (self.X, self.Y)
        TargetPosition = (self.Target.X, self.Target.Y)

        # Trajectory vector
        Direction = (TargetPosition[0] - CurrentPosition[0], TargetPosition[1] - CurrentPosition[1])

        # Distance between both points
        Distance = math.sqrt(Direction[0]**2 + Direction[1]**2)

        # Unit vector
        Direction = (Direction[0]/Distance, Direction[1]/Distance)

        # Move
        self.X += self.Speed * Direction[0]
        self.Y += self.Speed * Direction[1]