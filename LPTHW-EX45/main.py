# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from sys import exit
from random import randint
from skill import *


you = Hero('pizza')
zombie = Zombie('zombie')
battle = Battle(you, zombie)
battle.play()