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

/// "" is 2 characters of code (the two double quotes), but the string contains zero characters.
///
/// "abc" is 5 characters of code, but 3 characters in the string data.
///
/// "aaa\"aaa" is 10 characters of code, but the string itself contains six "a" characters and
/// -> a single, escaped quote character, for a total of 7 characters in the string data.
///
/// "\x27" is 6 characters of code, but the string itself contains just one - an apostrophe ('),
/// -> escaped using hexadecimal notation.

pub fn get_code_character_length(input: &str) -> usize {
    let mut chars: Vec<char> = Vec::new();

    let mut stop_push_for = 0;
    for c in input.chars() {

        if c != ' ' {

            if stop_push_for > 0 {

                if stop_push_for == 1 {
                    if c == 'x' {
                        stop_push_for += 2;
                        chars.push('-')
                    } else if c == '"' || c == '\\'{
                        chars.push(c);
                    }
                }

                stop_push_for -= 1;

            } else if c == '\\' {
                stop_push_for = 1;
            } else if c != '"' {
                chars.push(c);
            }

        }
    }

    input.len() - chars.len()
}

pub fn get_wrapped_code_character_length(input: &str) -> usize {
    let mut chars: Vec<char> = Vec::new();

    // header
    chars.push('"');

    for c in input.chars() {
        if c == '"' || c == '\\' {
            chars.push('\\');
        }
        chars.push(c);
    }

    // footer
    chars.push('"');

    chars.len() - input.len()

}

#[test]
fn test_get_code_character_length() {
    assert_eq!(get_code_character_length("\"abc\""), 2);
    assert_eq!(get_code_character_length("\"ab\\\\c\""), 3);
    assert_eq!(get_code_character_length("\"ab\\x27c\""), 5);
    assert_eq!(get_code_character_length("\"txqnyvzmibqgjs\\xb6xy\\x86nfalfyx\""), 8);
}

#[test]
fn test_get_wrapped_code_character_length() {
    assert_eq!(get_wrapped_code_character_length("\"abc\""), 4);
    assert_eq!(get_wrapped_code_character_length("\"ab\\\\c\""), 6);
    assert_eq!(get_wrapped_code_character_length("\"ab\\x27c\""), 5);
    assert_eq!(get_wrapped_code_character_length("\"\\x27\""), 5);
    assert_eq!(get_wrapped_code_character_length("\"txqnyvzmibqgjs\\xb6xy\\x86nfalfyx\""), 6);
}