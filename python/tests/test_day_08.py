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

from python import day_08


class TestDay08(unittest.TestCase):
    def test_get_code_and_characters_test_quotes(self):
        self.assertEqual((2, 0, 4), day_08.get_code_and_characters(r'""'))

    def test_get_code_and_characters_test_quotes_and_string(self):
        self.assertEqual((5, 3, 4), day_08.get_code_and_characters(r'"abc"'))

    def test_get_code_and_characters_test_escape_quote(self):
        self.assertEqual((10, 7, 6), day_08.get_code_and_characters(r'"aaa\"aaa"'))

    def test_get_code_and_characters_test_escape_numbers(self):
        self.assertEqual((6, 1, 5), day_08.get_code_and_characters(r'"\x27"'))


if __name__ == "__main__":
    unittest.main()
