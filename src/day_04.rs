extern crate md5;


pub fn get_md5_with_prefix(input: &str, leading_zeroes: i32) -> i32 {
    let max = match leading_zeroes % 2 == 0 {
        true => 0,
        false => 9
    };

    for index in 0.. {
        let new_string = [input, &index.to_string()].concat();
        let mut digest = md5::compute(new_string);
        if digest[0] == 0 && digest[1] == 0 && digest[2] <= max {
            return index;
        }
    }
    0
}

///secret key is abcdef, the answer is 609043
#[test]
fn test_leading_five_zeroes() {
    assert_eq!(get_md5_with_prefix("abcdef", 5), 609043);
    assert_eq!(get_md5_with_prefix("pqrstuv", 5), 1048970);
}