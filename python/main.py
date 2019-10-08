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
import time

from python import (
    helpers,
    day_01,
    day_02,
    day_03,
    day_04,
    day_05,
    day_06,
    day_07,
    day_08,
    day_09,
    day_11,
    day_12,
    day_13,
    day_14,
    day_15,
    day_16,
    day_17,
    day_18,
    day_19,
    day_20,
    day_21,
    day_23,
    day_24,
    day_25,
)

if __name__ == "__main__":
    t1 = time.perf_counter()
    args = [
        day_01.main,
        day_02.main,
        day_03.main,
        # day_04.main, # can't be used with the multiprocessor pool
        day_05.main,
        day_06.main,
        day_07.main,
        day_08.main,
        day_09.main,
        # day_10.main,  # takes a long time to run
        day_11.main,
        day_12.main,
        day_13.main,
        day_14.main,
        day_15.main,
        day_16.main,
        day_17.main,
        day_18.main,
        day_19.main,
        day_20.main,
        day_21.main,
        # day_22.main,  # has problems being called -- something to do with deepcopy
        day_23.main,
        day_24.main,
        day_25.main,
    ]

    helpers.time_it_all(args)
    helpers.time_it(day_04.main)

    print(f"Completed Run for 2015 solutions in {time.perf_counter() - t1}s.")
