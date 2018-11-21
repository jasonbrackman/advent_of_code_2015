mod day_01;
mod day_02;
mod day_03;
mod day_04;
mod day_05;
mod day_06;

use std::fs::File;
use std::io::prelude::*;

fn read(path: &str) -> String {
    let mut f = File::open(path).expect("file not found");

    let mut contents = String::new();
    f.read_to_string(&mut contents).expect("something went wrong reading the file");

    contents
}

fn day_01_run() {
    let path = "data/day_01.txt";
    let data = read(path);
    println!("Day 01: Part A: {}; Part B: {}",
             day_01::what_floor(&data),
             day_01::which_index_is_basement(&data));
}

fn day_02_run() {
    let path = "data/day_02.txt";
    let lines = read(path);

    let mut total = 0;
    for line in lines.split('\n') {
        total = total + day_02::get_dimensions(line);
    }

    let mut ribbon_total = 0;
    for line in lines.split('\n') {
        ribbon_total = ribbon_total + day_02::calculate_bow_length(line);
    }
    println!("Day 02: Part A: {}; Part B: {}", total, ribbon_total);
}

fn day_03_run() {
    let path = "data/day_03.txt";
    let data = read(path);
    let stops = day_03::get_stops(&data);
    let robo_stops = day_03::get_stops_with_robo(&data);
    println!("Day 03: Part A: {}; Part B: {}", stops.0, robo_stops);
}

#[allow(dead_code)]
fn day_04_run() {
    let result1 = day_04::get_md5_with_prefix("iwrupvqb", 5);
    let result2 = day_04::get_md5_with_prefix("iwrupvqb", 6);
    println!("Day 04: Part A: {}; Part B: {}", result1, result2);
}

fn day_05_run() {
    let path = "data/day_05.txt";
    let lines = read(path);

    let mut total_nice = 0;
    let mut total_nice_new = 0;
    for line in lines.split('\n') {
        if day_05::follows_all_rules(line) {
            total_nice += 1;
        }

        if day_05::follows_new_rules(line) {
            total_nice_new +=1;
        }
    }

    println!("Day 05: Part A: {}; Part B: {}", total_nice, total_nice_new);
}

fn day_06_run() {
    let path = "data/day_06.txt";
    let lines = read(path);

    // part A
    let mut board = day_06::Board::new();
    for line in lines.split('\n') {
        let mut args = day_06::process_line(line);
        board.switch(args.0, args.1, args.2);
        board.switch2(args.0, args.1, args.2);
    }
    let result1 = board.count_true_squares();
    let result2 = board.count_true_squares2();

    println!("Day 06: Part A: {}; Part B: {}", result1, result2);
}

fn main() {
    day_01_run(); // Day 01: Part A: 232; Part B: 1783
    day_02_run(); // Day 02: Part A: 1588178; Part B: 3783758
    day_03_run(); // Day 03: Part A: 2592; Part B: 2360
    day_04_run(); // Day 04: Part A: 346386; Part B: 9958218
    day_05_run(); // Day 05: Part A: 255; Part B: 55
    day_06_run(); // Day 06: Part A: 400410; Part B: 15343601
}


