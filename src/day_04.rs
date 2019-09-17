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

extern crate md5;


pub fn get_md5_with_prefix(input: &str, leading_zeroes: i32) -> i32 {
    let max = if leading_zeroes % 2 == 0 { 0 } else { 9 };

    for index in 0.. {
        let new_string = [input, &index.to_string()].concat();
        let digest = md5::compute(new_string);
        if digest[0] == 0 && digest[1] == 0 && digest[2] <= max {
            return index;
        }
    }
    0
}

///secret key is abcdef, the answer is 609043
#[test]
fn test_leading_five_zeroes() {
    assert_eq!(get_md5_with_prefix("abcdef", 5), 609043);
    assert_eq!(get_md5_with_prefix("pqrstuv", 5), 1048970);
}