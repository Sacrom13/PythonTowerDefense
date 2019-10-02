# Required Libs
import pygame
import os
import time
import random

# Game Default Definitions
from Source.Game.GameConfig import *

# Resources
from Source.Resources.Resources import *

# Enemies
from Source.Enemy.Enemy import *

# Towers
from Source.Tower.Tower import *

########################
#### File Structure ####
########################

# 1 - Game
# 	1.1 - Init
# 	1.2 - Run
#	1.3 - Update
#	1.4 - Delete


##################
#### 1 - Game ####
##################
class Game:
	
	####################
	#### 1.1 - Init ####
	####################
	def __init__(self, Index):
		"""
		Initializes a Game
		
		Arguments:
			Index {String} -- Which level to run
		"""

		# Init Pygame
		pygame.init()

		# Game Resolution
		self.ScreenWidth, self.ScreenHeight = GameConfigs['ScreenDimensions']

		# Init Game Window
		self.Window = pygame.display.set_mode((self.ScreenWidth, self.ScreenHeight))

		# Load Resources
		R = Resources()
		R.LoadResources()

		# Game Background
		self.Background = LevelConfigs[Index]['Background']

		# Enemy Path
		self.EnemyPath = LevelConfigs[Index]['Path']

		# Enemies
		self.Enemies = []

		# Towers 
		self.Towers = []

		# Lives
		self.Lives = GameConfigs['StartLives']

		# Image to display lives
		self.LiveImage = GameConfigs['LiveImage']
		self.LiveImageWidth, self.LiveImageHeigth = GameConfigs['LiveImageDimensions']

		# Money
		self.Money = GameConfigs['StartMoney']

		# Font to write text with
		pygame.font.init()
		self.Font = pygame.font.SysFont('Comic Sans MS', 40)



	###################
	#### 1.2 - Run ####
	###################
	def Run(self):
		""" 
		Runs the Game
		"""

		# Setup
		self.Towers.append(Tower(220, 200, 'Wood'))
		self.Towers[0].AddArcher('Legolas')
		self.Towers.append(Tower(50, 150, 'Wood'))
		self.Towers[1].AddArcher('Legolas')
		self.Towers[1].AddArcher('Legolas')

		timer = 0

		# FrameRate Counter
		Clock = pygame.time.Clock()

		# Game loop
		Run = True

		while Run:

			# Count Frames
			Clock.tick(GameConfigs['FrameRate'])

			# Handle Events
			for Event in pygame.event.get():

				# Get out of game loop
				if Event.type == pygame.QUIT:
					Run = False			

				# Not neccesary for now
				pos = pygame.mouse.get_pos()
				if Event.type == pygame.MOUSEBUTTONDOWN:
					pass
			
			# Add Enemies randomly, for now
			if time.time() - timer >= random.randrange(2, 3):
				timer = time.time()
				self.Enemies.append(Enemy('Arcanine', self.EnemyPath))

			self.Update()

		# Stop Pygame
		pygame.quit()


	######################
	#### 1.3 - Update ####
	######################
	def Update(self):
		
		# Background
		self.Window.blit(self.Background, (0,0))

		# Lives

		# show live image
		DrawX = self.ScreenWidth - self.LiveImageWidth - 10
		DrawY = 10

		self.Window.blit(self.LiveImage, (self.ScreenWidth - self.LiveImageWidth - 10, 10))

		# show amount of lives
		TextSurface = self.Font.render(str(self.Lives), False, (0, 0, 0))
		self.Window.blit(TextSurface, (DrawX + 13, DrawY + 3))

		# Update Enemies
		for Enemy in self.Enemies:
			if Enemy.Update(self.Window):
				self.Enemies.remove(Enemy)

		# Update Towers
		for Tower in self.Towers:
			Tower.Update(self.Window, self.Enemies)

		# Delete Enemies from the screen
		self.Delete()

		# Update pygame window
		pygame.display.update()
		

	######################
	#### 1.4 - Delete ####
	######################
	def Delete(self):
		""" 
		Deletes enemies who are offscreen
		"""

		for Enemy in self.Enemies:
			if(Enemy.X > self.ScreenWidth):
				self.Enemies.remove(Enemy)
