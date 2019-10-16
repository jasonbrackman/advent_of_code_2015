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
import sys
from collections import deque
from typing import Optional, List


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

        self.spells: List[Spell] = list()
        self.spent: int = 0


class GameState:
    spells: List[Spell] = [
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
    ]

    def __init__(self, boss: Character, player: Character, hard: bool = False) -> None:
        self.boss = boss
        self.player = player
        self.hard = hard
        self.turns = 0

    def is_player_turn(self):
        return self.turns % 2 == 0

    def __str__(self):
        text = "\n".join(
            [
                f" => EFFECT: {s.effect.name} deals {s.effect.damage}; its timer is now {s.effect.turns}"
                for s in self.player.spells
                if s.effect is not None
            ]
        )

        turn_owner = "Boss" if self.is_player_turn() else "Player"

        msg = f" - Boss attacks for {self.boss.damage - self.player.armor} damage."
        if self.is_player_turn() is False:
            # Must have finished a round where it was the player's turn
            msg = (
                f" - Player attacks for {self.player.damage - self.boss.armor} damage."
            )

        return (
            f"-- [{self.turns}] {turn_owner} turn [hard={self.hard}] --\n"
            f" - Player has {self.player.hit_points} hit points, {self.player.armor} armor, {self.player.mana} mana\n"
            f" - Boss has {self.boss.hit_points} hit points\n"
            f" - {text}\n"
            # f"{msg}\n"
            f" - Player spent {self.player.spent}\n"
        )

    def hard_play_should_continue(self) -> bool:
        # For part 2
        if self.hard is True and self.is_player_turn():
            self.player.hit_points -= 1
            if self.player.hit_points <= 0:
                return False
        return True

    def cast_active_spell_effects(self):
        to_remove = list()

        # Deal all spell effects that are active each turn
        for s in self.player.spells:
            if hasattr(s, "effect") and s.effect is not None:
                # poison
                self.boss.hit_points -= s.effect.damage

                # Recharge
                self.player.mana += s.effect.mana

                # Reduce the turns
                s.effect.turns -= 1
                if s.effect.turns <= 0:
                    # Remove one time active boosts from effects
                    self.player.armor -= s.effect.armor
                    to_remove.append(s)

        for d in to_remove:
            self.player.spells.remove(d)

    def cast_new_spell(self, spell: Spell):
        if self.is_player_turn():
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
                self.player.spells.append(spell)

    def goal_test(self, limit: int = sys.maxsize) -> bool:
        # part_01 = 900
        # part_02 = 1_241  # 1242 is too high
        # limit = part_01 if self.hard is False else part_02
        # if self.boss.hit_points <= 0:
        #     print("Is kind of a winner.  Looking for <= {}, but found {}".format(limit, self.player.spent))

        if (
            self.player.hit_points > 0 >= self.boss.hit_points
            and self.player.spent <= limit
        ):
            return True
        return False

    def is_legal(self) -> bool:
        return self.player.hit_points > 0

    def boss_turn(self) -> None:
        min_damage = 1
        max_damage = self.boss.damage - self.player.armor
        damage = max(min_damage, max_damage)
        self.player.hit_points -= damage

    def is_spell_ok_to_cast(self, spell: Spell) -> bool:
        # These are affordable spells
        spells = (s for s in self.player.spells if s.cost <= self.player.mana)

        for s in spells:
            # New spells are allowed to start on the same turn that they end.
            if s.name == spell.name and s.effect.turns <= 1:
                return True

        return all(spell.name != s.name for s in self.player.spells)

    def take_turn_boss(self):
        game_states = list()
        temp = copy.deepcopy(self)
        temp.cast_active_spell_effects()
        if temp.boss.hit_points <= 0:
            # We won -- send this golden nugget back :)
            game_states.append(temp)
        else:
            temp.boss_turn()
            if temp.is_legal():
                temp.turns += 1
                game_states.append(temp)
        return game_states

    def take_turn_player(self):

        # Can only use spells that are OK to cast - cheap enough and non-repeating
        next_spells = [
            spell for spell in self.spells if self.is_spell_ok_to_cast(spell)
        ]

        game_states = list()

        for spell in next_spells:
            if self.player.mana >= spell.cost:
                temp = copy.deepcopy(self)
                temp.cast_active_spell_effects()
                temp.cast_new_spell(spell)
                temp.turns += 1
                game_states.append(temp)

        return game_states

    def successors(self, limit: int) -> List[Optional[GameState]]:
        items: List[GameState] = []

        # ensure we are cutting out early if we have already spent more than the budget
        if self.player.spent >= limit:
            return items

        if self.is_player_turn():
            if self.hard_play_should_continue():
                if self.player.mana >= min(s.cost for s in self.spells):
                    items = self.take_turn_player()
        else:
            items = self.take_turn_boss()

        return items


class Node:
    def __init__(self, state: GameState, node: Optional[Node]):
        self.state = state
        self.parent = node

    def report(self):
        current = self
        collect = [current.state]
        while current.parent is not None:
            current = current.parent
            collect.append(current.state)

        for item in reversed(collect):
            print(item)


def bfs(initial: GameState, limit: int) -> Optional[Node]:
    # frontier is where we've yet to go
    frontier = deque()
    frontier.append(Node(initial, None))

    # keep going while there is more to explore
    while frontier:
        current_node = frontier.pop()
        current_state = current_node.state

        # if we found the goal, we're done
        if current_state.goal_test(limit):
            return current_node
        else:
            # check where we can go next and haven't explored
            for child in current_state.successors(limit):
                frontier.append(Node(child, current_node))

    return None


def get_cheapest_win(game: GameState) -> int:
    lowest_spent_to_win = sys.maxsize
    while True:
        solution: Optional[Node] = bfs(game, limit=lowest_spent_to_win - 1)
        if solution is None:
            break
        else:
            lowest_spent_to_win = solution.state.player.spent
            print(lowest_spent_to_win, f"Hard play [{solution.state.hard}]")
    return lowest_spent_to_win


def main():

    boss = Character("Boss", hit_points=51, mana=0, damage=9, armor=0)
    player = Character("Player", hit_points=50, mana=500, damage=0, armor=0)

    game01 = GameState(boss=boss, player=player, hard=False)
    min_spend_part01 = get_cheapest_win(game01)
    assert min_spend_part01 == 900, "Actual: {}".format(min_spend_part01)

    game02 = GameState(boss=boss, player=player, hard=True)
    min_spend_part02 = get_cheapest_win(game02)
    assert min_spend_part02 == 1216, "Actual: {}".format(min_spend_part02)


if __name__ == "__main__":

    main()
    print("*" * 100)

    # helpers.time_it(main)
