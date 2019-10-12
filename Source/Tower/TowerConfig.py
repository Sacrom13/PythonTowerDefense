# Tower Configurations
TowerConfigs = {}


##############
#### Wood ####
##############
Configuration = {
                'ImageDimensions' : (72, 115),      # Image scale
                'TowerTops' : (1/3, 1/8),           # Drawing configurations
                'MaxLevel' : 3,                     # Max level
                'MaxArchers' : 2,                   # Max amount of archers in tower
                'SellMoney' : [0, 0, 0],            # How much tower sells for
                'BuyMoney' : [0, 0, 0],             # How much tower costs to buy
                'Range' : 100,                      # Tower range
                'Images' : None                     # Image, loaded separately
                }

TowerConfigs['Wood'] = Configuration