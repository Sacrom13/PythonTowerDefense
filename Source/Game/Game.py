# Required Libs
import pygame

# Game Default Definitions
from Source.Game.GameConfig import *

# Levels
from Source.Level.Level import *

########################
#### File Structure ####
########################

# 1 - Game
# 	1.1 - Init
#   1.2 - Run

class Game:

    ####################
	#### 1.1 - Init ####
	####################
	def __init__(self):
		"""
		Initializes the game
		"""

		# Init Pygame
		pygame.init()

		# Screen Resolution
		self.ScreenWidth, self.ScreenHeight = GameConfigs['ScreenDimensions']

		# Init Game Window
		self.Window = pygame.display.set_mode((self.ScreenWidth, self.ScreenHeight))

		# Load Game Resources
		R = Resources()
		R.LoadGameResources()

		# Loading screen image while waiting for everything to load

		# Loop or pygame doesn't draw
		Intro = 0
		while Intro < 2:
			
			for Event in pygame.event.get():
				if Event.type == pygame.QUIT:
					break

			# Draw Loading screen
			self.Window.blit(GameConfigs['LoadingImage'], (0,0))
			pygame.display.update()

			pygame.time.Clock().tick(15)
			Intro += 1

		# Load pygame Font for writing text
		pygame.font.init()

		# Load remaining resources
		R.LoadArcherResources()
		R.LoadEnemyResources()
		R.LoadLevelResources()
		R.LoadProjectileResources()
		R.LoadTowerResources()

		# Lives
		self.Lives = GameConfigs['StartLives']

		# Money
		self.Money = GameConfigs['StartMoney']

		# Font to write text with
		self.FontSize = GameConfigs['FontSize']
		self.Font = pygame.font.SysFont(GameConfigs['Font'], self.FontSize)

		# FrameRate
		self.FrameRate = GameConfigs['FrameRate']


	###################
	#### 1.2 - Run ####
	###################
	def Run(self):
		L = Level('1', self.ScreenWidth, self.ScreenHeight, self.Window, self.FrameRate, self.Font, self.Lives, self.Money)
		L.Run()