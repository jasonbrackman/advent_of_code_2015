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


use regex;
use serde_json;
use serde_json::Value;

/// iterative example from the 'net to parse an unknown depth/breadth json.
///
fn sum(v: Value, include_red: bool) -> i64 {
    match v {
        Value::Null => 0,
        Value::Bool(_) => 0,
        Value::Number(n) => n.as_i64().unwrap(),
        Value::String(_) => 0,
        Value::Array(v) => v.into_iter().map(|e| sum(e, include_red)).sum(),
        Value::Object(v) => {
            let mut max = 0;
            for v in v.values() {
                if (v == "red") && !include_red {
                    return 0;
                }
                max += sum(v.clone(), include_red);
            }
            return max;
        }
    }

}

pub fn read_json(input: &str) -> i64 {
    let data: Value = match serde_json::from_str(input) {
        Ok(x) => x,
        Err(_) => Value::Null,
    };

    sum(data, false)
}


pub fn search_for_numbers(input: &str) -> i32 {
    let re = regex::Regex::new(r"(-?\d+)").unwrap();

    let results = re
        .find_iter(input)
        .map(|mat| mat.as_str())
        .collect::<Vec<&str>>();

    results.iter().map(|x| x.parse::<i32>()).filter_map(Result::ok).sum()

}

#[test]
fn test_search_for_numbers(){
    assert_eq!(search_for_numbers("[(\"a\":[-23, 1]xwer{ara})"), -22);
}

#[test]
fn test_search_for_numbers_03() {
    assert_eq!(search_for_numbers("[(\"a\":[-23, 1]xwer{{2}ared23a})"), 3);
}