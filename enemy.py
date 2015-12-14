class Enemy:
    def __init__(self, health, mana, damage):
        self._health = health
        self._max_health = health
        self._mana = mana
        self._damage = damage
        self._alive = True
        self._can_cast = True
        self._current_spell = None
        self._current_weapon = None

    def is_alive(self):
        if self._health <= 0:
            self._alive = False
        return self._alive

    def can_cast(self):
        if self._mana <= 0:
            self._can_cast = False
        return self._can_cast

    def get_health(self):
        return self._health

    def get_mana(self):
        return self._mana

    def take_healing(self, healing_points):
        if self._health <= 0:
            return False
        self._health += healing_points
        if self._health > self._max_health:
            self._health = self._max_health
        return True

    def take_mana(self, mana_points):
        return

    def attack(self, by=None):
        if by == "weapon" and self._current_weapon is not None:
            return self._current_weapon.damage()
        if by == "magic" and self._current_spell is not None:
            return self._current_spell.damage()
        return self._damage

    def take_damage(self, damage_points):
        if damage_points <= self._health:
            self._health -= damage_points
        else:
            self._health = 0

    def equip(self, weapon):
        self._current_weapon = weapon

    def learn(self, spell):
        self._current_spell = spell
