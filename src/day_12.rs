extern crate regex;


pub fn search_for_numbers(input: &str) -> i32 {
    let re = regex::Regex::new(r"(-?\d+)").unwrap();

    let results = re
        .find_iter(input)
        .map(|mat| mat.as_str())
        .collect::<Vec<&str>>();

    results
        .iter()
        .map(|x| x.parse::<i32>().unwrap())
        .sum()

}

#[test]
fn test_search_for_numbers(){
    assert_eq!(search_for_numbers("[(\"a\":[-23, 1])"), -22);
}