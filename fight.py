from hero import Hero
from enemy import Enemy
from dungeon import Dungeon


class Fights:

    def __init__(self, hero, curr_enemy, hero_weapon, hero_spell, enemy_weapon, enemy_spell, dungeon):
        self.__hero = hero
        self.__curr_enemy = curr_enemy
        self.__hero_weapon = hero_weapon
        self.__hero_spell = hero_spell
        self.__enemy_weapon = enemy_weapon
        self.__enemy_spell = enemy_spell
        self.__dungeon = dungeon

    def attack_enemy_weapon(self):
        self.__curr_enemy.take_damage(self.__hero_weapon.damage())

    def attack_enemy_spell(self):
        self.__curr_enemy.take_damage(self.__hero_spell.damage())

    def attack_the_enemy(self):
        if self.__dungeon.hero_attack("Weapon") == True:
            self.attack_enemy_weapon()
        else:
            self.attack_enemy_spell()

    def attack_hero_weapon(self):
        self.__hero.take_damage(self.__enemy_weapon.damage())

    def attack_hero_spell(self):
        self.__hero.take_damage(self.__enemy_spell.damage())

    def __main__(self):
        print("A fight is started between our Hero {} the {} (healh= {}, mana= {} ) and Enemy (health = {}, mana= {}, damage= {} )".format(
            self.__hero.get_name(), self.__hero.get_title(), self.__hero.get_health(), self.__enemy.get_health(), self.__enemy.get_mana(), self.__enemy.get_damage()))
        self.attack_the_enemy()
        print("Hero casts a {}, hits enemy for {}.".format(
            self.__hero_spell, self.__hero_weapon.damage()))
        print("Enemy health is {}".format(self.__enemy.get_health()))

