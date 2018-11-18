use std::collections::HashMap;

pub fn get_stops(input: &str) -> (i32, HashMap<(i32, i32), i32>) {
    let mut h = 0;
    let mut v = 0;

    let mut hmap: HashMap<(i32, i32), i32> = HashMap::new();
    hmap.entry((h, v)).or_insert( 1);


    for item in input.chars() {
        match item {
            '^' => { h += 1 },
            '>' => { v += 1 },
            'v' => { h -= 1 },
            '<' => { v -= 1 },
            _ => {}
        }

        let counter = hmap.entry((h, v)).or_insert(0);
        *counter += 1;
    }


    let mut counter = 0;
    for (_, v) in hmap.iter() {
        if *v > 0 {
            counter += 1;
        }
    }

    (counter, hmap)
}


pub fn get_stops_with_robo(input: &str) -> i32 {
    // need to split input into odds and evens -- then resend to get_directions()
    let mut odds = Vec::new();
    let mut evens = Vec::new();
    for c in input.chars().enumerate() {
       match c.0 as i32 % 2 {
           0 => evens.push(c.1.to_string()),
           _ => odds.push(c.1.to_string())
       }
    }

    let line1 = odds.join("");
    let line2 = evens.join("");
    let (_, hmap1) = get_stops(&line1);
    let (_, hmap2) = get_stops(&line2);

//    for (k, _v) in hmap1.into_iter() {
//        if hmap2.contains_key(&k) {
//            hmap1[&k] += hmap2[&k];
//        }
//    }

    let mut counter = 0;
    for (_, v) in hmap1.iter() {
        if *v > 0 {
            counter += 1;
        }
    }

    for (k, v) in hmap2.iter() {
        if hmap1.contains_key(k) == false && *v > 0 {
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