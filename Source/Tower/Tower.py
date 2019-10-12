############################
#### Required Libraries ####
############################

# System libs
import pygame
import os

# Tower Default Definitions
from Source.Tower.TowerConfig import *

# Archers
from Source.Archer.Archer import *

# Projectiles
from Source.Projectile.Projectile import *

########################
#### File Structure ####
########################

# 1 - Tower
# 	1.1 - Init
#   1.2 - Update
# 	1.3 - Draw
#   1.4 - Attack
#	1.5 - Click
#   1.6 - Sell
#   1.7 - Upgrade
#   1.8 - AddArcher
#   1.9 - Move


###################
#### 1 - Tower ####
###################
class Tower:

    ####################
    #### 1.1 - Init ####
    ####################
    def __init__(self, X, Y, Name):
        """
        Initialize tower
        
        Arguments:
            X {Integer} -- Position of tower center
            Y {Integer} -- Position of tower center
            Name {String} -- Tower name
        """

        # Tower configs
        self.Configs = TowerConfigs[Name]

        # Tower position
        self.X = X
        self.Y = Y
  
        # Image dimensions
        self.ImageWidth, self.ImageHeight = self.Configs['ImageDimensions']

        # Images
        self.TowerImages = self.Configs['Images']

        # Tower levels
        self.Level = 1
        self.MaxLevel = self.Configs['MaxLevel']

        # Archers
        self.Archers = []

        # Range of archers in this tower
        self.Range = self.Configs['Range']

        # Money
        self.SellMoney = self.Configs['SellMoney']
        self.BuyMoney = self.Configs['BuyMoney']

        # Tower selection by user
        self.Selected = False
        self.Menu = None


    ######################
    #### 1.2 - Update ####
    ######################
    def Update(self, Window, Enemies):
        """
        Does necessary actions for each frame
        
        Arguments:
            Window {Pygame Surface} -- Window to draw on
            Enemies {List} -- List of enemies on the screen
        """

        # Attack
        self.Attack(Enemies)

        # Draw tower
        self.Draw(Window)

        # Archer updates
        for Archer in self.Archers:
            Archer.Update(Window)


    ####################
    #### 1.3 - Draw ####
    ####################
    def Draw(self, Window):
        """
        Draws tower
        
        Arguments:
            Window {Pygame Surface} -- Window to draw on
        """
        
        # Select tower image
        Image = self.TowerImages[self.Level - 1]

        # Calculate position
        DrawX = self.X - self.ImageWidth/2
        DrawY = self.Y - self.ImageHeight/2

        # Draw
        Window.blit(Image, (DrawX, DrawY))


    ######################
    #### 1.4 - Attack ####
    ######################
    def Attack(self, Enemies):
        """
        Finds closest enemy and sets Archer target
       
        Arguments:
            Enemies {List} -- List of enemies currently on the screen
        """

        # Find distance to closest enemy
        SmallestDistance = 999
        Closest = None

        for enemy in Enemies:

            # Calculate distance
            EnemyDistance = math.sqrt( (self.X - enemy.X)**2 + (self.Y - enemy.Y)**2 )

            # Check if closest
            if EnemyDistance < SmallestDistance :
                Closest = enemy
                SmallestDistance = EnemyDistance
        
        # Closest enemy in firing range!
        if SmallestDistance < self.Range:

            # Set archer target
            for Archer in self.Archers:
                Archer.SetEnemy(Closest)

        # Closest enemy outside firing range.
        else:
            
            # Signal no enemy is in range.
            for Archer in self.Archers:
                Archer.SetEnemy(None)


    #####################
    #### 1.5 - Click ####
    #####################
    def Click(self, X, Y):
        """
        Selects tower if it's clicked
        
        Arguments:
            X {Integer} -- X position of click
            Y {Integer} -- Y position of click
        
        Returns:
            [Boolean] -- True if clicked, false otherwise
        """

        # Check if position is within image bounds
        if X >= self.X and X <= self.X + self.ImageWidth:
            if Y >= self.Y and Y <= self.Y + self.ImageHeight:
                return True
        return False


    ####################
    #### 1.6 - Sell ####
    ####################
    def Sell(self):
        """
        Sells a tower

        Returns:
            [Integer] -- Amount of money to give the player when selling a tower
        """

        # Return amount of money to give the player
        return self.SellMoney[self.Level - 1]


    #######################
    #### 1.7 - Upgrade ####
    #######################
    def Upgrade(self):
        """
        Upgrades a tower
        
        Returns:
            [Integer] -- Amount of money upgrade costs, or -1 if already maximum level
        """

        # If under maximum level
        if self.Level < self.MaxLevel:
            
            # Upgrade tower level
            self.Level += 1
            
            # Return money
            return self.BuyMoney[self.Level - 1]

        # Can't upgrade because tower is already maximum level
        return -1


    #########################
    #### 1.8 - AddArcher ####
    #########################
    def AddArcher(self, Name):
        """
        Adds an archer to this tower
        
        Arguments:
            Name {String} -- Name of archer to add
        
        Returns:
            [Boolean] -- True if archer added, false if not
        """

        XTowerTops, YTowerTops = self.Configs['TowerTops']

        if len(self.Archers) == 0:

            # Calculate position
            ArcherX = self.X
            ArcherY = self.Y - (self.ImageHeight/2) + (YTowerTops * self.ImageHeight)

        elif len(self.Archers) == 1:

            # Update old archer position (left)
            ArcherX = self.X - (self.ImageWidth/2) + (XTowerTops * self.ImageWidth)
            ArcherY = self.Y - (self.ImageHeight/2) + (YTowerTops * self.ImageHeight)
            self.Archers[0].Move(ArcherX, ArcherY)

            # New Archer position (right)
            ArcherX = self.X + (self.ImageWidth/2) - (XTowerTops * self.ImageWidth)
            ArcherY = self.Y - (self.ImageHeight/2) + (YTowerTops * self.ImageHeight)

        else:
            return False

        # Add new archer with calculated position
        self.Archers.append(Archer(Name, ArcherX, ArcherY))
        return True


    ####################
    #### 1.9 - Move ####
    ####################
    def Move(self, X, Y):
        """
        Moves a tower
        
        Arguments:
            X {Integer} -- New X position of tower
            Y {Integer} -- New Y position of tower
        """

        # Save new tower position
        self.X = X
        self.Y = Y
