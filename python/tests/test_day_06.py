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

from python import day_06


class TestDay06(unittest.TestCase):
    def test_grid_create_count(self):
        grid = day_06.Grid(10, 10)
        self.assertEqual(100, grid.count(False))
        self.assertEqual(0, grid.count(True))

    def test_grid_flip_center_four(self):
        grid = day_06.Grid(10, 10)
        grid.flip(True, (4, 4), (5, 5))
        self.assertEqual(4, grid.count(True))

    def test_grid_flip_aoc_tests(self):
        grid = day_06.Grid(1000, 1000)
        grid.flip(True, (0, 0), (999, 999))
        grid.flip("toggle", (0, 0), (999, 0))
        grid.flip(False, (499, 499), (500, 500))
        grid.flip("toggle", (499, 499), (500, 500))
        self.assertEqual(999_000, grid.count(True))

    def test_grid_flip_from_data(self):
        grid = day_06.Grid(1000, 1000)
        grid.flip("toggle", (0, 0), (999, 0))
        self.assertEqual(1000, grid.count(True))

        grid.flip("toggle", (0, 0), (999, 999))
        self.assertEqual(999_000, grid.count(True))


if __name__ == "__main__":
    unittest.main()
