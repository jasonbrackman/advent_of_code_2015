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


def parse_lines(lines: List[str]) -> List[List[str]]:
    parsed = list()
    for line in lines:
        parse = (
            line.strip()
            .replace("->", "=")
            .replace("AND", "&")
            .replace("OR", "|")
            .replace("NOT", "65535 + 1 + ~")
            .replace("RSHIFT", ">>")
            .replace("LSHIFT", "<<")
            .split()
        )
        parsed.append([parse[-1], parse[-2]] + parse[:-2])

    return parsed


def main():
    lines = helpers.get_lines(r"../data/day_07.txt")
    parsed = parse_lines(lines)

    values = collect_values(parsed)

    part1 = values["a"]
    assert part1 == 3176

    values = collect_values(parsed, override={"b": part1})
    part2 = values["a"]
    assert part2 == 14710


def collect_values(parsed, override=None):
    values = dict()

    queue = []
    for parse in parsed:
        lhs, _, *rhs = parse
        if len(rhs) == 1 and rhs[0].isdigit():
            values[lhs] = int(rhs[0])
            queue.append(lhs)
        else:
            values[lhs] = rhs

        if override is not None:
            for k, v in override.items():
                values[k] = v

    while queue:
        needle = queue.pop()
        for k, v in values.items():
            if isinstance(v, list) and needle in v:
                v[v.index(needle)] = values[needle]
                if is_valid(v) is True:
                    as_text = [str(x) for x in v]
                    values[k] = eval("".join(as_text))
                    queue.append(k)
    return values


def is_valid(items: List[str]) -> bool:
    math_ops = {"&", "<<", ">>", "|", "+", "~"}
    if None in items:
        return False
    tests = [i for i in items if i in math_ops or isinstance(i, int) or i.isdigit()]
    return len(tests) == len(items)


if __name__ == "__main__":
    main()
