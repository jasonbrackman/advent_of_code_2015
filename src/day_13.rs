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

use permutohedron;

struct GuestPair {
    primary: String,
    secondary: String,
    happiness: i64
}

impl GuestPair {
    pub fn new(line: &str) -> GuestPair {
        let mut primary = "";
        let mut secondary= "".to_string();
        let mut is_negative: i64= 0;
        let mut happiness: i64 = 0;

        for (index, word) in line.split(' ').enumerate() {
            match index {
                0 => primary = word,
                2 => is_negative = if word == "lose" { -1 } else { 1 },
                3 => happiness = word.parse::<i64>().unwrap() * is_negative,
                10 =>
                    for c in word.chars() {
                        if c != '.' {
                            secondary.push(c);
                        }
                },
                _ => ()
            }
        }

        GuestPair{primary: primary.to_string(),
                  secondary:secondary.to_string(),
                  happiness}
    }
}

pub fn organize_data(input: &str, include_me: bool) -> i64 {
    let stuff: Vec<GuestPair> = input
        .lines()
        .map(|l| GuestPair::new(l)).collect();

    let mut hmap = HashMap::new();
    let me = "Jason".to_string();
    let mut guests: Vec<String> = Vec::new();
    if include_me {

        guests.push(me.to_string());
    }


    for item in stuff.iter() {
        hmap.entry((item.primary.to_string(), item.secondary.to_string())).or_insert(item.happiness);
        if include_me {
            hmap.entry((item.primary.to_string(), me.to_string())).or_insert(0);
            hmap.entry((me.to_string(), item.secondary.to_string())).or_insert(0);
        }

        if !guests.contains(&item.primary) {
            guests.push(item.primary.to_string());
        }
        if !guests.contains(&item.secondary) {
            guests.push(item.secondary.to_string())};
        }


    // generate all combinations
    let mut permutations = Vec::new();
    permutohedron::heap_recursive(&mut guests, |permutation| {
        permutations.push(permutation.to_vec())
    });


    let mut best_score = -500;
    for p in permutations.iter() {
        let mut temp = p.clone();
        temp.push(p[0].clone());
        let mut score = 0;
        for (name1, name2) in temp.iter().zip(temp[1..].iter()) {
            let x = &hmap[&(name1.to_string(), name2.to_string())];
            let y= &hmap[&(name2.to_string(), name1.to_string())];

            // println!("{}-{}={}", name1, name2, x);
            // println!("{}-{}={}", name2, name1, y);
            score = score + *x + *y;
        }

        if score > best_score {
            best_score = score;
        }
        // println!("Total Score: {}: {:?}", score, p);
    }

    // println!("Part_a: {}", best_score);

    best_score

}

#[test]
fn test_get_guests_pairs_and_scores() {
    let input = "Alice would gain 2 happiness units by sitting next to Carol.\nCarol would lose 35 happiness units by sitting next to Alice.\nGeorge would gain 15 happiness units by sitting next to Alice.";
    let mut stuff = Vec::new();

    for line in input.lines() {
        stuff.push(GuestPair::new(line));
    }
    for item in stuff.iter() {
        println!("{}", item.primary);
    };
    // assert_eq!(get_guests_pairs_and_scores(input), ["Carol", "Alice", "George"]);

}
