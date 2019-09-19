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

from itertools import permutations
from typing import List, Dict, Tuple

from python import helpers


def add_new_guest(db: dict, name: str, default_change: int):
    # add new name to all existing guest relationships
    for k in db.keys():
        if name not in db[k]:
            db[k][name] = default_change

    # add a new named guest
    db[name] = {}
    for k in db.keys():
        db[name][k] = default_change

    # return updated database
    return db


def create_database(lines: List[str]) -> Dict:
    db = dict()

    for line in lines:
        source, target, value = parse_line(line)
        if source not in db:
            db[source] = {}
        db[source][target] = value

    return db


def parse_line(line: str) -> Tuple[str, str, int]:
    source, _, sign, value, *_, target = line.strip(".").split()
    multiplier = -1 if sign == "lose" else 1
    value = int(value) * multiplier
    return source, target, value


def main():
    lines = helpers.get_lines(r"../data/day_13.txt")
    db = create_database(lines)

    happy_bank = get_happiness_results(db)
    part01 = max(happy_bank)
    assert part01 == 733

    db = add_new_guest(db, "Jason", default_change=0)
    happy_bank = get_happiness_results(db)
    part02 = max(happy_bank)
    assert part02 == 725


def get_happiness_results(db):
    happy_bank = list()
    seatings = permutations(db.keys())
    for seating in seatings:
        happiness = 0
        for a, b in zip(seating, seating[1:]):
            happiness += db[a][b]
            happiness += db[b][a]
        happiness += db[seating[0]][seating[-1]]
        happiness += db[seating[-1]][seating[0]]
        happy_bank.append(happiness)
    return happy_bank


if __name__ == "__main__":
    main()
