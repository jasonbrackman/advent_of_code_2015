mod day_01;
mod day_02;
mod day_03;

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

fn main() {
    day_01_run();
    day_02_run();
    day_03_run(); // 4488 too high
}


