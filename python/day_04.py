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

import hashlib
from functools import partial
from multiprocessing import Pool
from typing import Optional


def get_md5_needle(prefix: str, d_max: int, needle: int) -> Optional[int]:
    current = f"{prefix}{needle}".encode()

    m = hashlib.md5()
    m.update(current)
    result = m.digest()
    if result[0] == result[1] == 0 and result[2] < d_max:
        return needle

    return None


def get_advent_coin_threaded(prefix: str, leading: str, start_at: int = 1) -> hex:
    # using bytes to compare the 3rd byte may or may not need to be
    # less than the first flip to two places.  So anything up to 9
    d_max = 10 if len(leading) == 5 else 1

    # Providing some defaults for the loop
    increase_by = 1_000_000
    numbers = range(start_at, increase_by)

    # need to use partial to setup the multiprocess pool .map function.
    # The .map was by far the fastest -- shaving approx. 4s from the time.
    func = partial(get_md5_needle, prefix, d_max)

    while True:
        # More than four didn't appear to make a difference, less than four increased time.
        # One second faster for each increase to 4
        with Pool(4) as p:
            for result in p.map(func, numbers):
                if result is not None:
                    return result
        start_at += increase_by
        numbers = range(start_at, start_at + increase_by)


def get_advent_coin(prefix: str, leading: str, start_at: int = 1) -> hex:

    # using bytes to compare the 3rd byte may or may not need to be
    # less than the first flip to two places.  So anything up to 9
    d_max = 10 if len(leading) == 5 else 1

    # Caching the function call reduces time by 1s on my laptop
    md5 = hashlib.md5

    index = start_at
    while True:
        current = f"{prefix}{index}"

        m = md5()
        m.update(current.encode())
        result = m.digest()
        if result[0] == result[1] == 0 and result[2] < d_max:
            return index

        index += 1


def main():
    part1 = get_advent_coin_threaded("iwrupvqb", leading="00000")
    assert part1 == 346386, f"Got Part1: {part1}"
    # print("Part01:", part1)

    part2 = get_advent_coin_threaded("iwrupvqb", leading="000000", start_at=part1)
    assert part2 == 9958218, f"Got Part2: {part2}"
    # print("Part02:", part2)


if __name__ == "__main__":
    import cProfile

    cProfile.run("main()")
    # main()
