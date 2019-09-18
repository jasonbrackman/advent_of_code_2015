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

import string
from typing import List

CHARS = string.ascii_lowercase


def is_valid(tumbler: List[chr]) -> bool:

    # Exit early if contains confusing characters
    if any(i for i in tumbler if i in ["i", "o", "l"]):
        return False

    s1 = "".join(tumbler)

    # Check if two characters match each other; in two non-overlapping sections
    pairs = [(a + b) for a, b in zip(s1, s1[1:]) if a == b]
    if len(pairs) >= 2:
        for pair in pairs:
            if pair in s1:
                s1 = s1.replace(pair, "*", 1)
            else:
                return False
    else:
        return False

    s2 = "".join(tumbler)
    # Is there a sequence of three alphabetical characters.
    for i in range(len(s2)):
        temp = s2[i : i + 3]
        if len(temp) == 3 and temp in CHARS:
            return True

    return False


def increment(tumbler: List[chr], skip_first: bool = False) -> str:

    while is_valid(tumbler) is False or skip_first is True:
        skip_first = False
        for index in reversed(range(0, len(tumbler))):
            current_index = CHARS.index(tumbler[index])
            tumbler[index] = CHARS[(current_index + 1) % 26]
            if tumbler[index] != "a":
                break

    return "".join(tumbler)


def main():
    puzzle = "cqjxjnds"
    part01 = increment(list(puzzle))
    assert part01 == "cqjxxyzz"

    part02 = increment(list(part01), skip_first=True)
    assert part02 == "cqkaabcc"


if __name__ == "__main__":
    main()
