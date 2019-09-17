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

pub struct Circuit {
    pub registers: HashMap<String, u16>,
}

impl Circuit {
    pub fn new() -> Circuit {
        Circuit {
            registers: HashMap::new(),
        }
    }

    // args can be:
    // 1. a register; ie: ab
    // 2. a value; ie: 4
    // 3. bitwise operator; ie: AND, OR, NOT
    // 4. an assignment value ->
    pub fn parse_line(&mut self, input: &str) -> i32 {
        let mut problems = 0;

        let mut args = input
            .split_whitespace()
            .map(str::trim)
            .collect::<Vec<&str>>();

        let rhs = args.pop().unwrap();
        let _ = args.pop(); // remove the ->

        if args.len() == 1 {
            match args[0].parse::<u16>() {
                Ok(n) => *self.registers.entry(rhs.to_string()).or_insert(0) = n,
                Err(_) => {
                    if self.registers.contains_key(args[0]) {
                        *self.registers.entry(rhs.to_string()).or_insert(0) =
                            self.registers[args[0]];
                    } else {
                        problems += 1
                    }
                }
            };
        } else if args.len() == 2 {
            match args[1].parse::<u16>() {
                Ok(n) => *self.registers.entry(rhs.trim().to_string()).or_insert(0) = !n,
                Err(_) => {
                    if self.registers.contains_key(args[1]) {
                        *self.registers.entry(rhs.to_string()).or_insert(0) =
                            !self.registers[args[1]];
                    } else {
                        problems += 1;
                    }
                }
            };
        } else {
            let arg_1 = args[0].parse::<u16>();
            let mut result1 = 0;
            if arg_1.is_ok() {
                result1 = arg_1.unwrap();
            } else if self.registers.contains_key(args[0]) {
                result1 = self.registers[args[0]];
            } else {
                problems += 1;
            }

            let arg_2 = args[2].parse::<u16>();
            let mut result2 = 0;
            if arg_2.is_ok() {
                result2 = arg_2.unwrap();
            } else if self.registers.contains_key(args[2]) {
                result2 = self.registers[args[2]];
            } else {
                problems += 1;
            }

            if problems == 0 {
                *self.registers.entry(rhs.to_string()).or_insert(0) = match args[1] {
                    "AND" => result1 & result2,
                    "OR" => result1 | result2,
                    "LSHIFT" => result1 << result2,
                    "RSHIFT" => result1 >> result2,
                    _ => panic!("Unexpected pattern found ... "),
                };
            }
        }

        problems
    }
}

#[test]
fn test_bitwise_and() {
    let mut circuit = Circuit::new();
    let mut total = -1;
    while total != 0 {
        total = 0;

        total += circuit.parse_line("123 -> x");
        total += circuit.parse_line("456 -> y");
        total += circuit.parse_line("x AND y -> d");
        total += circuit.parse_line("x OR y -> e");
        total += circuit.parse_line("x LSHIFT 2 -> f");
        total += circuit.parse_line("y RSHIFT 2 -> g");
        total += circuit.parse_line("NOT x -> h");
        total += circuit.parse_line("NOT y -> i");
    }
    assert_eq!(circuit.registers["d"], 72);
    assert_eq!(circuit.registers["e"], 507);
    assert_eq!(circuit.registers["f"], 492);
    assert_eq!(circuit.registers["g"], 114);
    assert_eq!(circuit.registers["h"], 65412);
    assert_eq!(circuit.registers["i"], 65079);
    assert_eq!(circuit.registers["x"], 123);
    assert_eq!(circuit.registers["y"], 456);
}

#[test]
fn test_get_parent_values() {
    let mut circuit = Circuit::new();
    let mut total = -1;
    while total != 0 {
        total = 0;
        total += circuit.parse_line("124 -> f");
        total += circuit.parse_line("eo AND f -> gg");
        total += circuit.parse_line("gg OR eo -> z");
        total += circuit.parse_line("9 -> eo");
    }
    assert_eq!(circuit.registers["z"], 9);
}
