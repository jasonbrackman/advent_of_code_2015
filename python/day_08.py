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

from typing import Tuple

from python import helpers


def get_code_and_characters(line: str) -> Tuple[int, int, int]:
    code_count = 0
    char_count = 0
    enco_count = 2

    escape_sequence = list()
    is_code = False
    for c in line:
        if is_code and escape_sequence:
            escape_len = len(escape_sequence)

            if escape_len == 1:
                if c == "\\" or c == '"':
                    enco_count += 1
                    code_count += 1
                    char_count += 1
                    escape_sequence = list()

                elif c == "x":
                    code_count += 1
                    escape_sequence.append(c)

            elif escape_len == 2:
                code_count += 1
                escape_sequence.append(c)

            elif escape_len == 3:
                code_count += 1
                char_count += 1
                escape_sequence = list()

        else:
            if is_code and c == "\\":
                enco_count += 1
                code_count += 1
                escape_sequence.append(c)

            elif c == '"':
                enco_count += 1
                code_count += 1
                is_code = not is_code

            elif is_code:
                code_count += 1
                char_count += 1

    return code_count, char_count, enco_count


def main():
    lines = helpers.get_lines(r"../data/day_08.txt")
    t_code = 0
    t_char = 0
    t_enco = 0
    for line in lines:
        code, char, enco = get_code_and_characters(line)
        t_code += code
        t_char += char
        t_enco += enco
    part1 = t_code - t_char
    part2 = t_enco

    assert part1 == 1350
    assert part2 == 2085


if __name__ == "__main__":
    main()
