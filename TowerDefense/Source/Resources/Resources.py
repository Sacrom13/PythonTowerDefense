############################
#### Required Libraries ####
############################

# System libs
import pygame
import os

# Configuration file
from Source.Config.ResourceConfig import *

# Configuration files from remaining classes
from Source.Config.ArcherConfig import *
from Source.Config.ButtonConfig import *
from Source.Config.EditorConfig import *
from Source.Config.EnemyConfig import *
from Source.Config.GameConfig import *
from Source.Config.LevelConfig import *
from Source.Config.ProjectileConfig import *
from Source.Config.TileConfig import *
from Source.Config.TowerConfig import *

########################
#### File Structure ####
########################

# 1 - Resources
# 	1.1 - Init
#   1.2 - LoadArcherResources
#   1.3 - LoadButtonResources
#   1.4 - LoadEditorResources
#   1.5 - LoadEnemyResources
#   1.6 - LoadGameResources
#   1.7 - LoadLevelResources
#   1.8 - LoadProjectileResources
#   1.9 - LoadTowerResources


#######################
#### 1 - Resources ####
#######################
class Resources():

    ####################
    #### 1.1 - Init ####
    ####################
    def __init__(self):
        """
        Initializes resources object
        """
        pass


    ###################################
    #### 1.2 - LoadArcherResources ####
    ###################################
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

                # Load from absolute path and scale
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


    ###################################
    #### 1.3 - LoadButtonResources ####
    ###################################
    def LoadButtonResources(self):
        """
        Loads resources for button class
        """
        pass
    

    ###################################
    #### 1.4 - LoadEditorResources ####
    ###################################
    def LoadEditorResources(self):
        """
        Loads resources for editor class
        """
        pass


    ##################################
    #### 1.5 - LoadEnemyResources ####
    ##################################
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

                    # Load from absolute path and scale
                    Image = pygame.image.load(os.path.join(os.path.dirname(__file__), ImagePath)).convert_alpha()
                    Image = pygame.transform.scale(Image, Configs['ImageDimensions'])

                    # Append image
                    TypeImages.append(Image)

                # Append list for each type
                Images.append(TypeImages)

            # Save images
            Configs['Images'] = Images


    #################################
    #### 1.6 - LoadGameResources ####
    #################################
    def LoadGameResources(self):
        """
        Loads resources for game class
        """

        # Load loading image
        
        # Image path relative to this file
        ImagePath = "Images/Game/Loading.png"

        # Load from absolute path, remove background and scale
        Image = pygame.image.load(os.path.join(os.path.dirname(__file__), ImagePath)).convert_alpha()
        Image = pygame.transform.scale(Image, GameConfigs['ScreenDimensions'])

        # Save image
        GameConfigs['LoadingImage'] = Image


    ##################################
    #### 1.7 - LoadLevelResources ####
    ##################################
    def LoadLevelResources(self):
        """
        Loads resources for level class
        """

        ################################
        #### Load Background Images ####
        ################################

        # Folder where level images are saved
        ImagePath = "Images/Level/Levels"

        # Go through every folder in levels
        for Root, Dirs, Files in os.walk(os.path.join(os.path.dirname(__file__), ImagePath)):

            # Go through each directory
            for Dir in Dirs:

                Configuration = {}

                # Load from absolute path and scale
                Image = pygame.image.load(os.path.join(Root, Dir + '/Background.png')).convert_alpha()
                Image = pygame.transform.scale(Image, LevelConfigs['BackgroundDimensions'])

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
        
        # Image path relative to this file
        ImagePath = "Images/Level/Lives.png"

        # Load from absolute path and scale
        Image = pygame.image.load(os.path.join(os.path.dirname(__file__), ImagePath)).convert_alpha()
        Image = pygame.transform.scale(Image, LevelConfigs['LiveImageDimensions'])

        # Save image
        LevelConfigs['LiveImage'] = Image

        ##########################
        #### Load Money Image ####
        ##########################

        # Image path relative to this file
        ImagePath = "Images/Level/Money.png"

        # Load from absolute path and scale
        Image = pygame.image.load(os.path.join(os.path.dirname(__file__), ImagePath)).convert_alpha()
        Image = pygame.transform.scale(Image, LevelConfigs['MoneyImageDimensions'])

        # Save image
        LevelConfigs['MoneyImage'] = Image

        ############################
        #### Load Sidebar Image ####
        ############################

        # Image path relative to this file
        ImagePath = "Images/Level/SidebarBackground.png"

        # Calculate sidebar dimensions
        SidebarDimensions = GameConfigs['ScreenDimensions'][0] - LevelConfigs['BackgroundDimensions'][0]

        # Load from absolute path and scale
        Image = pygame.image.load(os.path.join(os.path.dirname(__file__), ImagePath)).convert_alpha()
        Image = pygame.transform.scale(Image, (SidebarDimensions, GameConfigs['ScreenDimensions'][1]))

        # Save image
        LevelConfigs['SidebarTexture'] = Image

        ########################################
        #### Load Remaining Level Resources ####
        ########################################

        self.LoadEnemyResources()
        self.LoadProjectileResources()
        self.LoadArcherResources()
        self.LoadTowerResources()

    
    #######################################
    #### 1.8 - LoadProjectileResources ####
    #######################################
    def LoadProjectileResources(self):
        """
        Loads projectile resources
        """

        # Get every projectile and respective configurations
        for Name, Configs in ProjectileConfigs.items():

            # Image path relative to this file
            ImagePath = "Images/Projectile/" + Name + ".png"

            # Load from absolute path and scale
            Image = pygame.image.load(os.path.join(os.path.dirname(__file__), ImagePath)).convert_alpha()
            Image = pygame.transform.scale(Image, Configs['ImageDimensions'])

            # Save image
            Configs['Image'] = Image


    ##################################
    #### 1.9 - LoadTowerResources ####
    ##################################
    def LoadTowerResources(self):
        """
        Loads tower resources
        """

        # Get every tower and respective configurations
        for Name, Configs in TowerConfigs.items():

            ###########################
            #### Load Tower Images ####
            ###########################

            Images = []

            for i in range(Configs['MaxLevel']):

                # Image path relative to this file
                ImagePath = "Images/Tower/" + Name + "/"  + str(i + 1) + ".png"

                # Load from absolute path and scale
                Image = pygame.image.load(os.path.join(os.path.dirname(__file__), ImagePath)).convert_alpha()
                Image = pygame.transform.scale(Image, Configs['ImageDimensions'])

                Images.append(Image)

            # Save images
            Configs['Images'] = Images

            ###########################
            #### Load Button Image ####
            ###########################

            # Image path relative to this file
            ImagePath = "Images/Tower/" + Name + "/Button.png"

            # Load from absolute path and scale
            Image = pygame.image.load(os.path.join(os.path.dirname(__file__), ImagePath)).convert_alpha()
            Image = pygame.transform.scale(Image, Configs['ButtonImageDimensions'])

            # Save image
            Configs['ButtonImage'] = Image