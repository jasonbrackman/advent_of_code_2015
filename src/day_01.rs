pub fn what_floor(s: &str) -> i32 {
    s.chars()
        .into_iter()
        .map(|item| match item {
            '(' => 1,
            ')' => -1,
            _ => 0
        })
        .sum()
}

pub fn which_index_is_basement(s: &str) -> i32 {
    let mut total = 0;
    for (index, item) in s.chars().into_iter().enumerate() {
        match item {
            '(' => total = total + 1,
            ')' => total = total - 1,
            _ => total = total
        }
        if total == -1 {
            return index as i32 + 1;
        }
    }

    return 0;
}


#[test]
fn day_01_part_a() {
    assert_eq!(what_floor("(())"), 0);
    assert_eq!(what_floor("(()()(()()()())(((((()))))(()()()"), 3)
}

fn day_01_part_b() {
    assert_eq!(which_index_is_basement(")"), 1);
    assert_eq!(which_index_is_basement("()())"), 5);
}