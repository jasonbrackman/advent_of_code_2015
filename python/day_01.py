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

from typing import List, Optional

from python import helpers


def get_floor(lines: List[str], search_floor: Optional[int] = None) -> int:
    options = {"(": 1, ")": -1}

    total = 0
    for line in lines:
        for index, c in enumerate(line, 1):
            total += options[c]
            if search_floor is not None and total == search_floor:
                return index

    return total


def main():
    lines = helpers.get_lines(r"../data/day_01.txt")
    part1 = get_floor(lines)
    part2 = get_floor(lines, -1)
    assert part1 == 232
    assert part2 == 1783
    # print("Part1:", part1)
    # print("Part2:", part2)


if __name__ == "__main__":
    main()
