mod day_01;

use std::fs::File;
use std::io::prelude::*;

fn read(path: &str) -> String {
    println!("In file {}", path);

    let mut f = File::open(path).expect("file not found");

    let mut contents = String::new();
    f.read_to_string(&mut contents).expect("something went wrong reading the file");

    contents
}

fn day_01_run_a() {
    let path = "data/day_01.txt";
    let data = read(path);
    println!("{}", day_01::what_floor(&data));
    println!("{}", day_01::which_index_is_basement(&data))
}

fn main() {
    day_01_run_a();

}


