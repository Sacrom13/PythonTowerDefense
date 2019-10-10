# Required Libs
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
		Initializes a Level
		
		Arguments:
			Index {String} -- Which level to run
			ScreenWidth {Integer} -- Screen Width
			ScreenHeight {Integer} -- Screen Heigth
			Lives {Integer} -- Current amount of lives player has
			Money {Integer} -- Current amount of money player has
			Font {Pygame Font} -- Font used to write on screen
		"""

		# Screen Resolution
		self.ScreenWidth = ScreenWidth
		self.ScreenHeight = ScreenHeight

		# Window
		self.Window = Window

		# Frame Rate
		self.FrameRate = FrameRate

		# Font to write text with
		self.Font = Font

		# Lives
		self.Lives = Lives

		# Image to display lives
		self.LiveImage = LevelConfigs['LiveImage']
		self.LiveImageWidth, self.LiveImageHeigth = LevelConfigs['LiveImageDimensions']

		# Money
		self.Money = Money

		# Enemy Path
		self.EnemyPath = LevelConfigs[Index]['Path']

		# Enemies
		self.Enemies = []

		# Towers 
		self.Towers = []

		# Game Background
		self.Background = LevelConfigs[Index]['Background']


	###################
	#### 1.2 - Run ####
	###################
	def Run(self):
		""" 
		Runs the Level
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

			# Count Frames
			Clock.tick(self.FrameRate)

			# Handle Events
			for Event in pygame.event.get():

				# Get out of Level loop
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

		# Draw what needs to be drawn
		self.Draw()

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
	#### 1.4 - Draw ####
	######################
	def Draw(self):
		self.DrawBackground()
		self.DrawLives()


	################################
	#### 1.4.1 - DrawBackground ####
	################################
	def DrawBackground(self):
		
		# Draw Background
		self.Window.blit(self.Background, (0,0))


	############################
	#### 1.4.2 - Draw Lives ####
	############################
	def DrawLives(self):
		
		# Offset so lives aren't exactly on the edge
		Offset = 10			

		# Draw Image on top right
		DrawX = self.ScreenWidth - self.LiveImageWidth - Offset
		DrawY = Offset

		self.Window.blit(self.LiveImage, (DrawX, DrawY))

		# Draw Amount of Lives
		TextDimensions = self.Font.size(str(self.Lives))
		TextSurface = self.Font.render(str(self.Lives), False, (0, 0, 0))

		DrawX += math.floor((self.LiveImageWidth - TextDimensions[0])/2)
		DrawY += math.floor((self.LiveImageHeigth - TextDimensions[1])/2)
		self.Window.blit(TextSurface, (DrawX, DrawY))


	######################
	#### 1.5 - Delete ####
	######################
	def Delete(self):
		""" 
		Deletes enemies who are offscreen
		"""

		for Enemy in self.Enemies:
			if(Enemy.X > self.ScreenWidth):
				self.Lives -= 1
				self.Enemies.remove(Enemy)
