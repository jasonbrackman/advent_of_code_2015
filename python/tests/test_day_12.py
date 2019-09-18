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

from python import day_12


class TestDay12(unittest.TestCase):
    def test_drill_down_for_six(self):
        data1 = {"a": 2, "b": 4}
        data2 = [1, 2, 3]
        result1 = sum(i for i in day_12.drill_down(data1))
        result2 = sum(i for i in day_12.drill_down(data2))
        self.assertEqual(6, result1)
        self.assertEqual(6, result2)

    def test_drill_down_for_three(self):
        data1 = [[[3]]]
        data2 = {"a": {"b": 4}, "c": [-1, 4, -4, "a"]}
        result1 = sum(i for i in day_12.drill_down(data1))
        result2 = sum(i for i in day_12.drill_down(data2) if type(i) == int)
        self.assertEqual(3, result1)
        self.assertEqual(3, result2)

    def test_drill_down_for_zero(self):
        data1 = list()
        data2 = dict()
        result1 = sum(i for i in day_12.drill_down(data1))
        result2 = sum(i for i in day_12.drill_down(data2))
        self.assertEqual(0, result1)
        self.assertEqual(0, result2)


if __name__ == "__main__":
    unittest.main()
