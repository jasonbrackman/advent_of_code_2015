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


def generate_codes(num_start: int = 20151125):
    while True:
        yield num_start
        num_next = num_start * 252533
        num_start = num_next % 33554393


def infinite_grid(max_row: int, max_col: int):
    codes = generate_codes()
    items = dict()
    row = 1
    col = 1
    new_row = row
    while True:

        items[(new_row, col)] = next(codes)
        while col != row:
            new_row -= 1
            col += 1
            items[(new_row, col)] = next(codes)
            if new_row == max_row and col == max_col:
                return items

        row += 1
        new_row = row
        col = 1


def main():
    """
    To continue, please consult the code grid in the manual.
    Enter the code at row 3010, column 3019.
    """
    results = infinite_grid(3010, 3019)
    assert results[(3010, 3019)] == 8997277


if __name__ == "__main__":
    main()
