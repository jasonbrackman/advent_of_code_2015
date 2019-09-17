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

import re

from python import helpers


def get_area(l: int, w: int, h: int) -> int:
    side_a = l * w
    side_b = w * h
    side_c = h * l

    minimum = min(side_a, side_b, side_c)

    return sum((2 * side_a, 2 * side_b, 2 * side_c, minimum))


def get_ribbon(l: int, w: int, h: int) -> int:
    largest = max((l, w, h))
    sides = [l, w, h]
    sides.remove(largest)
    return (sides[0] + sides[0] + sides[1] + sides[1]) + (l * w * h)


def main():
    pattern = r"^(\d+)x(\d+)x(\d+)"
    lines = helpers.get_lines(r"../data/day_02.txt")
    total1 = 0
    total2 = 0
    for line in lines:
        groups = re.search(pattern, line)
        l, w, h = groups.groups()
        total1 += get_area(int(l), int(w), int(h))
        total2 += get_ribbon(int(l), int(w), int(h))

    assert total1 == 1588178
    assert total2 == 3783758
    # print("Part01:", total1)
    # print("Part02:", total2)


if __name__ == "__main__":
    main()
