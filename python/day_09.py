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

import sys
from itertools import permutations
from typing import List, Dict, Tuple

from python import helpers


def generate_db(lines: List[str]) -> Dict:
    db = dict()
    for line in lines:
        f, _, t, _, distance = line.split()
        db.setdefault(f, dict())
        db.setdefault(t, dict())
        db[f][t] = int(distance)
        db[t][f] = int(distance)

    return db


def get_shortest_distance(db: Dict) -> Tuple[int, int]:

    high_cost = 0
    low_cost = sys.maxsize
    for route in permutations(db.keys()):
        cost = sum([db[a][b] for a, b in zip(route, route[1:])])

        if cost > high_cost:
            high_cost = cost

        if cost < low_cost:
            low_cost = cost

    return low_cost, high_cost


def main():
    lines = helpers.get_lines(r"../data/day_09.txt")
    db = generate_db(lines)
    low, high = get_shortest_distance(db)

    assert low == 117
    assert high == 909


if __name__ == "__main__":
    main()
