
extern crate regex;
extern crate serde_json;
extern crate permutohedron;

use std::thread;
use std::fs::File;
use std::io::prelude::*;
use std::time::Instant;

mod day_01;
mod day_02;
mod day_03;
mod day_04;
mod day_05;
mod day_06;
mod day_07;
mod day_08;
mod day_09;
mod day_10;
mod day_11;
mod day_12;
mod day_13;


fn read(path: &str) -> String {
    let mut f = File::open(path).expect("file not found");

    let mut contents = String::new();
    f.read_to_string(&mut contents).expect("something went wrong reading the file");

    contents
}

fn day_01_run() {
    let path = "data/day_01.txt";
    let data = read(path);

    let part_a = day_01::what_floor(&data);
    let part_b = day_01::which_index_is_basement(&data);

    assert_eq!(part_a, 232);
    assert_eq!(part_b, 1783);

    println!("Day 01: Part A: {}; Part B: {}", part_a, part_b);

}

fn day_02_run() {
    let path = "data/day_02.txt";
    let lines = read(path);

    let mut total = 0;
    for line in lines.split('\n') {
        total += day_02::get_dimensions(line);
    }

    let mut ribbon_total = 0;
    for line in lines.split('\n') {
        ribbon_total += day_02::calculate_bow_length(line);
    }

    assert_eq!(total, 1_588_178);
    assert_eq!(ribbon_total, 3_783_758);
    println!("Day 02: Part A: {}; Part B: {}", total, ribbon_total);
}

fn day_03_run() {
    let path = "data/day_03.txt";
    let data = read(path);
    let stops = day_03::get_stops(&data);
    let robo_stops = day_03::get_stops_with_robo(&data);

    assert_eq!(stops.0, 2592);
    assert_eq!(robo_stops, 2360);

    println!("Day 03: Part A: {}; Part B: {}", stops.0, robo_stops);
}

#[allow(dead_code)]
fn day_04_run() {
    let result1 = day_04::get_md5_with_prefix("iwrupvqb", 5);
    let result2 = day_04::get_md5_with_prefix("iwrupvqb", 6);

    assert_eq!(result1, 346_386);
    assert_eq!(result2, 9_958_218);

    println!("Day 04: Part A: {}; Part B: {}", result1, result2);
}

fn day_05_run() {
    let path = "data/day_05.txt";
    let data = read(path);

    let mut total_nice = 0;
    let mut total_nice_new = 0;
    for line in data.lines() {
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

fn day_07_run() {
    let path = "data/day_07.txt";
    let lines = read(path);

    // Part A
    let mut circuit = day_07::Circuit::new();
    let mut total = -1;
    while total != 0 {
        total = 0;
        for line in lines.split('\n') {
            total += circuit.parse_line(line);
        }
    }
    let part1 = circuit.registers["a"];

    // part B
    circuit = day_07::Circuit::new();
    circuit.registers.insert("b".to_string(), part1);
    let mut total = -1;
    while total != 0 {
        total = 0;
        for line in lines.split('\n') {
            if !line.contains("44430 -> b") {
                total += circuit.parse_line(line);
            }
        }
    }

    println!("Day 07: Part A: {}; Part B: {}", part1, circuit.registers["a"]);
}

fn day_08_run() {
    let path = "data/day_08.txt";
    let lines = read(path);

    let mut part_a = 0;
    let mut part_b = 0;

    for line in lines.split('\n') {
        part_a += day_08::get_code_character_length(line);
        part_b += day_08::get_wrapped_code_character_length(line);
    }

    println!("Day 08: Part A: {}; Part B: {}", part_a, part_b);
}

fn day_09_run() {
    let path = "data/day_09.txt";
    let lines = read(path);

    let (part_a, part_b) = day_09::create_nd_array_of_cities(&lines);

    assert_eq!(part_a, 117);
    assert_eq!(part_b, 909);

    println!("Day 09: Part A: {}; Part B: {}", part_a, part_b);
}

fn day_10_run() {
    let mut input = "1113122113".to_string();
    let mut part_a = 0;
    let mut part_b = 0;

    for index in 0..51 {
        if index == 40 {
            part_a = input.len();
        } else if index == 50 {
            part_b = input.len();
        }

        input = day_10::parse_string(&input);
    }

    assert_eq!(part_a, 360_154);
    assert_eq!(part_b, 5_103_798);

    println!("Day 10: Part A: {}; Part B: {}", part_a, part_b);
}

fn day_11_run() {
    let part_a = day_11::iterate_next_with_rules("cqjxjnds");
    let part_b = day_11::iterate_next_with_rules("cqjxxyzz");

    assert_eq!(part_a, "cqjxxyzz");
    assert_eq!(part_b, "cqkaabcc");

    println!("Day 11: Part A: {}; Part B: {}", part_a, part_b);

}

fn day_12_run() {
    let path = "data/day_12.json";
    let lines = read(path);


    let part_a = day_12::search_for_numbers(&lines);
    let part_b = day_12::read_json(&lines);

    assert_eq!(part_a, 156_366);
    assert_eq!(part_b, 96_852);

    println!("Day 12: Part A: {}; Part B: {}", part_a, part_b);
}

fn day_13_run() {
    let path = "data/day_13.txt";
    let lines = read(path);
    day_13::organize_data(&lines);
}
pub fn time_it(func: fn() -> ()) {
    // Marker for benchmarking start
    let start = Instant::now();

    func();

    // Benchmarking
    let time = Instant::now() - start;
    let time_secs = time.as_secs();
    let time_millis = time.subsec_millis();

    println!("\t|-> Done in {} seconds.", time_secs as f32 + time_millis as f32 / 1000.0);
}

fn main() {
    let mut threads = Vec::new();
    threads.push(thread::spawn(||{ time_it(day_01_run) })); // Day 01: Part A: 232; Part B: 1783
    threads.push(thread::spawn(||{ time_it(day_02_run) })); // Day 02: Part A: 1588178; Part B: 3783758
    threads.push(thread::spawn(||{ time_it(day_03_run) })); // Day 03: Part A: 2592; Part B: 2360
    threads.push(thread::spawn(||{ time_it(day_04_run) })); // Day 04: Part A: 346386; Part B: 9958218
    threads.push(thread::spawn(||{ time_it(day_05_run) })); // Day 05: Part A: 255; Part B: 55
    threads.push(thread::spawn(||{ time_it(day_06_run) })); // Day 06: Part A: 400410; Part B: 15343601
    threads.push(thread::spawn(||{ time_it(day_07_run) })); // Day 07: Part A: 3176; Part B: 14710
    threads.push(thread::spawn(||{ time_it(day_08_run) })); // Day 08: Part A: 1350; Part B: 2085
    threads.push(thread::spawn(||{ time_it(day_09_run) })); // Day 09: Part A: 117; Part B: 909
    threads.push(thread::spawn(||{ time_it(day_10_run) })); // Day 10: Part A: 360154; Part B: 5103798
    threads.push(thread::spawn(||{ time_it(day_11_run) })); // Day 11: Part A: cqjxxyzz; Part B: cqkaabcc
    threads.push(thread::spawn(||{ time_it(day_12_run) })); // Day 12: Part A: 156366; Part B: 96852
    threads.push(thread::spawn(||{ time_it(day_13_run) })); // Day 12: Part A: 156366; Part B: 96852

    for item in threads {
        item.join().expect("Thread failed...");
    }
}


