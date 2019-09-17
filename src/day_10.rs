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

extern crate regex;


fn get_count(input: &str, pattern: char) -> i32 {
    let mut counter = 0;
    for item in input.chars() {
        if item == pattern {
            counter += 1;
        } else {
            break;
        }
    }
    counter
}

/// For each character, discover how many times it is repeated and reassemble the string with the
/// repetitions preceeding the actual digit.  For example:
/// -> 21 becomes 1211
/// -> 1211 becomes 111221
pub fn parse_string(input: &str) -> String {

    let mut output = "".to_string();
    let mut items = input.chars().peekable();

    let mut current_index: usize = 0;

    while items.peek() != None {

        let test = items.next().unwrap();
        let number = get_count(&input[current_index..], test);
        current_index += number as usize;

        output.push(number.to_string().parse().unwrap());
        output.push(test.to_owned());

        // skip to next item
        for _ in 0..number-1 {
            items.next();
        }
    }

    output
}

#[test]
fn test_get_next_number() {
    assert_eq!(parse_string("112"), "2112");
    assert_eq!(parse_string("1"), "11");
    assert_eq!(parse_string("11"), "21");
    assert_eq!(parse_string("21"), "1211");
}

