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


def corners_on(grid: List[List[chr]]):
    max_h = len(grid) - 1
    max_w = len(grid[0]) - 1
    grid[0][0] = "#"
    grid[0][max_w] = "#"
    grid[max_h][0] = "#"
    grid[max_h][max_w] = "#"

    return grid


def get_grid(lines: List[str], corners_always_on: bool = False) -> List[List[chr]]:
    grid = list()
    for index in range(100):
        grid.append(list(lines[index]))

    if corners_always_on:
        grid = corners_on(grid)

    return grid


def flip(grid: List[List[chr]], corners_always_on: bool = False):
    max_len = len(grid[0])

    new_grid = list()
    for x in range(max_len):
        icos = list()
        for y in range(max_len):
            neighbours = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 == j:
                        pass
                    elif x + i < 0 or y + j < 0 or x + i >= max_len or y + j >= max_len:
                        pass
                    else:
                        neighbours += int(grid[x + i][y + j] == "#")

            new_ico = "."
            current = grid[x][y]
            if current == "#" and 2 <= neighbours <= 3:
                new_ico = "#"
            elif current == "." and neighbours == 3:
                new_ico = "#"

            icos.append(new_ico)
        new_grid.append(icos)
    if corners_always_on:
        new_grid = corners_on(new_grid)

    return new_grid


def main():
    lines = helpers.get_lines(r"../data/day_18.txt")
    grid = get_grid(lines)

    for _ in range(100):
        grid = flip(grid)
    part01 = sum([g.count("#") for g in grid])
    assert part01 == 821

    grid = get_grid(lines, corners_always_on=True)
    for _ in range(100):
        grid = flip(grid, corners_always_on=True)
    part02 = sum([g.count("#") for g in grid])
    assert part02 == 886


if __name__ == "__main__":
    # import cProfile
    # cProfile.run("main()")
    main()
