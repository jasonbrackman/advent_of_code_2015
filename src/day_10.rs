extern crate regex;


pub fn get_count(input: &str, pattern: char) -> i32 {
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

//pub fn get_next_number(input: &str) -> String {
//
//
//    let mut temp = '-';
//
//    let mut count: u32 = 1;
//
//    let mut output = "".to_string();
//
//    for item in input.chars() {
//        // deal with a repeat
//        if item == temp {
//            count += 1;
//        } else {
//            if count == 1 {
//                temp = item;
//
//            }
//            if count > 1 {
//                output.push(count.to_string().parse().unwrap());
//                output.push(temp.to_owned());
//                temp = item;
//                count = 1;
//            }
//
//            //temp = item;
//        }
//    }
//
//    output.push(count.to_string().parse().unwrap());
//    output.push(temp.to_owned());
//
//
//    output
//}

#[test]
fn test_get_next_number() {
    assert_eq!(parse_string("112"), "2112");
    assert_eq!(parse_string("1"), "11");
    assert_eq!(parse_string("11"), "21");
    assert_eq!(parse_string("21"), "1211");
}

