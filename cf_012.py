# Code Festival - Python Practice 012
# Author : ㄱㄱㅊ
# Title : Making class of game character
# Date : 20-01-16

class Wizard:
    def __init__(self, health = 0, mana = 0, armor = 0):
        self.health = health
        self.mana = mana
        self.armor = armor

    def attack(self):
        print('파이어볼')

x = Wizard(health = 545, mana = 210, armor = 10)
print(x.health, x.mana, x.armor)
x.attack()
