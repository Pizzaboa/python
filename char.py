# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from sys import exit
from random import randint

class MainGame(object):
	pass

class Char(MainGame):

	hit_point = 30

	atk_power = 5

	armor_level = 2

class Hero(Char):

	def __init__(self, name):
		self.name = name

	hit_point = 20

	atk_power = 3

	armor_level = 2

class Zombie(Char):

	def __init__(self, name):
		self.name = name

	hit_point = 30

	atk_power = 3

	armor_level = 1 