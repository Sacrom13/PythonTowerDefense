############################
#### Required Libraries ####
############################

# System libs
import pygame
import os

# Configuration files
from Source.Archer.ArcherConfig import *
from Source.Enemy.EnemyConfig import *
from Source.Game.GameConfig import *
from Source.Level.LevelConfig import *
from Source.Projectile.ProjectileConfig import *
from Source.Tower.TowerConfig import *

########################
#### File Structure ####
########################

# 1 - Resources
# 	1.1 - Init
#   1.2 - LoadArcherResources
# 	1.3 - LoadEnemyResources
#   1.4 - LoadGameResources
#   1.5 - LoadLevelResources
#   1.6 - LoadProjectileResources
#   1.7 - LoadTowerResources

class Resources():

    ####################
    #### 1.1 - Init ####
    ####################
    def __init__(self):
        """
        Initializes resources object
        """
        pass

    ##########################
    #### 1.1 - LoadArcher ####
    ##########################
    def LoadArcherResources(self):
        """
        Loads archer resources
        """

        # Get every archer and respective configurations
        for Name, Configs in ArcherConfigs.items():

            # Load images
            ShootingImages = []

            # Shooting images
            for i in range(Configs['ShootingImages']):

                # Image path relative to this file
                ImagePath = "Images/Archer/" + Name + "/Shoot/"  + str(i + 1) + ".png"

                # Load from absolute path, remove background and scale
                Image = pygame.image.load(os.path.join(os.path.dirname(__file__), ImagePath)).convert_alpha()
                Image = pygame.transform.scale(Image, Configs['ImageDimensions'])

                # Save image
                ShootingImages.append(Image)

            # Standby image

            # Image path relative to this file
            ImagePath = "Images/Archer/" + Name + "/Standby/1.png"

            # Load from absolute path and scale
            Image = pygame.image.load(os.path.join(os.path.dirname(__file__), ImagePath)).convert_alpha()
            StandbyImage = pygame.transform.scale(Image, Configs['ImageDimensions'])

            # Save both
            Images = ShootingImages, StandbyImage
            Configs['Images'] = Images


    #########################
    #### 1.2 - LoadEnemy ####
    #########################
    def LoadEnemyResources(self):
        """
        Loads enemy resources
        """

        # Get every enemy and respective configurations
        for Name, Configs in EnemyConfigs.items():

            # Images to save
            Images = []

            # Load enemy images
            for ImageType in Configs['ImageTypes']:
                
                # One array for each image type
                TypeImages = []

                # Load every image for each type
                for i in range(Configs['ImagesPerType']):

                    # Image path relative to this file
                    ImagePath = "Images/Enemy/" + Name + "/" + ImageType + "/" + str(i + 1) + ".png"

                    # Load from absolute path, remove background and scale
                    Image = pygame.image.load(os.path.join(os.path.dirname(__file__), ImagePath)).convert_alpha()
                    Image = pygame.transform.scale(Image, Configs['ImageDimensions'])

                    # Append image
                    TypeImages.append(Image)

                # Append list for each type
                Images.append(TypeImages)

            # Save images
            Configs['Images'] = Images


    ########################
    #### 1.3 - LoadGame ####
    ########################
    def LoadGameResources(self):
        """
        Loads game resources
        """

        # Load loading image
        
        # Image path relative to this file
        ImagePath = "Images/Game/Loading.png"

        # Load from absolute path, remove background and scale
        Image = pygame.image.load(os.path.join(os.path.dirname(__file__), ImagePath)).convert_alpha()
        Image = pygame.transform.scale(Image, GameConfigs['ScreenDimensions'])

        # Save image
        GameConfigs['LoadingImage'] = Image
    

    #########################
    #### 1.1 - LoadLevel ####
    #########################
    def LoadLevelResources(self):
        """
        Loads level resources
        """

        ################################
        #### Load Background Images ####
        ################################

        # Folder where level images are saved
        ImagePath = "Images/Level/Levels"

        # Go through every folder in Levels
        for Root, Dirs, Files in os.walk(os.path.join(os.path.dirname(__file__), ImagePath)):

            # Go through each directory
            for Dir in Dirs:

                Configuration = {}

                # Load Background from absolute path, remove background and scale
                Image = pygame.image.load(os.path.join(Root, Dir + '/Background.png')).convert_alpha()
                Image = pygame.transform.scale(Image, GameConfigs['ScreenDimensions'])

                # Save image
                Configuration['Background'] = Image

                # Get path
                Path = []

                # Open file
                File = open(os.path.join(Root, Dir + '/Path.py'), "r")

                # Read file
                Lines = File.readlines()
                for Line in Lines:
                    Numbers = Line.split(",")
                    Path.append((int(Numbers[0]), int(Numbers[1])))

                # Save path
                Configuration['Path'] = Path

            # Save configuration for each level
            LevelConfigs[Dir] = Configuration   

        ##########################
        #### Load Lives Image ####
        ##########################
        
        # Image Path Relative to this file
        ImagePath = "Images/Level/Lives.png"

        # Load from absolute path, remove BG and scale
        Image = pygame.image.load(os.path.join(os.path.dirname(__file__), ImagePath)).convert_alpha()
        Image = pygame.transform.scale(Image, LevelConfigs['LiveImageDimensions'])

        # Save Image
        LevelConfigs['LiveImage'] = Image

        ##########################
        #### Load Money Image ####
        ##########################

        # Image Path Relative to this file
        ImagePath = "Images/Level/Money.png"

        # Load from absolute path, remove BG and scale
        Image = pygame.image.load(os.path.join(os.path.dirname(__file__), ImagePath)).convert_alpha()
        Image = pygame.transform.scale(Image, LevelConfigs['MoneyImageDimensions'])

        # Save Image
        LevelConfigs['MoneyImage'] = Image
        

    ##############################
    #### 1.1 - LoadProjectile ####
    ##############################
    def LoadProjectileResources(self):
        """
        Loads projectile resources
        """

        # Get every projectile and respective configurations
        for Name, Configs in ProjectileConfigs.items():

            # Image path relative to this file
            ImagePath = "Images/Projectile/" + Name + ".png"

            # Load from absolute path, remove background and scale
            Image = pygame.image.load(os.path.join(os.path.dirname(__file__), ImagePath)).convert_alpha()
            Image = pygame.transform.scale(Image, Configs['ImageDimensions'])

            # Save image
            Configs['Image'] = Image


    #########################
    #### 1.1 - LoadTower ####
    #########################
    def LoadTowerResources(self):
        """
        Loads tower resources
        """

        # Get every tower and respective configurations
        for Name, Configs in TowerConfigs.items():

            Images = []

            for i in range(Configs['MaxLevel']):

                # Image path relative to this file
                ImagePath = "Images/Tower/" + Name + "/"  + str(i + 1) + ".png"

                # Load from absolute path, remove background and scale
                Image = pygame.image.load(os.path.join(os.path.dirname(__file__), ImagePath)).convert_alpha()
                Image = pygame.transform.scale(Image, Configs['ImageDimensions'])

                Images.append(Image)

            # Save
            Configs['Images'] = Images

