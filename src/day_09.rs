/// London to Dublin = 464
/// London to Belfast = 518
/// Dublin to Belfast = 141
///
/// The possible routes are therefore:
///
/// Dublin -> London -> Belfast = 982
/// London -> Dublin -> Belfast = 605
/// London -> Belfast -> Dublin = 659
/// Dublin -> Belfast -> London = 659
/// Belfast -> Dublin -> London = 605
/// Belfast -> London -> Dublin = 982

extern crate permutohedron;
use std::collections::HashMap;

pub fn create_nd_array_of_cities(lines: String) -> (i32, i32) {
    let mut hmap: HashMap<(&str, &str), i32> = HashMap::new();

    // part one: Obtain all of the places
    let mut destinations = Vec::new();
    for line in lines.split('\n') {
        let x: Vec<&str> = line.split(' ').map(str::trim).collect();
        if !destinations.contains(&x[0]) {
            destinations.push(x[0]);
        }
        if !destinations.contains(&x[2]) {
            destinations.push(x[2]);
        }
        hmap.insert((x[0], x[2]), x[4].parse::<i32>().unwrap());
        hmap.insert((x[2], x[0]), x[4].parse::<i32>().unwrap());
    }

    // generate all combinations
    let mut permutations = Vec::new();
    permutohedron::heap_recursive(&mut destinations, |permutation| {
        permutations.push(permutation.to_vec())
    });

    let mut scores = Vec::new();
    // calculate each score
    for args in permutations.iter() {

        let mut total = 0;
        for index in 0..args.len()-1 {
            total += hmap[&(args[index], args[index+1])];
        }
        scores.push(total)
    }

    scores.sort();

    (scores[0], scores[scores.len()-1])

}

#[test]
fn test_create_nd_array_of_cities() {
    assert_eq!(
        create_nd_array_of_cities("l to d = 464\nl to b = 518\nd to b = 141".to_string()),
        (605, 982));
}


#[test]
fn test_permutation() {
    let mut data = [1, 2, 3, 4, 5, 6];
    let mut permutations = Vec::new();
    permutohedron::heap_recursive(&mut data, |permutation| {
        permutations.push(permutation.to_vec())
    });

    assert_eq!(permutations.len(), 720);
}
