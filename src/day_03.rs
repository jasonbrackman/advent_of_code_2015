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

pub fn get_stops(input: &str) -> (i32, HashMap<(i32, i32), i32>) {
    let mut h = 0;
    let mut v = 0;

    let mut hmap: HashMap<(i32, i32), i32> = HashMap::new();
    hmap.entry((h, v)).or_insert( 1);

    for item in input.chars() {
        match item {
            '^' => h += 1,
            '>' => v += 1,
            'v' => h -= 1,
            '<' => v -= 1,
            _ => ()
        }

        let counter = hmap.entry((h, v)).or_insert(0);
        *counter += 1;
    }


    let mut counter = 0;
    for _ in hmap
        .iter()
        .map(|(_, v)|  {
                if *v > 0 {
                    counter += 1 }
            }) {};

    (counter, hmap)
}


pub fn get_stops_with_robo(input: &str) -> i32 {
    // need to split input into odds and evens -- then resend to get_directions()
    let mut odds = Vec::new();
    let mut evens = Vec::new();
    for (index,character) in input.chars().map(|x| x.to_string()).enumerate() {
       match index as i32 % 2 {
           0 => evens.push(character),
           _ => odds.push(character)
       }
    }

    let line1 = odds.join("");
    let line2 = evens.join("");
    let (_, hmap1) = get_stops(&line1);
    let (_, hmap2) = get_stops(&line2);

    let mut counter = 0;
    hmap1.iter().for_each(|(_, y)| if *y > 0 { counter += 1});


    for (k, v) in hmap2.iter() {
        if !hmap1.contains_key(k) && *v > 0 {
            counter += 1;
        }
    }

    counter
}
/// > delivers presents to 2 houses: one at the starting location, and one to the east.
/// ^>v< delivers to 4 houses in a square, including twice to the his starting/ending location.
/// ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.
#[test]
fn test_directions() {
    assert_eq!(get_stops(">").0, 2);
    assert_eq!(get_stops("^>v<").0, 4);
    assert_eq!(get_stops("^v^v^v^v^v").0, 2);
}


/// ^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
/// ^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
/// ^v^v^v^v^v delivers presents to 11 houses, w Santa going one way and Robo-Santa going the other.
#[test]
fn test_directions_with_robo_santa() {
    assert_eq!(get_stops_with_robo("^v"), 3);
    assert_eq!(get_stops_with_robo("^>v<"), 3);
    assert_eq!(get_stops_with_robo("^v^v^v^v^v"), 11);
}