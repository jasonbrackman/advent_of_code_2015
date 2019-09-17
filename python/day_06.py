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

import re

from python import helpers


class Grid:
    def __init__(self, w: int, h: int):
        self.__width = w
        self.__height = h
        self.grid = self.create_grid()

    def create_grid(self):
        return [[False] * self.__height for _ in range(self.__width)]

    def flip(self, instruction, start, end):
        for x in range(start[0], end[0] + 1):
            for y in range(start[1], end[1] + 1):
                if instruction == "toggle":
                    self.grid[x][y] = not self.grid[x][y]
                else:
                    self.grid[x][y] = instruction

    def intensity(self, instruction, start, end):
        for x in range(start[0], end[0] + 1):
            for y in range(start[1], end[1] + 1):
                if instruction == "toggle":
                    self.grid[x][y] += 2
                elif instruction is True:
                    self.grid[x][y] += 1
                else:
                    self.grid[x][y] -= 1
                    if self.grid[x][y] < 0:
                        self.grid[x][y] = False

    def count(self, position):
        lights = {True: 0, False: 0}

        for x in range(self.__width):
            for y in range(self.__height):
                lights[self.grid[x][y]] += 1

        return lights[position]

    def light_value(self):
        total = 0
        for x in range(self.__width):
            for y in range(self.__height):
                total += self.grid[x][y]
        return total


class Info:
    def __init__(self):
        self.instructions = list()
        self.get_instructions()

    def get_instructions(self):
        pattern = re.compile(r"^.* (\d+),(\d+) through (\d+),(\d+)")

        lines = helpers.get_lines(r"../data/day_06.txt")
        for line in lines:
            items = [None, None, None]

            info = line.strip().split()

            if "off" in info:
                items[0] = False
            elif "on" in info:
                items[0] = True
            elif "toggle" in info:
                items[0] = "toggle"

            matches = re.match(pattern, line)
            items[1] = (int(matches.group(1)), int(matches.group(2)))
            items[2] = (int(matches.group(3)), int(matches.group(4)))

            self.instructions.append(items)


def main():
    grid = Grid(1000, 1000)

    info = Info()
    for instruction, start, end in info.instructions:
        grid.flip(instruction, start, end)

    part01 = grid.count(True)
    assert part01 == 400410

    grid = Grid(1000, 1000)

    info = Info()
    for instruction, start, end in info.instructions:
        grid.intensity(instruction, start, end)

    part02 = grid.light_value()
    assert part02 == 15_343_601


if __name__ == "__main__":
    main()
