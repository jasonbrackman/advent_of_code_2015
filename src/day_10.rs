extern crate regex;


fn get_count(input: &str, pattern: char) -> i32 {
    let mut counter = 0;
    for item in input.chars() {
        if item == pattern {
            counter += 1;
        } else {
            break;
        }
    }
    counter
}

/// For each character, discover how many times it is repeated and reassemble the string with the
/// repetitions preceeding the actual digit.  For example:
/// -> 21 becomes 1211
/// -> 1211 becomes 111221
pub fn parse_string(input: &str) -> String {

    let mut output = "".to_string();
    let mut items = input.chars().peekable();

    let mut current_index: usize = 0;

    while items.peek() != None {

        let test = items.next().unwrap();
        let number = get_count(&input[current_index..], test);
        current_index += number as usize;

        output.push(number.to_string().parse().unwrap());
        output.push(test.to_owned());

        // skip to next item
        for _ in 0..number-1 {
            items.next();
        }
    }

    output
}

#[test]
fn test_get_next_number() {
    assert_eq!(parse_string("112"), "2112");
    assert_eq!(parse_string("1"), "11");
    assert_eq!(parse_string("11"), "21");
    assert_eq!(parse_string("21"), "1211");
}

