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

import unittest

from python import day_07


class TestDay07(unittest.TestCase):
    def test_parse_line(self):
        texts = """123 -> x
                456 -> y
                x AND y -> d
                x OR y -> e
                x LSHIFT 2 -> f
                y RSHIFT 2 -> g
                NOT x -> h
                NOT y -> i""".split(
            "\n"
        )

        expected = {
            "d": 72,
            "e": 507,
            "f": 492,
            "g": 114,
            "h": 65412,
            "i": 65079,
            "x": 123,
            "y": 456,
        }
        parsed = day_07.parse_lines(texts)
        self.assertEqual(expected, day_07.collect_values(parsed))


if __name__ == "__main__":
    unittest.main()
