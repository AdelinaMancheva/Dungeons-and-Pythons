class Spell:
    def __init__(self, name, damage, mana_cost, cast_range):
        self._name = name
        self._damage = damage
        self._mana_cost = mana_cost
        self._cast_range = cast_range

    def name(self):
        return self._name

    def damage(self):
        return self._damage

    def mana_cost(self):
        return self._mana_cost

    def cast_range(self):
        return this._cast_range

