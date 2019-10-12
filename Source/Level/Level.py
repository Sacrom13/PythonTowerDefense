############################
#### Required Libraries ####
############################

# System libs
import pygame
import os
import time
import random
import math

# Level Default Definitions
from Source.Level.LevelConfig import *

# Resources
from Source.Resources.Resources import *

# Enemies
from Source.Enemy.Enemy import *

# Towers
from Source.Tower.Tower import *

########################
#### File Structure ####
########################

# 1 - Level
# 	1.1 - Init
# 	1.2 - Run
#	1.3 - Update
#	1.4 - Draw
#		1.4.1 - Draw Background
#		1.4.2 - Draw Lives
#		1.4.3 - Draw Money
#	1.5 - Delete


##################
#### 1 - Level ####
##################
class Level:
	
	####################
	#### 1.1 - Init ####
	####################
	def __init__(self, Index, ScreenWidth, ScreenHeight, Window, FrameRate, Font, Lives, Money):
		"""
		Initializes a level
		
		Arguments:
			Index {String} -- Which level to run
			ScreenWidth {Integer} -- Screen width
			ScreenHeight {Integer} -- Screen height
			Window {Pygame Surface} -- Window to draw on
			FrameRate {Integer} -- Maximum amount of fps game runs at
			Font {Pygame font} -- Font used to write on screen
			Lives {Integer} -- Current amount of lives player has
			Money {Integer} -- Current amount of money player has
		"""

		# Screen resolution
		self.ScreenWidth = ScreenWidth
		self.ScreenHeight = ScreenHeight

		# Window
		self.Window = Window

		# FrameRate
		self.FrameRate = FrameRate

		# Font to write text with
		self.Font = Font

		# Lives
		self.Lives = Lives

		# Image to display lives
		self.LiveImage = LevelConfigs['LiveImage']
		self.LiveImageWidth, self.LiveImageHeight = LevelConfigs['LiveImageDimensions']
		self.LiveImageXOffset, self.LiveImageYOffset = LevelConfigs['LiveImageDrawOffsets']

		# Money
		self.Money = Money

		# Image to display money
		self.MoneyImage = LevelConfigs['MoneyImage']
		self.MoneyImageWidth, self.MoneyImageHeight = LevelConfigs['MoneyImageDimensions']
		self.MoneyImageXOffset, self.MoneyImageYOffset = LevelConfigs['MoneyImageDrawOffsets']

		# Enemy path
		self.EnemyPath = LevelConfigs[Index]['Path']

		# Enemies
		self.Enemies = []

		# Towers 
		self.Towers = []

		# Game background
		self.Background = LevelConfigs[Index]['Background']


	###################
	#### 1.2 - Run ####
	###################
	def Run(self):
		""" 
		Runs the level
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

		# Level loop
		Run = True

		while Run:

			# Cap amount of fps
			Clock.tick(self.FrameRate)

			# Handle events
			for Event in pygame.event.get():

				# Get out of level loop
				if Event.type == pygame.QUIT:
					Run = False			

				# Not neccesary for now
				pos = pygame.mouse.get_pos()
				if Event.type == pygame.MOUSEBUTTONDOWN:
					pass
			
			# Add enemies randomly, for now
			if time.time() - timer >= random.randrange(2, 3):
				timer = time.time()
				self.Enemies.append(Enemy('Arcanine', self.EnemyPath))

			# Update everything
			self.Update()


	######################
	#### 1.3 - Update ####
	######################
	def Update(self):

		# Draw what needs to be drawn
		self.Draw()

		# Update enemies
		for Enemy in self.Enemies:
			if Enemy.Update(self.Window):
				self.Enemies.remove(Enemy)

		# Update towers
		for Tower in self.Towers:
			Tower.Update(self.Window, self.Enemies)

		# Delete enemies from the screen
		self.Delete()

		# Update pygame window
		pygame.display.update()
		

	######################
	#### 1.4 - Draw ####
	######################
	def Draw(self):
		"""
		Draws everything required by the game
		"""

		# Draw background
		self.DrawBackground()

		# Draw lives
		self.DrawLives()

		# Draw money
		self.DrawMoney()


	################################
	#### 1.4.1 - DrawBackground ####
	################################
	def DrawBackground(self):
		"""
		Draws level background
		"""

		# Draw background
		self.Window.blit(self.Background, (0,0))


	############################
	#### 1.4.2 - Draw Lives ####
	############################
	def DrawLives(self):
		"""
		Draws live image and amount of lives on screen
		"""

		# Draw Image on top right
		DrawX = self.ScreenWidth - self.LiveImageWidth - self.LiveImageXOffset
		DrawY = self.LiveImageYOffset

		self.Window.blit(self.LiveImage, (DrawX, DrawY))

		# Draw Amount of lives
		TextDimensions = self.Font.size(str(self.Lives))
		TextSurface = self.Font.render(str(self.Lives), False, (0, 0, 0))

		DrawX += math.floor((self.LiveImageWidth - TextDimensions[0])/2)
		DrawY += math.floor((self.LiveImageHeight - TextDimensions[1])/2)
		self.Window.blit(TextSurface, (DrawX, DrawY))


	############################
	#### 1.4.3 - Draw Money ####
	############################
	def DrawMoney(self):
		"""
		Draws money image and amount of money on screen
		"""

		# Draw Image on top right, below lives
		DrawX = self.ScreenWidth - self.MoneyImageWidth - self.MoneyImageXOffset
		DrawY = self.MoneyImageYOffset

		self.Window.blit(self.MoneyImage, (DrawX, DrawY))

		# Draw Amount of Money
		TextDimensions = self.Font.size(str(self.Money))
		TextSurface = self.Font.render(str(self.Money), False, (0, 0, 0))

		DrawX += math.floor((self.MoneyImageWidth - TextDimensions[0])/2)
		DrawY += math.floor((self.MoneyImageHeight - TextDimensions[1])/2)
		self.Window.blit(TextSurface, (DrawX, DrawY))


	######################
	#### 1.5 - Delete ####
	######################
	def Delete(self):
		""" 
		Deletes enemies who are offscreen
		"""

		# Check every enemy
		for Enemy in self.Enemies:

			# If offscreen remove lives and delete enemy
			if(Enemy.X > self.ScreenWidth):
				self.Lives -= 1
				self.Enemies.remove(Enemy)
