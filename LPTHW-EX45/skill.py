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

class Dead(MainGame):
	def play(self):
		print "\n僵尸的牙齿深深的咬进了你的脖子,你无助地躺在地上等待死亡."
		print "\nGame Over"
		exit(1)

class Win(MainGame):
	def play(self):
		print "\n你用尽最后一击打碎了僵尸的脑袋,然而这个城市已被僵尸占领,你能在这个末世中生存到何时?"
		print "\nGame Over"
		exit(1)

class Hero(Char):

	def __init__(self, name):
		self.name = name

	hit_point = 20

	atk_power = 3

	armor_level = 2

class Zombie(Char):

	def __init__(self, name):
		self.name = name

	hit_point = 50

	atk_power = 8

	armor_level = 1 

class Battle(Char):
	scene ={'dead':Dead(),
			'win':Win()

			}

	def __init__(self, hero, zombie):
		self.hero = hero #设法将hero实例导入这里
		self.zombie = zombie #设法将僵尸实例导入这里

	def play(self):
		print "\n一觉醒来,你发现城市被莫名病毒感染,周边的市民已变成僵尸,你需要在这个末世中生存下去.\n"
		print "你遇到了一只%s,它蹒跚着向你走来,你将会:\n" % (self.zombie.name)
		return self.play_next()

	def play_next(self):
		print "1.攻击\n"
		print "2.心神凝聚\n" 
		print "3.逃跑\n"
		print "4.使用药草"

		action = raw_input('\n>')

		if action == "1":
			return self.attack()

		elif action == "2":
			return self.buff()

		elif action == "3":
			print "\n你慌不择路逃进了一个死胡同,僵尸朝你步步逼近,你已无路可逃."
			return self.scene['dead'].play()

		elif action == '4':
			print "\n你打开包裹用药草包扎了伤害,生命值恢复了10点.\n"
			self.hero.hit_point = self.hero.hit_point + 10
			return self.play_next2()

		else:
			print "\n请选择正确的行动.\n"
			return self.play_next()

	def play_next2(self):
		print "\n1.攻击\n"
		print "2.逃跑\n"
		print "3.使用药草"

		action = raw_input('\n>')

		if action == "1":
			return self.attack()

		elif action == "2":
			print "\n你慌不择路逃进了一个死胡同,僵尸朝你步步逼近,你已无路可逃.\n"
			return self.scene['dead'].play()

		elif action == '3':
			print "\n你打开包裹用药草包扎了伤害,生命值恢复了10点.\n"
			self.hero.hit_point = self.hero.hit_point + 10
			return self.play_next2()

		else:
			print "\n请选择正确的行动.\n"
			return self.play_next2()

	def buff(self): #buff技能,提升人物属性
		print '\n你深深地吸了一口气,调整了战斗姿势,感觉自己冷静了下来.\n'
		print '你进入心神凝聚状态,攻击力和防御力都有所提升.\n'
		self.hero.atk_power = 5
		self.hero.armor_level = 4
		return self.play_next2()

	def rage(self): #僵尸会在生命底下时狂暴
		print "\n经过几回合的搏斗,僵尸的一只胳膊已经被你打断.\n"
		print "然而你也被抓伤好几处,所幸并没有被咬到."
		print "\n但是僵尸似乎被你伤口渗出的血液所吸引,它的眼神散发着对血肉的渴望,它的动作愈发疯狂"
		print "\n注意:僵尸的属性似乎有所上升,请小心应对."

		self.zombie.atk_power = 15
		self.zombie.armor_level = 2

	def attack(self): #普通攻击
		hero_damage = randint(2, self.hero.atk_power) - self.zombie.armor_level
		zombie_damage = randint(5, self.zombie.atk_power) - self.hero.armor_level

		self.zombie.hit_point = self.zombie.hit_point - hero_damage
		print "\n你对%s发动了普通攻击,造成了%d点伤害.  %s的剩余生命: %d/30" % (self.zombie.name, hero_damage, self.zombie.name, self.zombie.hit_point)

		self.hero.hit_point = self.hero.hit_point - zombie_damage
		print "\n%s对你发动了普通攻击,你受到了%d点伤害.  你的剩余生命: %d/20" % (self.zombie.name, zombie_damage, self.hero.hit_point)

		if self.zombie.hit_point <= 0:
			print "\n%s被打倒了,你气喘吁吁的擦了一把汗." % (self.zombie.name)
			return self.scene['win'].play()
		 
		elif self.hero.hit_point <= 0:
			return self.scene['dead'].play()

		elif self.zombie.hit_point < 11 and self.zombie.hit_point > 8:
			self.rage()

		return self.play_next2()
