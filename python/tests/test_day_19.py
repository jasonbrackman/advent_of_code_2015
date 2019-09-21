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

from python import day_19


class TestDay19(unittest.TestCase):
    lines = """H => HO\nH => OH\nO => HH\n\nHOH"""

    def test_parse_lines(self):
        key, db = day_19.parse_lines(self.lines.split("\n"))
        self.assertEqual("HOH", key)
        self.assertEqual({"H": ["HO", "OH"], "O": ["HH"]}, db)

    def test_get_permutations(self):
        expected = ["HOOH", "HOHO", "OHOH", "HHHH"]
        key, db = day_19.parse_lines(self.lines.split("\n"))
        results = day_19.get_distinct_molecules(key, db)

        self.assertEqual(expected, results)

    def test_get_molecule_fabrication(self):
        lines = "e => H\ne => O\nH => HO\nH => OH\nO => HH NOTHING"
        _, db = day_19.parse_lines(lines.split("\n"))
        self.assertEqual(["H", "O"], db["e"])


if __name__ == "__main__":
    unittest.main()
