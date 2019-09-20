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

from itertools import combinations
from typing import List

from python import helpers


def get_buckets(items: List[int], value: int):
    results = list()
    for index in range(len(items)):
        for group in combinations(items, index):
            if sum(group) == value:
                results.append(group)

    return results


def main():
    lines = helpers.get_lines(r"../data/day_17.txt")
    items = [int(l) for l in lines]
    buckets = get_buckets(items, 150)
    part01 = len(buckets)
    assert part01 == 1304

    # find the smallest sized grouping
    smallest_size = 1_000_000
    for b in buckets:
        if len(b) < smallest_size:
            smallest_size = len(b)

    # Collect and count the number of buckets using the smallest size
    part02 = len([b for b in buckets if len(b) == smallest_size])

    assert part02 == 18


if __name__ == "__main__":
    main()
