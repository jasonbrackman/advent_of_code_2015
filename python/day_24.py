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

from itertools import combinations
from typing import List, Tuple, Any

from python import helpers


def reduce_list(original: List[int], reduce: Tuple[int]) -> List[int]:
    return [n for n in original if n not in reduce]


def can_be_balanced(original_nums: List[int], value: int, buckets: int) -> bool:
    for count in range(1, len(original_nums)):
        for items in combinations(original_nums, count):
            if sum(items) == value:
                new_list = reduce_list(original_nums, items)
                if buckets == 2:
                    if sum(new_list) == value:
                        return True
                else:
                    buckets -= 1
                    return can_be_balanced(new_list, value, buckets)
    return False


def quantum_entanglement_value(items: Tuple[Any]) -> int:
    value = 1

    for item in items:
        value *= item

    return value


def main():
    lines = helpers.get_lines(r"../data/day_24.txt")
    nums = [int(n) for n in lines]

    magic_number = (
        6
    )  # was the smallest brute force that would generate the balanced number
    buckets = 3  # from instructions -- need three equal weighted buckets
    part_01_results = get_smallest_quantum_entanglement_bucket(
        buckets, magic_number, nums
    )
    assert min(part_01_results) == 10439961859

    magic_number = 5  # brute forced this minimum number that makes up the value
    buckets = 4  # from instructions
    part_02_results = get_smallest_quantum_entanglement_bucket(
        buckets, magic_number, nums
    )
    assert min(part_02_results) == 72050269


def get_smallest_quantum_entanglement_bucket(buckets, magic_number, nums):
    part_01_results: List = list()
    balanced = sum(nums) // buckets
    # print("Total sum:", sum(nums), "Looking for:", balanced)
    for items in combinations(nums, magic_number):
        if sum(items) == balanced:
            if can_be_balanced(
                [n for n in nums if n not in items], balanced, buckets=buckets - 1
            ):
                part_01_results.append(quantum_entanglement_value(items))
    return part_01_results


if __name__ == "__main__":
    main()
