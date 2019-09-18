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


# Has a growth rate of 1.3~
# there is stabilization in both the start and end of the number, cycling in patterns of three


def look_and_say(num: int) -> int:

    old_num = str(num)
    watch = old_num[0]
    counter = 0

    new_num = list()
    for s in old_num:
        if s == watch:
            counter += 1
        else:
            new_num.extend(str(counter))
            new_num.append(watch)
            counter = 1
            watch = s

    new_num.append(str(counter))
    new_num.append(watch)

    return int("".join(new_num))


def main():
    num = 1113122113

    for i in range(50):
        num = look_and_say(num)

        if i == 39:
            total = len(str(num))
            print("Part01:", total)
        if 39 < i < 49:
            print(f"Still working [{i}]: {len(str(num))}")
        if i == 49:
            total = len(str(num))
            print("Part02:", total)


if __name__ == "__main__":
    # import cProfile
    # cProfile.run("main()")
    main()
