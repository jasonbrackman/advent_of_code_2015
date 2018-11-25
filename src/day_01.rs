pub fn what_floor(s: &str) -> i32 {
    s.chars()
        .map(|item| match item {
            '(' => 1,
            ')' => -1,
            _ => 0
        })
        .sum()
}

pub fn which_index_is_basement(s: &str) -> i32 {
    let mut total = 0;
    for (index, item) in s.chars().enumerate() {
        match item {
            '(' => total += 1,
            ')' => total -= 1,
            _ => total = total
        }
        if total == -1 {
            return index as i32 + 1;
        }
    }

    0
}


#[test]
fn day_01_part_a() {
    assert_eq!(what_floor("(())"), 0);
    assert_eq!(what_floor("(()()(()()()())(((((()))))(()()()"), 3)
}

#[test]
fn day_01_part_b() {
    assert_eq!(which_index_is_basement(")"), 1);
    assert_eq!(which_index_is_basement("()())"), 5);
}