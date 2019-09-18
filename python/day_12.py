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

from typing import Any

from python import helpers


def drill_down(data: Any, ignore=None):
    if isinstance(data, list):
        for v in data:
            if isinstance(v, (dict, list)):
                yield from drill_down(v, ignore=ignore)
            else:
                yield v

    elif isinstance(data, dict):
        if ignore is not None and ignore in data.values():
            raise StopIteration
        for k, v in data.items():
            if isinstance(v, (dict, list)):
                yield from drill_down(v, ignore=ignore)
            else:
                yield v


def main():
    data = helpers.load_json(r"../data/day_12.json")
    part01 = sum(i for i in drill_down(data) if type(i) == int)
    assert part01 == 156366

    part02 = sum(i for i in drill_down(data, ignore="red") if type(i) == int)
    assert part02 == 96852


if __name__ == "__main__":
    main()
