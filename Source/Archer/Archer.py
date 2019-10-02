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
        Initializes an Archer
        
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

        # Image Dimensions
        self.ImageWidth, self.ImageHeight = self.Configs['ImageDimensions']

        # Images
        self.ShootingImages, self.StandbyImage = self.Configs['Images']

        # Image Selection
        self.AnimationCount = 0

        # Enemy Archer is attacking
        self.Enemy = None

        # Fire Rate
        self.FireRate = self.Configs['FireRate']

        # Projectiles fired by this Archer
        self.Projectiles = []


    ######################
    #### 1.2 - Update ####
    ######################
    def Update(self, Window):
        """
        Does necessary actions for each frame
        
        Arguments:
            Window {Pygame Surface} -- Window to draw on
        """

        # Attack
        self.Attack()

        # Draw Archer
        self.Draw(Window)

        # Active projectiles
        for Projectile in self.Projectiles:

            # Update Projectiles
            if Projectile.Update(Window):

                # Remove if projectile reached target enemy
                self.Projectiles.remove(Projectile)


    ####################
    #### 1.3 - Draw ####
    #################### 
    def Draw(self, Window):
        """
        Draws Archer
        
        Arguments:
            Window {Pygame Surface} -- Surface to Draw On
        """

        # Select Attacking Image if enemy is in range
        if self.Enemy is not None:
            
            # Select Image
            Image = self.ShootingImages[self.AnimationCount // self.FireRate]
            
            # Animation Loop
            self.AnimationCount += 1
            if self.AnimationCount == len(self.ShootingImages * self.FireRate):
                self.AnimationCount = 0
            
            # Flip image if necessary
            if self.Enemy.X < self.X:
                Image = pygame.transform.flip(Image, True, False)

        # Select Standby image if no enemies in range
        else:
            Image = self.StandbyImage
            self.AnimationCount = 0

        # Calculate Position
        DrawX = self.X - self.ImageWidth/2
        DrawY = self.Y - self.ImageHeight/2

        # Draw Archer
        Window.blit(Image, (DrawX, DrawY))


    ######################
    #### 1.4 - Attack ####
    ######################
    def Attack(self):
        """
        Attacks nearest enemy
        """
        if self.AnimationCount == 0 and self.Enemy is not None:
            self.Projectiles.append(Projectile(self.Enemy, self.X, self.Y, self.Configs['Projectile']))


    ########################
    #### 1.5 - SetEnemy ####
    ########################
    def SetEnemy(self, Enemy):
        """
        Sets Enemy
        
        Arguments:
            Enemy {Enemy} -- Enemy to set
        """
        self.Enemy = Enemy

    
    ####################
    #### 1.6 - Move ####
    ####################
    def Move(self, X, Y):
        """
        Moves Archer
        
        Arguments:
            X {Integer} -- X position
            Y {Integer} -- Y position
        """
        self.X = X
        self.Y = Y