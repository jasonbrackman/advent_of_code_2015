#  MIT License
#
#  Copyright (c) 2019 Jason Brackman
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

import unittest

from python import day_22


class TestDay22(unittest.TestCase):

    def test_boss_13_hit_points_8_damage(self):
        """player has 10 hit points and 250 mana,
        and that the boss has 13 hit points and 8 damage:"""
        boss = day_22.Character("Boss", hit_points=13, mana=0, damage=8, armor=0)
        player = day_22.Character("Player", hit_points=10, mana=250, damage=0, armor=0)

        game = day_22.GameState(boss=boss, player=player)
        # Player Turn 1
        game.cast_active_spell_effects()
        game.take_turn(spell="Poison")
        self.assertEqual(game.player.hit_points, 10)
        self.assertEqual(game.boss.hit_points, 13)

        # Boss Turn 1
        game.cast_active_spell_effects()
        game.take_turn()
        if game.goal_test() is False:
            game.boss_turn()
        self.assertEqual(game.player.hit_points, 2)
        self.assertEqual(game.boss.hit_points, 10)

        # Player Turn 2
        game.cast_active_spell_effects()
        game.take_turn(spell="Magic Missile")

        # Boss Turn 2
        game.cast_active_spell_effects()
        game.take_turn()
        if game.goal_test() is False:
            game.boss_turn()

        # self.assertLessEqual(game.boss.hit_points, 0)
        # self.assertEqual(game.player.hit_points, 2)

    def test_boss_14_hit_points_8_damage(self):
        boss = day_22.Character("Boss", hit_points=14, mana=0, damage=8, armor=0)
        player = day_22.Character("Player", hit_points=10, mana=250, damage=0, armor=0)

        game = day_22.GameState(boss=boss, player=player)
        # Player Turn 1
        game.cast_active_spell_effects()
        game.take_turn(spell="Recharge")
        self.assertEqual(game.player.hit_points, 10)
        self.assertEqual(game.boss.hit_points, 14)

        # Boss Turn 1
        game.cast_active_spell_effects()
        game.take_turn()
        if game.goal_test() is False:
            game.boss_turn()
        self.assertEqual(game.player.hit_points, 2)
        self.assertEqual(game.boss.hit_points, 14)

        # Player Turn 2
        game.cast_active_spell_effects()
        game.take_turn(spell="Shield")
        self.assertEqual(game.player.hit_points, 2)
        self.assertEqual(game.boss.hit_points, 14)

        # Boss Turn 2
        game.cast_active_spell_effects()
        game.take_turn()
        if game.goal_test() is False:
            game.boss_turn()
        self.assertEqual(game.player.hit_points, 1)
        self.assertEqual(game.boss.hit_points, 14)

        # Player Turn 3
        game.cast_active_spell_effects()
        game.take_turn(spell="Drain")
        self.assertEqual(game.player.hit_points, 3)
        self.assertEqual(game.boss.hit_points, 12)

        # Boss Turn 3
        game.cast_active_spell_effects()
        game.take_turn()
        if game.goal_test() is False:
            game.boss_turn()
        self.assertEqual(game.player.hit_points, 2)
        self.assertEqual(game.boss.hit_points, 12)

        # Player Turn 4
        game.cast_active_spell_effects()
        game.take_turn(spell="Poison")
        self.assertEqual(game.player.hit_points, 2)
        self.assertEqual(game.boss.hit_points, 12)

        # Boss Turn 4
        game.cast_active_spell_effects()
        game.take_turn()
        if game.goal_test() is False:
            game.boss_turn()
        self.assertEqual(game.player.hit_points, 1)
        self.assertEqual(game.boss.hit_points, 9)

        # Player Turn 5
        game.cast_active_spell_effects()
        game.take_turn(spell="Magic Missile")
        self.assertEqual(game.player.hit_points, 1)
        self.assertEqual(game.boss.hit_points, 2)

        # Boss Turn 5
        game.cast_active_spell_effects()
        game.take_turn()
        if game.goal_test() is False:
            game.boss_turn()
        self.assertEqual(game.player.hit_points, 1)
        self.assertEqual(game.boss.hit_points, -1)


if __name__ == "__main__":
    unittest.main()
