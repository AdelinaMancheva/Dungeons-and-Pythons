from weapon import Weapon


class Hero:

    def __init__(self, name, title, health, start_health, mana, mana_rate, curr_weapon, curr_spell):
        self.__name = name
        self.__health = health
        self.__start_health = start_health
        self.__title = title
        self.__mana = mana
        self.__mana_rate = mana_rate
        self.__curr_weapon = curr_weapon
        self.__cur_spell = curr_spell

    def __str__(self):
        return "{} {} {} {} {}".format(self.__name, self.__title, self.__health, self.__mana, self.__mana_rate)

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_health(self):
        return self.__health

    def set_health(self, health):
        self.__health = health

    def get_start_health(self):
        return self.__start_health

    def set_start_health(self, start_health):
        self.__start_health = start_health

    def get_mana(self):
        return self.__mana

    def set_mana(self, mana):
        self.__mana = mana

    def get_mana_rate(self):
        return self.__mana_rate

    def set_mana_rate(self, mana_rate):
        self.__mana_rate = mana_rate

    def get_weapon(self):
        return self.__currr_weapon.get_name()

    def set_weapon(self, weapon):
        self.__curr_weapon = weapon

    def get_spell(self):
        return self.__cur_spell.name()

    def set_spell(self, spell):
        self.__curr_spell = spell

    def known_as(self):
        return "{} the {}".format(self.__name, self.__title)

    def is_alive(self):
        if self.__health > 0:
            return True
        return False

    def is_dead(self):
        if self.__health <= 0:
            return True
        return False

    def can_cast(self):
        if self.__mana > 0:
            return True
        return False

    def take_damage(self, damage_points):
        if self.__health > damage_points:
            self.__health -= damage_points
            return self.__health
        else:
            return False

    def take_healing(self, health_points):
        if self.__health + health_points <= self.__start_health:
            self.__health += health_points
            return self.__health
        else:
            return self.__start_health

    def take_mana(self):
        pass

    def equip(self, weapon):
        return "Equipped with {}, damage: {}".format(self.__curr_weapon.name(), self.__curr_weapon.damage())

    def learn_spell(self, spell):
        return "Learnt spell {}, damage: {}".format(self.__curr_spell.name(), self.__curr_spell.damage())

    def attack(self, by=None):
        if by == "weapon" and self.__curr_weapon is not None:
            return self.__curr_weapon.damage()
        if by == "magic" and self.__curr_spell is not None:
            return self.__curr_spell.damage()
