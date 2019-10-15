# Enemy configurations
EnemyConfigs = {}

##################
#### Arcanine ####
##################
Configuration = {                
                'Path' : None,                                          # Path to take through level
                'ImageDimensions' : (40, 40),                           # Image dimensions
                'ImageTypes' : ['Down', 'Left', 'Right', 'Up'],         # Types of movement
                'ImagesPerType' : 4,                                    # How many images per type
                'HealthBarLength' : 50,                                 # Length of health bar
                'HealthBarYOffset' : 10,                                # Health bar offset in y plane
                'MaxHealth' : 5,                                        # Max amount of health
                'Velocity' : 5,                                         # Speed
                'Images' : None,                                        # Images, which are loaded seperately
                'Deviation' : 5                                         # Pixel deviation to make enemies not stack
                }

EnemyConfigs['Arcanine'] = Configuration