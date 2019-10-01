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

from __future__ import annotations

from collections import deque
from typing import NamedTuple, Tuple, Optional, Set, List


class Effect(NamedTuple):
    name: str
    turns: int
    armor: int
    damage: int
    mana: int


class Spell(NamedTuple):
    name: str
    cost: int
    damage: int
    heal: int
    effect: Optional[Tuple]


class Character:
    def __init__(self, name: str, hit_points: int, mana: int, damage: int, armor: int):
        self.name: str = name
        self.hit_points: int = hit_points
        self.mana: int = mana
        self.damage: int = damage
        self.armor: int = armor

        self.spells: Set[Spell] = set()
        self.spent: int = 0


class GameState:
    def __init__(self, boss: Character, player: Character, spells: Set[Spell]) -> None:
        self.boss = boss
        self.player = player
        self.spells = spells

    def __str__(self):
        text = [
            f"{s.effect.name} deals {s.effect.damage}; its timer is now {s.effect.turns}"
            for s in self.boss.spells
        ]

        return (
            f" - Player has {self.player.hit_points} hit points, {self.player.armor} armor, {self.player.mana} mana",
            f" - Boss has {self.boss.hit_points} hit points",
            *text,
            f"Boss attacks for {self.boss.damage - self.player.armor} damage.",
        )

    def goal_test(self) -> bool:
        if self.boss.hit_points <= 0:
            return True
        return False

    def is_legal(self) -> bool:
        if self.player.mana < min(s.cost for s in self.spells):
            return False

        if self.player.hit_points <= 0:
            return False

        return True

    def successors(self) -> List[Optional[Spell]]:
        items: List[Spell] = []
        for spell in self.spells:
            if spell.cost <= self.player.mana:

                for boss_spells in self.boss.spells:
                    if boss_spells.effect.turns <= 1:
                        continue

                items.append(spell)

        return items


def main():
    spells = {
        Spell("Magic Missile", cost=53, damage=4, heal=0, effect=None),
        Spell("Drain", cost=73, damage=2, heal=2, effect=None),
        Spell(
            "Shield",
            cost=113,
            damage=0,
            heal=0,
            effect=Effect("Shield Effect", turns=6, armor=7, damage=0, mana=0),
        ),
        Spell(
            "Poison",
            cost=173,
            damage=0,
            heal=0,
            effect=Effect("Poison Effect", turns=6, armor=0, damage=3, mana=0),
        ),
        Spell(
            "Recharge",
            cost=229,
            damage=0,
            heal=0,
            effect=Effect("Recharge Effect", turns=5, armor=0, damage=0, mana=101),
        ),
    }
    boss = Character("Boss", hit_points=51, mana=0, damage=9, armor=0)
    player = Character("Player", hit_points=50, mana=500, damage=0, armor=0)

    game = GameState(boss=boss, player=player, spells=spells)
    for itm in game.successors():
        print(itm)


class Node:
    def __init__(self, spell: Spell, node: Optional[Node]):
        self.state = spell
        self.parent = node


def bfs(initial, goal_test, successors):
    # frontier is where we've yet to go
    frontier = deque()
    frontier.append(Node(initial, None))  # explored is where we've been

    explored: Set = {initial}

    # keep going while there is more to explore
    while frontier:
        current_node = frontier.pop()
        current_state = current_node.state  # if we found the goal, we're done
        if goal_test(current_state):
            return current_node
        # check where we can go next and haven't explored
        for child in successors(current_state):
            if child in explored:  # skip children we already explored
                continue
            explored.add(child)
            frontier.append(Node(child, current_node))

    return None


if __name__ == "__main__":
    main()
