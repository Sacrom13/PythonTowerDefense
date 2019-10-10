# Required Libs
import pygame
import os

# Config Files
from Source.Archer.ArcherConfig import *
from Source.Enemy.EnemyConfig import *
from Source.Game.GameConfig import *
from Source.Level.LevelConfig import *
from Source.Projectile.ProjectileConfig import *
from Source.Tower.TowerConfig import *

class Resources():

    def __init__(self):
        """
        Initializes resources object
        """
        pass


    def LoadArcherResources(self):
        """
        Loads archer resources
        """

        # Get every archer and respective configurations
        for Name, Configs in ArcherConfigs.items():

            # Load Images
            ShootingImages = []

            # Shooting Images
            for i in range(Configs['ShootingImages']):

                # Image Path Relative to this file
                ImagePath = "Images/Archer/" + Name + "/Shoot/"  + str(i + 1) + ".png"

                # Load from absolute path, remove BG and scale
                Image = pygame.image.load(os.path.join(os.path.dirname(__file__), ImagePath)).convert_alpha()
                Image = pygame.transform.scale(Image, Configs['ImageDimensions'])

                # Save Image
                ShootingImages.append(Image)

            # Standby Image

            # Image Path Relative to this file
            ImagePath = "Images/Archer/" + Name + "/Standby/1.png"

            # Load from absolute path and scale
            Image = pygame.image.load(os.path.join(os.path.dirname(__file__), ImagePath)).convert_alpha()
            StandbyImage = pygame.transform.scale(Image, Configs['ImageDimensions'])

            # Save Both
            Images = ShootingImages, StandbyImage
            Configs['Images'] = Images


    def LoadEnemyResources(self):
        """
        Loads enemy resources
        """

        # Get every enemy and respective configurations
        for Name, Configs in EnemyConfigs.items():

            # Images to save
            Images = []

            # Load Enemy images
            for ImageType in Configs['ImageTypes']:
                
                # One array for each Image Type
                TypeImages = []

                # Load every image for each Type
                for i in range(Configs['ImagesPerType']):

                    # Image Path Relative to this file
                    ImagePath = "Images/Enemy/" + Name + "/" + ImageType + "/" + str(i + 1) + ".png"

                    # Load from absolute path, remove BG and scale
                    Image = pygame.image.load(os.path.join(os.path.dirname(__file__), ImagePath)).convert_alpha()
                    Image = pygame.transform.scale(Image, Configs['ImageDimensions'])

                    # Append image
                    TypeImages.append(Image)

                # Append list for each type
                Images.append(TypeImages)

            # Save Images
            Configs['Images'] = Images


    def LoadGameResources(self):
        """
        Loads game resources
        """

        # Load Loading Image
        
        # Image Path Relative to this file
        ImagePath = "Images/Game/Loading.png"

        # Load from absolute path, remove BG and scale
        Image = pygame.image.load(os.path.join(os.path.dirname(__file__), ImagePath)).convert_alpha()
        Image = pygame.transform.scale(Image, GameConfigs['ScreenDimensions'])

        # Save Image
        GameConfigs['LoadingImage'] = Image
    

    def LoadLevelResources(self):
        """
        Loads level resources
        """

        # Load Background Images

        # Folder where Level images are saved
        ImagePath = "Images/Level/Levels"

        # Go Through every folder in Levels
        for Root, Dirs, Files in os.walk(os.path.join(os.path.dirname(__file__), ImagePath)):

            # Go through each directory
            for Dir in Dirs:

                Configuration = {}

                # Load Background from absolute path, remove BG and scale
                Image = pygame.image.load(os.path.join(Root, Dir + '/Background.png')).convert_alpha()
                Image = pygame.transform.scale(Image, GameConfigs['ScreenDimensions'])

                # Save Image
                Configuration['Background'] = Image

                # Get Path
                Path = []

                # Open File
                File = open(os.path.join(Root, Dir + '/Path.py'), "r")

                # Read File
                Lines = File.readlines()
                for Line in Lines:
                    Numbers = Line.split(",")
                    Path.append((int(Numbers[0]), int(Numbers[1])))

                # Save Path
                Configuration['Path'] = Path

            # Save configuration for each level
            LevelConfigs[Dir] = Configuration   

        # Load Lives image
        
        # Image Path Relative to this file
        ImagePath = "Images/Level/Lives.png"

        # Load from absolute path, remove BG and scale
        Image = pygame.image.load(os.path.join(os.path.dirname(__file__), ImagePath)).convert_alpha()
        Image = pygame.transform.scale(Image, LevelConfigs['LiveImageDimensions'])

        # Save Image
        LevelConfigs['LiveImage'] = Image


    def LoadProjectileResources(self):
        """
        Loads projectile resources
        """

        # Get every projectile and respective configurations
        for Name, Configs in ProjectileConfigs.items():

            # Image Path Relative to this file
            ImagePath = "Images/Projectile/" + Name + ".png"

            # Load from absolute path, remove BG and scale
            Image = pygame.image.load(os.path.join(os.path.dirname(__file__), ImagePath)).convert_alpha()
            Image = pygame.transform.scale(Image, Configs['ImageDimensions'])

            # Save Image
            Configs['Image'] = Image


    def LoadTowerResources(self):
        """
        Loads tower resources
        """

        # Get every Tower and respective configurations
        for Name, Configs in TowerConfigs.items():

            Images = []

            for i in range(Configs['MaxLevel']):

                # Image Path Relative to this file
                ImagePath = "Images/Tower/" + Name + "/"  + str(i + 1) + ".png"

                # Load from absolute path, remove BG and scale
                Image = pygame.image.load(os.path.join(os.path.dirname(__file__), ImagePath)).convert_alpha()
                Image = pygame.transform.scale(Image, Configs['ImageDimensions'])

                Images.append(Image)

            # Save
            Configs['Images'] = Images

