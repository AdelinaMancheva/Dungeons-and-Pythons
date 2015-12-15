class Weapon:

    def __init__(self, name, damage):
        self.__name = name
        self.__damage = damage

    def __str__(self):
        return "{} {}".format(self.__name, self.__damage)

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_damage(self):
        return self.__damage

    def set_damage(self, damage):
        self.__damage = damage
