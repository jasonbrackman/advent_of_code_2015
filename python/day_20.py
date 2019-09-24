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
import math
from typing import List


def get_divisors(number: int) -> List[int]:
    small_divisors = [
        i for i in range(1, int(math.sqrt(number)) + 1) if number % i == 0
    ]
    large_divisors = [int(number / d) for d in small_divisors if number != d * d]
    return small_divisors + large_divisors


def get_house_value(address: int) -> int:
    return sum(i for i in get_divisors(address)) * 10


def get_house_value_decay(address: int) -> int:
    return sum(i for i in get_divisors(address) if address / i <= 50) * 11


def part_01(seek: int):
    for x in range(0, 1_000_000, 960):
        value = get_house_value(x)
        if value >= seek:
            return x
    return 0


def part_02(seek: int):
    for x in range(0, 1_000_000, 840):
        value = get_house_value_decay(x)
        if value >= seek:
            return x
    return 0


if __name__ == "__main__":
    part_01 = part_01(29_000_000)
    part_02 = part_02(29_000_000)

    assert part_01 == 665280
    assert part_02 == 705600
