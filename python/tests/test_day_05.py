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

from python import day_05


class TestDay05(unittest.TestCase):
    def test_naughty_or_nice_string(self):
        self.assertIs(True, day_05.is_naughty_or_nice_part1("ugknbfddgicrmopn"))
        self.assertIs(True, day_05.is_naughty_or_nice_part1("aaa"))
        self.assertIs(False, day_05.is_naughty_or_nice_part1("jchzalrnumimnmhp"))
        self.assertIs(False, day_05.is_naughty_or_nice_part1("haegwjzuvuyypxyu"))
        self.assertIs(False, day_05.is_naughty_or_nice_part1("dvszwmarrgswjxmb"))

    def test_naughty_or_nice_new(self):
        self.assertIs(True, day_05.is_naughty_or_nice_part2("qjhvhtzxzqqjkmpb"))
        self.assertIs(True, day_05.is_naughty_or_nice_part2("xxyxx"))
        self.assertIs(True, day_05.is_naughty_or_nice_part2("yzsmlbnftftgwadz"))

    def test_naughty_or_nice_new_is_false(self):
        self.assertIs(False, day_05.is_naughty_or_nice_part2("nlbyyywergronmir"))
        self.assertIs(False, day_05.is_naughty_or_nice_part2("uurcxstgmygtbstg"))
        self.assertIs(False, day_05.is_naughty_or_nice_part2("ieodomkazucvgmuy"))

    def test_does_character_repeat_with_interruption(self):
        self.assertIs(True, day_05.is_repeated_with_interuption("vxyx", check=3))
