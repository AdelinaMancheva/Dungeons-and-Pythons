import unittest
from hero import Hero
from weapon import Weapon
from spell import Spell


class Test(unittest.TestCase):

    def setUp(self):
        self.w = Weapon("axe", 20)
        self.spell = Spell("love spell", 70, 2, 4)
        self.h = Hero("Arthur", "great", 100, 100, 100, 2, self.w, self.spell)

    def test_hero_init(self):
        self.assertEqual(self.h.get_name(), "Arthur")
        self.assertEqual(self.h.get_title(), "great")
        self.assertEqual(self.h.get_health(), 100)
        self.assertEqual(self.h.get_start_health(), 100)
        self.assertEqual(self.h.get_mana(), 100)
        self.assertEqual(self.h.get_mana_rate(), 2)
        self.assertEqual(self.h.get_weapon(), "axe")

    def test_hero_init(self):
        self.assertEqual(str(self.h), "Arthur great 100 100 2")

    def test_hero_known_as(self):
        self.assertEqual(self.h.known_as(), "Arthur the great")

    def test_hero_is_alive(self):
        self.assertTrue(self.h.is_alive())

    def test_hero_is_dead(self):
        self.assertFalse(self.h.is_dead())

    def test_hero_can_cast(self):
        self.assertTrue(self.h.can_cast())

    def test_hero_take_damage(self):
        self.assertEqual(self.h.take_damage(70), 30)

    def test_hero_take_healing(self):
        self.h.take_damage(70)
        self.assertEqual(self.h.take_healing(20), 50)

    def test_hero_equip(self):
        self.assertEqual(self.h.equip(self.w), "Equipped with axe, damage: 20")

    def test_hero_attack(self):
        self.assertEqual(self.h.attack("weapon"), 20)

if __name__ == '__main__':
    unittest.main()
