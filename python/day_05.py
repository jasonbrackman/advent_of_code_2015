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

from python import helpers


def has_repeating_non_overlapping_pairs(text: str) -> bool:

    pairs = [i + j for i, j in zip(text, text[1:])]
    if len(pairs) != len(set(pairs)):
        for pair in set(pairs):
            if text.replace(pair, "*", 1).find(pair) >= 0:
                return True
    return False


def has_repeating_character(text: str) -> bool:
    evals = False
    for a, b in zip(text, text[1:]):
        if a + b in ["ab", "cd", "pq", "xy"]:
            return False
        if a == b:
            evals = True

    return evals


def is_repeated_with_interuption(text: str, check: int = 3) -> bool:
    for i in range(0, len(text)):
        chunk = text[i : i + check]

        if len(chunk) == check:
            if len(set(chunk)) == 1:
                return True

            result = chunk.split(chunk[check // 2])
            if len(result) == 2 and result[0] == result[1]:
                return True

    return False


def is_naughty_or_nice_part1(text: str) -> bool:
    vowels = [text.count(vowel) for vowel in "aeiou"]
    return sum(vowels) >= 3 and has_repeating_character(text)


def is_naughty_or_nice_part2(text: str) -> bool:
    text = text.strip()
    has_repeating_pairs = has_repeating_non_overlapping_pairs(text)
    same_but_divided = is_repeated_with_interuption(text, check=3)
    result = same_but_divided & has_repeating_pairs

    return result


def main():
    lines = helpers.get_lines(r"../data/day_05.txt")
    part1 = 0
    part2 = 0

    for line in lines:
        if is_naughty_or_nice_part1(line) is True:
            part1 += 1
        if is_naughty_or_nice_part2(line) is True:
            part2 += 1

    assert part1 == 255
    assert part2 == 55

    # print("Part01:", part1)
    # print("Part02:", part2)


if __name__ == "__main__":
    main()
