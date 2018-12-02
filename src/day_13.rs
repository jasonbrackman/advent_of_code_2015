use permutohedron;
use std::collections::HashMap;


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

pub fn organize_data(input: &str) {
    let stuff: Vec<GuestPair> = input
        .lines()
        .map(|l| GuestPair::new(l)).collect();

    let mut hmap = HashMap::new();

    let mut guests: Vec<String> = Vec::new();
    for item in stuff.iter() {
        hmap.entry((item.primary.to_string(), item.secondary.to_string())).or_insert(item.happiness);
        // hmap.entry((item.secondary.to_string(), item.primary.to_string())).or_insert(item.happiness);

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
            //println!("{}-{}={}", name2, name1, y);
            score = score + x + y;
        }

        if score > best_score {
            best_score = score;
        }
        // println!("Total Score: {}: {:?}", score, p);
    }

    println!("Part_a: {}", best_score);

    // not 476 & 590 & 725 -- too low?

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
