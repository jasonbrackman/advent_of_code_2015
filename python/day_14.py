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


def parse_lines(lines: List[str]):
    collection = list()
    for line in lines:
        name, _, _, speed, _, _, time_fly, *_, time_pause, _ = line.split()
        collection.append([name, int(speed), int(time_fly), int(time_pause)])
    return collection


def cycle(speed: int, t_go: int, t_stop: int):
    while True:
        for i in range(t_go):
            yield speed
        for i in range(t_stop):
            yield 0


def main():
    lines = helpers.get_lines(r"../data/day_14.txt")

    cycles = {c[0]: cycle(*c[1:]) for c in parse_lines(lines)}
    part01_results = {k: 0 for k in cycles.keys()}
    part02_results = {k: 0 for k in cycles.keys()}

    magic_cycle_number = 2503
    for t in range(magic_cycle_number):
        for k, v in cycles.items():
            # Calculate overall distance scores
            part01_results[k] += next(v)

        current_lead_score = max(part01_results.values())
        for k2, v2 in part01_results.items():
            if v2 == current_lead_score:
                part02_results[k2] += 1

    part01 = max(part01_results.values())
    assert part01 == 2696

    part02 = max(part02_results.values())
    assert part02 == 1084


if __name__ == "__main__":
    main()
