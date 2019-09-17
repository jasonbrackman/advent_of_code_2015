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

from typing import List

from python import helpers

DIRS = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}


def track_visits(directions: List[str]) -> int:
    locations = dict()
    pos = (0, 0)
    locations[pos] = 1  # starting position

    for direction in directions:
        pos = (0, 0)  # reset starting position each time.
        for c in direction:
            pos = (pos[0] + DIRS[c][0], pos[1] + DIRS[c][1])
            if pos in locations:
                locations[pos] += 1
            else:
                locations[pos] = 1

    return len(locations)


def main():
    lines = helpers.get_lines(r"../data/day_03.txt")
    for line in lines:
        part1 = track_visits([line])
        assert part1 == 2592

        visitors = split_list_into_even_odd_directions(line)
        part2 = track_visits(visitors)
        assert part2 == 2360

        # print("Part1:", part1)
        # print("Part2:", part2)


def split_list_into_even_odd_directions(line: str) -> List[str]:
    odds = []
    even = []
    for i, c in enumerate(line):
        if i % 2 == 0:
            even.append(c)
        else:
            odds.append(c)

    return ["".join(even), "".join(odds)]


if __name__ == "__main__":
    main()
