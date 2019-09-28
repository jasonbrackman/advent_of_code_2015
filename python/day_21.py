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

from itertools import combinations
from typing import NamedTuple, Set, Tuple


class Item(NamedTuple):
    name: str
    cost: int
    damage: int
    armor: int


class Character:
    def __init__(self, name: str, hit_points: int, damage: int, armor: int):
        self.name: str = name
        self.hit_points: int = hit_points
        self.damage: int = damage
        self.armor: int = armor


class RPG:

    weapons = [
        Item("Dagger", 8, 4, 0),
        Item("Shortsword", 10, 5, 0),
        Item("Warhammer", 25, 6, 0),
        Item("Longsword", 40, 7, 0),
        Item("Greataxe", 74, 8, 0),
    ]

    armor = [
        Item("None", 0, 0, 0),
        Item("Leather", 13, 0, 1),
        Item("Chainmail", 31, 0, 2),
        Item("Splintmail", 53, 0, 3),
        Item("Bandedmail", 75, 0, 4),
        Item("Platemail", 102, 0, 5),
    ]

    rings = [
        Item("None", 0, 0, 0),
        Item("None", 0, 0, 0),
        Item("Damage +1", 25, 1, 0),
        Item("Damage +2", 50, 2, 0),
        Item("Damage +3", 100, 3, 0),
        Item("Defense +1", 20, 0, 1),
        Item("Defense +2", 40, 0, 2),
        Item("Defense +3", 80, 0, 3),
    ]

    def __init__(self, hitpoints: int):
        self.__starting_hit_points = hitpoints
        self.boss = Character("Boss", hit_points=109, damage=8, armor=2)
        self.hero = Character("Hero", hit_points=0, damage=0, armor=0)
        # self.simulate_all_loadouts()

    def simulate_all_loadouts(self):
        boss_results: Set[int] = set()
        hero_results: Set[int] = set()
        for items in self.get_variations():
            self.update_stats(items)
            while self.hero.hit_points > 0 and self.boss.hit_points > 0:
                for _ in self.attack_round():
                    if self.hero.hit_points <= 0 < self.boss.hit_points:
                        # print(f"Boss Wins: {self.boss.hit_points} to {self.hero.hit_points} => {items}")
                        boss_results.add(self.get_variation_cost(items))
                        break

                    if self.hero.hit_points > 0 >= self.boss.hit_points:
                        # print(f"Hero Wins: {self.hero.hit_points} to {self.boss.hit_points} => {items}")
                        hero_results.add(self.get_variation_cost(items))
                        break

        return min(hero_results), max(boss_results)

    def update_stats(self, load_out: Tuple[Item]) -> None:
        self.boss = Character("Boss", hit_points=109, damage=8, armor=2)
        self.hero.hit_points = self.__starting_hit_points
        self.hero.damage = sum(i.damage for i in load_out)
        self.hero.armor = sum(i.armor for i in load_out)

    def attack_round(self):
        hero_attack = self.hero.damage - self.boss.armor
        hero_attack = hero_attack if hero_attack > 0 else 1
        self.boss.hit_points -= hero_attack
        yield

        boss_attack = self.boss.damage - self.hero.armor
        boss_attack = boss_attack if boss_attack > 0 else 1
        self.hero.hit_points -= boss_attack
        yield

    def get_variation_cost(self, variation: Tuple[Item]) -> int:
        return sum(i.cost for i in variation)

    def get_variations(self) -> Set[Tuple[Item]]:
        # Must buy exactly one weapon
        # Can buy zero OR one armour
        # Can buy zero to 2 rings (but only one of each)

        variations: Set[Tuple[Item]] = set()

        for weapon in self.weapons:
            for armor in self.armor:
                for rings in combinations(self.rings, 2):

                    x: Tuple[Item] = tuple([weapon, armor, rings[0], rings[1]])

                    variations.add(x)

        return variations


def main():
    rpg = RPG(hitpoints=100)
    part01, part02 = rpg.simulate_all_loadouts()
    assert part01 == 111
    assert part02 == 188


if __name__ == "__main__":
    main()
