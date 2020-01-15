############################
#### Required Libraries ####
############################

# System libs
import pygame
import sys

# Game default definitions
from Source.Config.GameConfig import *

# Levels
from Source.Level.Level import *
from Source.Level.Editor.Editor import *

# Resources
from Source.Resources.Resources import *

########################
#### File Structure ####
########################

# 1 - Game
# 	1.1 - Init
#   1.2 - Run


##################
#### 1 - Game ####
##################
class Game:

    ####################
	#### 1.1 - Init ####
	####################
	def __init__(self):
		"""
		Initializes the game
		"""

		# Init pygame
		pygame.init()

		# Screen resolution
		self.ScreenDimensions = GameConfigs['ScreenDimensions']

		# Init game window
		self.Window = pygame.display.set_mode(self.ScreenDimensions)

		# Load game resources
		R = Resources()
		R.LoadGameResources()

		# Loading screen image while waiting for everything to load
		Intro = 0
		while Intro < 2:
			
			for Event in pygame.event.get():
				if Event.type == pygame.QUIT:
					break

			# Draw loading screen
			self.Window.blit(GameConfigs['LoadingImage'], (0,0))
			pygame.display.update()

			pygame.time.Clock().tick(15)
			Intro += 1

		# Load pygame font for writing text
		pygame.font.init()

		# Load remaining resources
		R.LoadRemainingResources()

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
		"""
		Runs the Game
		"""

		# Setup, for now
		# L = Level('1', self.ScreenDimensions, self.Window, self.FrameRate, self.Font, self.Lives, self.Money)
		# L.Run()

		E = Editor(self.ScreenDimensions, self.Window, self.FrameRate, self.Font)
		E.Run()

		# Stop pygame
		pygame.quit()