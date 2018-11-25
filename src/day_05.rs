/// It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
/// It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
/// It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.

fn contains_non_overlapping_repeated_pairs(input: &str) -> bool {
    let mut z = input.chars().peekable();

    while z.peek().is_some() {
        let chunk: String = z.by_ref().take(2).collect();
        if chunk.len() == 2 && input.split(&chunk).count()-1 > 1 {
            return true;
        };
    }

    // try again -- but offset
    z = input.chars().peekable();
    let _z: String = z.by_ref().take(1).collect();
    while z.peek().is_some() {
        let chunk: String = z.by_ref().take(2).collect();
        if chunk.len() == 2 && input.split(&chunk).count()-1 > 1 {
            return true;
        };
    }

    false
}

fn contains_three_vowels(input: &str) -> bool {
    let mut counter = 0;
    for item in "aeiou".chars() {
        let count = input.matches(item).count();
        counter += count;
    }

    counter >= 3
}

fn contains_duplicated_letter(input: &str, interrupted: usize) -> bool {

    let mut counter = 0;
    for (c1, c2) in input.chars().zip(input.chars().skip(1 + interrupted)) {
        if c1 == c2 {
            counter += 1;
        }
    }

    counter >= 1
}

fn contains_bad_combos(input: &str) -> bool {
    let bad = ["ab", "cd", "pq", "xy"];
    for item in bad.iter() {
        if input.contains(item) {
            return true;
        }
    }

    false
}

pub fn follows_all_rules(input: &str) -> bool {
    !contains_bad_combos(input) && contains_three_vowels(input) && contains_duplicated_letter(input, 0)
}

pub fn follows_new_rules(input: &str) -> bool {
    contains_duplicated_letter(input, 1) && contains_non_overlapping_repeated_pairs(input)
}

#[test]
fn test_contains_three_vowels() {
    assert_eq!(contains_three_vowels("aeio"), true);
    assert_eq!(contains_three_vowels("azezio"), true);
    assert_eq!(contains_three_vowels("estyydmzothggudf"), true);
    assert_eq!(contains_three_vowels("aaa"), true);
}

#[test]
fn test_contains_duplicated_letter() {
    assert_eq!(contains_duplicated_letter("abcdefgg", 0), true);
    assert_eq!(contains_duplicated_letter("abcdefgh", 0), false);
    assert_eq!(contains_duplicated_letter("abaca", 1), true);
    assert_eq!(contains_duplicated_letter("zbaca", 1), true);
}

#[test]
fn test_contains_bad_combos() {
    assert_eq!(contains_bad_combos("abcdefgg"), true);
    assert_eq!(contains_bad_combos("aertyouwer"), false);
    assert_eq!(contains_bad_combos("estyydmzothggudf"), false);
}

#[test]
fn test_follows_all_rules() {
    assert_eq!(follows_all_rules("aaiou"), true);
    assert_eq!(follows_all_rules("xyaaiou"), false);
    assert_eq!(follows_all_rules("estyydmzothggudf"), true);
    assert_eq!(follows_all_rules("estyydmzothugg"), true);
}

#[test]
fn test_contains_nonoverlapping_repeating_pairs() {
    assert_eq!(contains_non_overlapping_repeated_pairs("aaa"), false);
    assert_eq!(contains_non_overlapping_repeated_pairs("aabaa"), true);
    assert_eq!(contains_non_overlapping_repeated_pairs("aaaa"), true);
    assert_eq!(contains_non_overlapping_repeated_pairs("ieodomkazucvgmuy"), false);

}