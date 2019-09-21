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


def get_distinct_molecules(key: str, db: Dict[str, List[str]]) -> List[str]:
    results = list()

    for k, v in db.items():
        for text in v:

            current = key.find(k)
            while current >= 0:
                new_key = ''.join([key[:current], key[current:].replace(k, text, 1)])
                if new_key not in results:
                    results.append(new_key)
                current = key.find(k, current + 1)

    return results


def fabricate_molecule(db: Dict[str, List[str]], target: str) -> List[str]:
    ...


def parse_lines(lines: List[str]):
    key = lines.pop(len(lines)-1)
    db = dict()
    for line in lines:
        if not line:
            continue

        k, _, v = line.split()
        if k not in db:
            db[k] = list()
        db[k].append(v)

    return key, db


def main():
    lines = helpers.get_lines(r"../data/day_19.txt")
    key, db = parse_lines(lines)
    part01 = get_distinct_molecules(key, db)
    assert len(part01) == 535


if __name__ == "__main__":
    main()
