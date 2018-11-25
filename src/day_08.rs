/// "" is 2 characters of code (the two double quotes), but the string contains zero characters.
///
/// "abc" is 5 characters of code, but 3 characters in the string data.
///
/// "aaa\"aaa" is 10 characters of code, but the string itself contains six "a" characters and
/// -> a single, escaped quote character, for a total of 7 characters in the string data.
///
/// "\x27" is 6 characters of code, but the string itself contains just one - an apostrophe ('),
/// -> escaped using hexadecimal notation.

pub fn get_code_character_length(input: &str) -> usize {
    let mut chars: Vec<char> = Vec::new();

    let mut stop_push_for = 0;
    for c in input.chars() {

        if c != ' ' {

            if stop_push_for > 0 {

                if stop_push_for == 1 {
                    if c == 'x' {
                        stop_push_for += 2;
                        chars.push('-')
                    } else if c == '"' || c == '\\'{
                        chars.push(c);
                    }
                }

                stop_push_for -= 1;

            } else if c == '\\' {
                stop_push_for = 1;
            } else if c != '"' {
                chars.push(c);
            }

        }
    }

    input.len() - chars.len()
}

pub fn get_wrapped_code_character_length(input: &str) -> usize {
    let mut chars: Vec<char> = Vec::new();

    // header
    chars.push('"');

    for c in input.chars() {
        if c == '"' || c == '\\' {
            chars.push('\\');
        }
        chars.push(c);
    }

    // footer
    chars.push('"');

    chars.len() - input.len()

}

#[test]
fn test_get_code_character_length() {
    assert_eq!(get_code_character_length("\"abc\""), 2);
    assert_eq!(get_code_character_length("\"ab\\\\c\""), 3);
    assert_eq!(get_code_character_length("\"ab\\x27c\""), 5);
    assert_eq!(get_code_character_length("\"txqnyvzmibqgjs\\xb6xy\\x86nfalfyx\""), 8);
}

#[test]
fn test_get_wrapped_code_character_length() {
    assert_eq!(get_wrapped_code_character_length("\"abc\""), 4);
    assert_eq!(get_wrapped_code_character_length("\"ab\\\\c\""), 6);
    assert_eq!(get_wrapped_code_character_length("\"ab\\x27c\""), 5);
    assert_eq!(get_wrapped_code_character_length("\"\\x27\""), 5);
    assert_eq!(get_wrapped_code_character_length("\"txqnyvzmibqgjs\\xb6xy\\x86nfalfyx\""), 6);
}