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

pub fn what_floor(s: &str) -> i32 {
    s
        .chars()
        .map(|item| match item {
            '(' => 1,
            ')' => -1,
            _ => 0
        })
        .sum()
}

pub fn which_index_is_basement(s: &str) -> i32 {
    let mut total = 0;

    for (index, item) in s.chars().enumerate() {
        match item {
            '(' => total += 1,
            ')' => total -= 1,
            _ => total = total
        }
        if total == -1 {
            return (index + 1) as i32;
        }
    }

    0
}


#[test]
fn day_01_part_a() {
    assert_eq!(what_floor("(())"), 0);
    assert_eq!(what_floor("(()()(()()()())(((((()))))(()()()"), 3)
}

#[test]
fn day_01_part_b() {
    assert_eq!(which_index_is_basement(")"), 1);
    assert_eq!(which_index_is_basement("()())"), 5);
}