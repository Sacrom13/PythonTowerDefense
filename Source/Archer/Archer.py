############################
#### Required Libraries ####
############################

# System libs
import pygame
import os
import math

# Archer Default Definitions
from Source.Archer.ArcherConfig import *

# Enemies
from Source.Enemy.Enemy import *

# Projectiles
from Source.Projectile.Projectile import *

########################
#### File Structure ####
########################

# 1 - Archer
# 	1.1 - Init
#   1.2 - Update
# 	1.3 - Draw
#   1.4 - Attack
#   1.5 - SetEnemy
#   1.6 - Move

####################
#### 1 - Archer ####
####################
class Archer():

    ####################
    #### 1.1 - Init ####
    ####################
    def __init__(self, Name, X, Y):
        """
        Initializes an archer
        
        Arguments:
            Name {String} -- Archer name
            X {Integer} -- X position
            Y {Integer} -- Y position
        """

        # Configurations
        self.Configs = ArcherConfigs[Name]

        # Position
        self.X = X
        self.Y = Y

        # Image dimensions
        self.ImageWidth, self.ImageHeight = self.Configs['ImageDimensions']

        # Images
        self.ShootingImages, self.StandbyImage = self.Configs['Images']

        # Image selection
        self.AnimationCount = 0

        # Enemy archer is attacking
        self.Enemy = None

        # FireRate
        self.FireRate = self.Configs['FireRate']

        # Projectiles fired by this archer
        self.Projectiles = []


    ######################
    #### 1.2 - Update ####
    ######################
    def Update(self, Window):
        """
        Does necessary actions for each frame
        
        Arguments:
            Window {Pygame surface} -- Window to draw on
        """

        # Attack
        self.Attack()

        # Draw archer
        self.Draw(Window)

        # Active projectiles
        for Projectile in self.Projectiles:

            # Update projectiles
            if Projectile.Update(Window):

                # Remove if projectile reached target enemy
                self.Projectiles.remove(Projectile)


    ####################
    #### 1.3 - Draw ####
    #################### 
    def Draw(self, Window):
        """
        Draws archer
        
        Arguments:
            Window {Pygame Surface} -- Window to draw on
        """

        # Select attacking image if enemy is in range
        if self.Enemy is not None:
            
            # Select image
            Image = self.ShootingImages[self.AnimationCount // self.FireRate]
            
            # Animation loop
            self.AnimationCount += 1
            if self.AnimationCount == len(self.ShootingImages * self.FireRate):
                self.AnimationCount = 0
            
            # Flip image if necessary
            if self.Enemy.X < self.X:
                Image = pygame.transform.flip(Image, True, False)

        # Select standby image if no enemies in range
        else:
            Image = self.StandbyImage
            self.AnimationCount = 0

        # Calculate position
        DrawX = self.X - self.ImageWidth/2
        DrawY = self.Y - self.ImageHeight/2

        # Draw archer
        Window.blit(Image, (DrawX, DrawY))


    ######################
    #### 1.4 - Attack ####
    ######################
    def Attack(self):
        """
        Attacks nearest enemy
        """

        # Only create new projectile if on first animation frame and enemy exists
        if self.AnimationCount == 0 and self.Enemy is not None:
            self.Projectiles.append(Projectile(self.Enemy, self.X, self.Y, self.Configs['Projectile']))


    ########################
    #### 1.5 - SetEnemy ####
    ########################
    def SetEnemy(self, Enemy):
        """
        Sets enemy
        
        Arguments:
            Enemy {Enemy} -- Enemy to set
        """

        # Set target enemy
        self.Enemy = Enemy

    
    ####################
    #### 1.6 - Move ####
    ####################
    def Move(self, X, Y):
        """
        Moves archer
        
        Arguments:
            X {Integer} -- X position
            Y {Integer} -- Y position
        """

        # Set new archer position
        self.X = X
        self.Y = Y