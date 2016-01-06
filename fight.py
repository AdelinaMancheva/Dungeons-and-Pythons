from hero import Hero
from enemy import Enemy
from dungeon import Dungeon


class Fights:

    def __init__(self, hero, curr_enemy, hero_weapon, hero_spell, enemy_weapon, enemy_spell):
        self.__hero = hero
        self.__curr_enemy = curr_enemy
        self.__hero_weapon = hero_weapon
        self.__hero_spell = hero_spell
        self.__enemy_weapon = enemy_weapon
        self.__enemy_spell = enemy_spell

    def attack_enemy_weapon(self):
        self.__curr_enemy.take_damage(self.__hero_weapon.damage())

    def attack_enemy_spell(self):
        self.__curr_enemy.take_damage(self.__hero_spell.damage())

    def attack_the_enemy(self):
        if self.__hero.hero_attack("Weapon") == True:
            self.attack_enemy_weapon()
        else:
            self.attack_enemy_spell()
