/*
 * MIT License
 *
 * Copyright (c) 2019 Jason Brackman
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 */

/// A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper
/// plus 6 square feet of slack, for a total of 58 square feet.
///
/// A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper
/// plus 1 square foot of slack, for a total of 43 square feet.

pub fn get_dimensions(input: &str) -> i32 {

    let numbers = input
        .trim_end()
        .split('x')
        .map(|s: &str| s.parse::<i32>().unwrap()).collect::<Vec<i32>>();

    let l = numbers[0];
    let w = numbers[1];
    let h = numbers[2];

    // prepare sides
    let side_01 = l * w;
    let side_02 = w * h;
    let side_03 = h * l;

    // get smallest size
    let mut smallest = side_03;
    for small in [side_01, side_02].iter() {
        if *small < smallest {
            smallest = *small;
        }
    }

    // get total wrapping
    let wrapping = || 2 * side_01 + 2 * side_02 + 2 * side_03;

    // calc total
    wrapping() + smallest

}


/// A present with dimensions 2x3x4 requires 2+2+3+3 = 10 feet of ribbon to wrap the present
/// plus 2*3*4 = 24 feet of ribbon for the bow, for a total of 34 feet.
///
/// A present with dimensions 1x1x10 requires 1+1+1+1 = 4 feet of ribbon to wrap the present
/// plus 1*1*10 = 10 feet of ribbon for the bow, for a total of 14 feet.

pub fn calculate_bow_length(input: &str) -> i32 {

    let numbers: Vec<i32> = input.trim_end().split('x').map(|s| s.parse::<i32>().unwrap()).collect();
    let l = numbers[0];
    let w = numbers[1];
    let h = numbers[2];

    let wrap_size = l * w * h;

    let mut ribbon = 0;
    for item in [l, w, h].iter() {
        ribbon += 2 * item;
    }

    let x = *[l, w, h].iter().max().unwrap();
    ribbon -= 2 * x;

    ribbon + wrap_size

}
#[test]
fn day_02_part_a() {
    assert_eq!(get_dimensions("2x3x4"), 58);
    assert_eq!(get_dimensions("1x1x10"), 43);
}

#[test]
fn day_02_part_b() {
    assert_eq!(calculate_bow_length("4x2x3"), 34);
    assert_eq!(calculate_bow_length("1x1x10"), 14);
    assert_eq!(calculate_bow_length("1x10x10"), 122);
}