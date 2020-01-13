############################
#### Required Libraries ####
############################

# System libs
import pygame
import os
import time
import random
import math
import sys

# Level default definitions
from Source.Config.LevelConfig import *

# Enemies
from Source.Level.Entities.Enemy import *

# Towers
from Source.Level.Entities.Tower import *

########################
#### File Structure ####
########################

# 1 - Level
# 	1.1 - Init
# 	1.2 - Run
#	1.3 - Update
#	1.4 - Draw
#		1.4.1 - Draw Background
#		1.4.2 - Draw Sidebar
#		1.4.3 - Draw Lives
#		1.4.4 - Draw Money
#	1.5 - Delete
#	1.6 - Handle Button Press


##################
#### 1 - Level ####
##################
class Level:
	
	####################
	#### 1.1 - Init ####
	####################
	def __init__(self, Index, ScreenDimensions, Window, FrameRate, Font, Lives, Money):
		"""
		Initializes a level
		
		Arguments:
			Index {String} -- Which level to run
			ScreenDimensions {Integer Tuple} - Screen dimensions
			Window {Pygame Surface} -- Window to draw on
			FrameRate {Integer} -- Maximum amount of fps game runs at
			Font {Pygame font} -- Font used to write on screen
			Lives {Integer} -- Current amount of lives player has
			Money {Integer} -- Current amount of money player has
		"""

		# Screen resolution
		self.ScreenDimensions = ScreenDimensions

		# Background level resolution
		self.BackgroundDimensions = LevelConfigs['BackgroundDimensions']

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
		self.LiveImageDimensions = LevelConfigs['LiveImageDimensions']
		self.LiveImageDrawOffset = LevelConfigs['LiveImageDrawOffset']

		# Money
		self.Money = Money

		# Image to display money
		self.MoneyImage = LevelConfigs['MoneyImage']
		self.MoneyImageDimensions = LevelConfigs['MoneyImageDimensions']
		self.MoneyImageDrawOffset = LevelConfigs['MoneyImageDrawOffset']

		# Sidebar texture
		self.SidebarTexture = LevelConfigs['SidebarTexture']

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

		# DEBUG
		self.Towers.append(Tower(220, 200, 'Wood'))
		self.Towers[0].AddArcher('Legolas')
		self.Towers.append(Tower(50, 150, 'Wood'))
		self.Towers[1].AddArcher('Legolas')
		self.Towers[1].AddArcher('Legolas')

		timer = 0

		# FrameRate counter
		Clock = pygame.time.Clock()

		# Level loop
		Run = True

		while Run:

			# Cap amount of fps
			Clock.tick(self.FrameRate)

			# Handle events
			for Event in pygame.event.get():

				# Get out of level loop if user closes game
				if Event.type == pygame.QUIT:
					Run = False			

				# Check if something's been clicked
				MousePos = pygame.mouse.get_pos()
				if Event.type == pygame.MOUSEBUTTONDOWN:
					self.HandleButtonPress(MousePos)
			
			# DEBUG
			if time.time() - timer >= random.randrange(2, 3):
				timer = time.time()
				self.Enemies.append(Enemy('Arcanine', self.EnemyPath))

			# Update everything
			self.Update()

			# Check if game over
			if self.Lives == 0:
				Run = False
				

	######################
	#### 1.3 - Update ####
	######################
	def Update(self):

		# Draw what needs to be drawn
		self.Draw()

		# Update enemies
		for Enemy in self.Enemies:

			# Delete if dead
			if Enemy.Update(self.Window):
				self.Enemies.remove(Enemy)
			
				# Delete projectiles because target died
				for Tower in self.Towers:
					for Archer in Tower.Archers:
						for Projectile in Archer.Projectiles:
							if Projectile.Target == Enemy:
								Projectile.Target = None

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

		# Draw sidebar
		self.DrawSideBar()

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


	#############################
	#### 1.4.2 - DrawSideBar ####
	#############################
	def DrawSideBar(self):
		"""
		Draw sidebar texture to right of background
		"""

		# Draw sidebar
		self.Window.blit(self.SidebarTexture, (self.BackgroundDimensions[0], 0))


	############################
	#### 1.4.3 - Draw Lives ####
	############################
	def DrawLives(self):
		"""
		Draws live image and amount of lives on screen
		"""

		# Draw Image on top right
		DrawX = self.ScreenDimensions[0] - (self.ScreenDimensions[0] - self.BackgroundDimensions[0])/2 - self.LiveImageDimensions[0]/2
		DrawY = self.LiveImageDrawOffset

		self.Window.blit(self.LiveImage, (DrawX, DrawY))

		# Draw Amount of lives
		TextDimensions = self.Font.size(str(self.Lives))
		TextSurface = self.Font.render(str(self.Lives), False, (0, 0, 0))

		DrawX += math.floor((self.LiveImageDimensions[0] - TextDimensions[0])/2)
		DrawY += math.floor((self.LiveImageDimensions[1]- TextDimensions[1])/2)
		self.Window.blit(TextSurface, (DrawX, DrawY))


	############################
	#### 1.4.4 - Draw Money ####
	############################
	def DrawMoney(self):
		"""
		Draws money image and amount of money on screen
		"""

		# Draw image on top right, below lives
		DrawX = self.ScreenDimensions[0] - (self.ScreenDimensions[0] - self.BackgroundDimensions[0])/2 - self.MoneyImageDimensions[0]/2
		DrawY = self.MoneyImageDrawOffset

		self.Window.blit(self.MoneyImage, (DrawX, DrawY))

		# Draw amount of money
		TextDimensions = self.Font.size(str(self.Money))
		TextSurface = self.Font.render(str(self.Money), False, (0, 0, 0))

		DrawX += math.floor((self.MoneyImageDimensions[0] - TextDimensions[0])/2)
		DrawY += math.floor((self.MoneyImageDimensions[1] - TextDimensions[1])/2)
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
			if(Enemy.X > self.ScreenDimensions[0]):
				self.Lives = max(self.Lives - 1, 0)
				self.Enemies.remove(Enemy)


	#################################
	#### 1.6 - HandleButtonPress ####
	#################################	
	def HandleButtonPress(self, X, Y):
		"""
		Does necessary actions when user clicks on screen
		
		Arguments:
			X {Integer} -- Click position
			Y {Integer} -- Click position
		"""

		# Check if tower has been clicked
		for Tower in self.Towers:
			if Tower.Click(X, Y):
				break