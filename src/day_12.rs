extern crate regex;
use std::collections::HashMap;

pub fn search_for_red_numbers(input: &str) -> i32 {
    let mut numbers = Vec::new();
    //let mut holder = Vec::new();
    let mut holder_map: HashMap<i32, Vec<char>> = HashMap::new();
    let mut record = 0;
    for c in input.chars() {
        if c == '{' {
            record += 1;
        }

        if record > 0 {
            //holder.push(c);
            holder_map.entry(record).or_insert(Vec::new()).push(c);
        }

        if c == '}' {
            record -= 1;
//            if record == 0 {
//                let buffer: String = holder.iter().collect();
//                if buffer.contains("red") {
//                    // collect all the numbers and add it to the numbers vec
//                    // println!("Holder contains RED!");
//                    numbers.push(search_for_numbers(&buffer));
//                }
//                println!("?? {:?}", buffer);
//                holder.clear();
//
//            }
        }
    }

    /*
    let buffer: String = holder.iter().collect();
    if buffer.contains("red") {
        // collect all the numbers and add it to the numbers vec
        // println!("Holder contains RED!");
        numbers.push(search_for_numbers(&buffer));
    }
    println!("?? {:?}", buffer);
    holder.clear();
    */

    numbers.iter().sum()
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
fn test_search_for_red_02() {
    assert_eq!(search_for_red_numbers("[(\"a\":[-23, 1]xwer{ared23a})"), 23);
}

#[test]
fn test_search_for_red_01() {
    assert_eq!(search_for_red_numbers( "[(asdfadfa{a4r{reddff1as}df})"), 1);
}
//#[test]
//fn test_search_for_numbers_03() {
//    assert_eq!(search_for_numbers("[(\"a\":[-23, 1]xwer{{2}ared23a})"), (-22, 0));
//}