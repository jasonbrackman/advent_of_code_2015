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

use std::collections::HashMap;

fn get_next(input: &str) -> String {
    let characters = "abcdefghijklmnopqrstuvwxyz".to_string();

    let mut output = "".to_string();

    let mut last = input.len() - 1;

    let mut index = get_index(input, &characters, last);

    let mut next_character = get_next_character(&characters, index);
    output.insert(0, next_character);
    while next_character == 'a' {
        if last > 0 {
            last -= 1;
            index = get_index(input, &characters, last);
            next_character = get_next_character(&characters, index);
            output.insert(0, next_character);
        // println!("{}", output);
        // need to start again but check the next character.
        // if there isn't another character -- we end with the 'a'
        } else {
            output.insert(0, 'z');
            //output.push('a');
            break;
        }
    }

    // need to put back whatever digits are missing...
    for c in input[0..last].chars().rev() {
        output.insert(0, c);
        //println!("backwards - {}", c);
    }
    output
}

fn get_next_character(characters: &str, index: usize) -> char {
    let next_character_index = if index < characters.len() - 1 {
        index + 1
    } else {
        0
    };
    match characters.chars().nth(next_character_index) {
        Some(x) => x,
        None => unimplemented!(),
    }
}

fn get_index(input: &str, characters: &str, last: usize) -> usize {
    characters
        .chars()
        .position(|c| {
            c == match input.chars().nth(last) {
                Some(x) => x,
                None => unimplemented!(),
            }
        })
        .expect("What Happened?")
}

fn contains_duplicated_letter(input: &str, interrupted: usize) -> bool {
    let mut hmap: HashMap<char, usize> = HashMap::new();

    for (c1, c2) in input.chars().zip(input.chars().skip(1 + interrupted)) {
        if c1 == c2 {
            *hmap.entry(c1).or_insert(0) += 1;
        }
    }

    hmap.len() == 2
}

fn contains_three_characters_in_a_row(input: &str) -> bool {
    let characters = "abcdefghijklmnopqrstuvwxyz".to_string();
    for index in 0..input.len() {
        if index + 3 < input.len() && characters.contains(&input[index..index + 3]) {
            return true;
        }
    }
    false
}

pub fn iterate_next_with_rules(start: &str) -> String {
    let mut result = start.to_string();

    let mut ready = false;
    while !ready {
        result = get_next(&result);
        // println!("Current_Result: {}", result);
        ready = !result.contains('i')
            && !result.contains('l')
            && !result.contains('o')
            && contains_duplicated_letter(&result, 0)
            && contains_three_characters_in_a_row(&result);
    }

    result
}

/// 'a', 'b', 'c', ... 'z', 'aa', 'ab', 'ac', ...
///
#[test]
fn test_get_next() {
    assert_eq!(get_next("a"), "b");
    //assert_eq!(get_next("h"), "j"); --> not testing the skipped characters
    assert_eq!(get_next("z"), "za");
    assert_eq!(get_next("aa"), "ab");
    assert_eq!(get_next("azz"), "baa");
}

#[test]
fn test_iterate_test_01() {
    assert_eq!(iterate_next_with_rules("abcdefgh"), "abcdffaa");
}

#[test]
fn test_iterate_test_02() {
    assert_eq!(iterate_next_with_rules("ghijklmn"), "ghjaabcc");
}

#[test]
fn test_contains_three_characters_in_a_row() {
    assert_eq!(contains_three_characters_in_a_row("ghjaabcc"), true);
}
