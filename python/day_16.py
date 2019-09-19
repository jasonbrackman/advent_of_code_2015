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

from typing import List, Dict

from python import helpers


def parse_lines(lines: List[str]) -> List[Dict[str, int]]:
    db = list()
    for line in lines:
        _, _, *pairs = line.split()
        entry = dict()
        for index in range(0, len(pairs), 2):
            entry[pairs[index].strip(":")] = int(pairs[index + 1].strip(","))
        db.append(entry)

    return db


def main():
    lines = helpers.get_lines(r"../data/day_16.txt")
    db = parse_lines(lines)

    rules = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1,
    }

    possibles = mfcsam(db, rules)
    part01 = possibles.index(max(possibles)) + 1
    assert part01 == 373

    possibles2 = mfcsam(db, rules, exact=False)
    part02 = possibles2.index(max(possibles2)) + 1
    assert part02 == 260


def mfcsam(db, rules, exact=True):
    possibles = list()
    for entry in db:
        total = 0
        for k, v in rules.items():
            if not exact and k in ["cats", "trees"]:
                if entry.get(k, -1) > v:
                    total += 1
            elif not exact and k in ["pomeranians", "goldfish"]:
                if entry.get(k, 1_000_000) < v:
                    total += 1
            else:
                if entry.get(k, -1) == v:
                    total += 1
        possibles.append(total)

    return possibles


if __name__ == "__main__":
    main()
