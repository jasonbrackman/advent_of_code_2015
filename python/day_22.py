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

import copy
from collections import deque
from typing import Optional, Set, List


class Effect:
    def __init__(
        self, name: str, turns: int, armor: int, damage: int, mana: int
    ) -> None:
        self.name: str = name
        self.turns: int = turns
        self.armor: int = armor
        self.damage: int = damage
        self.mana: int = mana


class Spell:
    def __init__(
        self, name: str, cost: int, damage: int, heal: int, effect: Optional[Effect]
    ) -> None:
        self.name: str = name
        self.cost: int = cost
        self.damage: int = damage
        self.heal: int = heal
        self.effect: Optional[Effect] = effect


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
    spells: Set[Spell] = {
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

    is_player_turn_over: bool = False

    def __init__(self, boss: Character, player: Character, hard: bool = False) -> None:
        self.boss = boss
        self.player = player
        self.hard = hard

    def __str__(self):
        text = "\n".join(
            [
                f" => EFFECT: {s.effect.name} deals {s.effect.damage}; its timer is now {s.effect.turns}"
                for s in self.player.spells
                if s.effect is not None
            ]
        )

        turn_owner = "Player" if self.is_player_turn_over else "Boss"

        msg = f" - Boss attacks for {self.boss.damage - self.player.armor} damage."
        if self.is_player_turn_over:
            # Must have finished a round where it was the player's turn
            msg = (
                f" - Player attacks for {self.player.damage - self.boss.armor} damage."
            )

        return (
            f"-- {turn_owner} turn --\n"
            f" - Player has {self.player.hit_points} hit points, {self.player.armor} armor, {self.player.mana} mana\n"
            f" - Boss has {self.boss.hit_points} hit points\n"
            f"{text}\n"
            f"{msg}\n"
            f" - Player spent {self.player.spent}\n"
        )

    def hard_play_should_continue(self) -> bool:
        # For part 2
        if self.hard is True:
            if self.is_player_turn_over is False:
                self.player.hit_points -= 1
                if self.player.hit_points <= 0:
                    return False
        return True

    def take_turn(self, spell: Optional[Spell, str] = None):
        # self.cast_active_spell_effects()

        if spell is not None:
            if isinstance(spell, str):
                spell = next(s for s in self.spells if s.name == spell)
            if isinstance(spell, Spell):
                self.cast_new_spell(spell)
            else:
                raise ValueError(f"Expected a Spell, but got a {type(spell)}!")

        self.is_player_turn_over = not self.is_player_turn_over

    def cast_active_spell_effects(self):
        to_remove = list()

        # Deal all spell effects that are active each turn
        for s in self.player.spells:
            if hasattr(s, "effect") and s.effect is not None:
                # poison
                # print(f"--> Casting poison dmg: {s.effect.damage}")
                self.boss.hit_points -= s.effect.damage

                # Recharge
                # print(f"--> Casting recharge mana: {s.effect.mana}")
                self.player.mana += s.effect.mana

                # Reduce the turns
                s.effect.turns -= 1
                if s.effect.turns <= 0:
                    # Remove one time active boosts from effects
                    # print("--> Removing armor bonus")
                    self.player.armor -= s.effect.armor
                    to_remove.append(s)

        for d in to_remove:
            self.player.spells.remove(d)

    def cast_new_spell(self, spell: Spell):
        if not self.is_player_turn_over:
            self.player.mana -= spell.cost
            self.player.spent += spell.cost

            # Check if its an instant spell or has an effect
            if spell.effect is None:  # instant
                damage = spell.damage - self.boss.armor
                damage = damage if damage > 0 else 1
                self.boss.hit_points -= damage
                self.player.hit_points += spell.heal
            else:
                # Add the one time armor bonus -- will be removed when spell is deleted
                self.player.armor += spell.effect.armor
                self.player.spells.add(spell)

    def goal_test(self, limit: int = 1_000_000) -> bool:
        # part_01 = 900
        # part_02 = 1_241  # 1242 is too high
        # limit = part_01 if self.hard is False else part_02
        if self.boss.hit_points <= 0 and self.player.spent <= limit:
            return True
        return False

    def is_legal(self) -> bool:

        if self.player.mana < min(s.cost for s in self.spells):
            return False

        if self.player.hit_points <= 0:
            return False

        return True

    def boss_turn(self) -> None:
        min_damage = 1
        max_damage = self.boss.damage - self.player.armor
        damage = max(min_damage, max_damage)
        self.player.hit_points -= damage

    def is_spell_ok_to_cast(self, spell: Spell) -> bool:
        for s in self.player.spells:
            # New spells are allowed to start on the same turn that they end.
            if s.name == spell.name and s.effect.turns <= 1:
                return True

        return all(spell.name != s.name for s in self.player.spells)

    def successors(self, limit: int) -> List[Optional[GameState]]:
        items: List[GameState] = []

        if self.hard_play_should_continue() is False:
            return items

        if self.is_player_turn_over:
            # Boss Turn
            temp = copy.deepcopy(self)
            temp.cast_active_spell_effects()
            temp.take_turn()
            if temp.goal_test(limit) is False:
                temp.boss_turn()

            if temp.is_legal():
                items.append(temp)

        else:
            for spell in self.spells:
                # Can't reuse an existing active spell
                if self.is_spell_ok_to_cast(spell):
                    # must be affordable
                    if spell.cost <= self.player.mana:
                        temp = copy.deepcopy(self)
                        temp.cast_active_spell_effects()
                        temp.take_turn(spell=spell)
                        if temp.is_legal():
                            items.append(temp)

        return items


class Node:
    def __init__(self, state: GameState, node: Optional[Node]):
        self.state = state
        self.parent = node


def bfs(initial: GameState, limit: int) -> Optional[List[Spell]]:
    # frontier is where we've yet to go
    frontier = deque()
    frontier.append(Node(initial, None))  # explored is where we've been

    explored: Set = {initial}

    # keep going while there is more to explore
    while frontier:
        current_node = frontier.pop()
        current_state = current_node.state  # if we found the goal, we're done
        if current_state.goal_test(limit):
            return current_node
        # check where we can go next and haven't explored
        for child in current_state.successors(limit):
            if child in explored:  # skip children we already explored
                continue
            explored.add(child)
            frontier.append(Node(child, current_node))

    return None


def main():

    boss = Character("Boss", hit_points=51, mana=0, damage=9, armor=0)
    player = Character("Player", hit_points=50, mana=500, damage=0, armor=0)

    game01 = GameState(boss=boss, player=player, hard=False)
    solution_01: Optional[Node] = bfs(game01, limit=1241)

    game02 = GameState(boss=boss, player=player, hard=True)
    solution_02: Optional[Node] = bfs(game02, limit=1241)
    assert solution_02.state.player.spent == 1216

    if solution_01 is not None:
        assert solution_01.state.player.spent == 900
        print(f"Part_01: {solution_01.state.player.spent}")

    if solution_02 is not None:
        print(f"Part_02: {solution_02.state.player.spent}")


if __name__ == "__main__":
    # import cProfile
    # cProfile.run("main()")
    main()
