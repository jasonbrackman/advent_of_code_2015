extern crate regex;
//use regex::Regex;

pub struct Board {
    squares: [[bool;1000] ;1000]
}

impl Board {
    pub fn new() -> Board {
        Board{squares:[[false; 1000]; 1000]}
    }

    pub fn switch(&mut self, start:(usize, usize), end:(usize, usize), state: &str) {
        let doit = |x: bool| {match state {
            "off" => false,
            "on" => true,
            _ => !x
        }};

        for x in 0..1000 {
            for y in 0..1000 {
                if x >= start.0 && x <= end.0 && y >= start.1 && y <= end.1 {
                    self.squares[x][y] = doit(self.squares[x][y]);
                }
            }
        }
    }

    pub fn count_true_squares(&self) -> i32 {
        let mut counter = 0;

        for x in 0..1000 {
            for y in 0..1000 {
                if self.squares[x][y] == true {
                    counter += 1
                }
            }
        }

        counter
    }
}

pub fn process_line(input: &str) -> ((usize, usize), (usize, usize), &str) {
    let arg = if input.contains("off") {
        "off"
    } else if input.contains("on") {
        "on"
    } else { "toggle" };

    let re = regex::Regex::new(r"(\d+),(\d+) through (\d+),(\d+)").unwrap();
    let caps = re.captures(input).unwrap();

    let sx = caps.get(1).map_or(1001, |m| m.as_str().parse::<usize>().unwrap());
    let sy = caps.get(2).map_or(1001, |m| m.as_str().parse::<usize>().unwrap());
    let ex = caps.get(3).map_or(1001, |m| m.as_str().parse::<usize>().unwrap());
    let ey = caps.get(4).map_or(1001, |m| m.as_str().parse::<usize>().unwrap());

    ((sx, sy), (ex, ey), arg)
}
#[test]
fn test_toggle_lights() {
    let mut board = Board::new();
    board.switch((0, 0), (999, 999), "on");
    assert_eq!(board.count_true_squares(), 1_000_000);
    board.switch((0, 0), (999, 0), "off");
    assert_eq!(board.count_true_squares(), 999_000);
    board.switch((499, 499), (500, 500), "off");
    assert_eq!(board.count_true_squares(), 998_996);
    board.switch((499, 499), (500, 500), "toggle");
    assert_eq!(board.count_true_squares(), 999_000);
}

#[test]
fn test_process_line() {
    let input = "turn off 660,55 through 986,197";
    assert_eq!(process_line(input), ((660, 55), (986, 197), "off"));

}

