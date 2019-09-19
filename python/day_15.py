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

from collections import defaultdict
from itertools import permutations
from typing import List, Dict, Iterator

from python import helpers


def parse_lines(lines: List[str]) -> Dict[str, Dict[str, int]]:
    db = dict()

    for line in lines:
        info = line.split()
        info = [c.strip(":,") for c in info]

        db[info[0]] = {
            info[1]: int(info[2]),
            info[3]: int(info[4]),
            info[5]: int(info[6]),
            info[7]: int(info[8]),
            info[9]: int(info[10]),
        }

    return db


def main():
    lines = helpers.get_lines(r"../data/day_15.txt")
    db = parse_lines(lines)
    part01 = calculate_cookie_score(db)
    assert part01 == 18965440

    part02 = calculate_cookie_score(db, calories=500)
    assert part02 == 15862900


def calculate_cookie_score(db: Dict[str, Dict[str, int]], calories=None) -> int:
    final_totals = list()
    calory_count = list()

    for scores in redistribute(len(db)):
        totals = defaultdict(int)
        for index, (k, v) in enumerate(db.items()):
            totals["calories"] += v["calories"] * scores[index]
            totals["capacity"] += v["capacity"] * scores[index]
            totals["durability"] += v["durability"] * scores[index]
            totals["flavor"] += v["flavor"] * scores[index]
            totals["texture"] += v["texture"] * scores[index]

        # ensure negatives are zero
        for k, v in totals.items():
            if v < 0:
                totals[k] = 0

        # return the total value of cookie (WITHOUT CALORIES)
        if calories is None:
            final_totals.append(
                totals["capacity"]
                * totals["durability"]
                * totals["flavor"]
                * totals["texture"]
            )

        # WITH CALORIES
        elif calories == totals["calories"]:
            final_totals.append(
                totals["capacity"]
                * totals["durability"]
                * totals["flavor"]
                * totals["texture"]
            )

    return max(final_totals)


def redistribute(buckets: int) -> Iterator[List[int]]:
    items = permutations(range(100), buckets)
    balanced = (item for item in items if sum(item) == 100)
    for balance in balanced:
        yield balance


if __name__ == "__main__":
    main()
