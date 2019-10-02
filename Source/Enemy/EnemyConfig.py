# Enemy Configs
EnemyConfigs = {}

##################
#### Arcanine ####
##################
Configuration = {                
                'Path' : None,                                          # Path to take through level
                'ImageDimensions' : (40, 40),                           # Image Dimensions
                'ImageTypes' : ['Down', 'Left', 'Right', 'Up'],         # Types of Movement
                'ImagesPerType' : 4,                                    # How many images per type
                'HealthBarLength' : 50,                                 # Length of Health Bar
                'HealthBarYOffset' : 10,                                # Health Bar Offset in Y plane
                'MaxHealth' : 5,                                        # Max Amount of HP
                'Velocity' : 5,                                         # Speed
                'Images' : None                                         # Images, which are loaded seperately
                }

EnemyConfigs['Arcanine'] = Configuration