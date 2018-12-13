extern crate regex;

pub struct Board {
    squares: [[bool; 1000]; 1000],
    squares2: Vec<Vec<i32>>,
}

impl Board {
    pub fn new() -> Board {
        let v1 = vec![vec![0; 1000]; 1000];

        Board {
            squares: [[false; 1000]; 1000],
            squares2: v1,
        }
    }

    /// dealing with squares (Part A)
    pub fn switch(&mut self, start: (usize, usize), end: (usize, usize), state: &str) {
        let doit = |x: bool| match state {
            "off" => false,
            "on" => true,
            _ => !x,
        };

        for x in start.0..=end.0 {
            for y in start.1..=end.1 {
                self.squares[x][y] = doit(self.squares[x][y]);
            }
        }
    }

    pub fn count_true_squares(&self) -> i32 {
        let mut counter = 0;

        for x in 0..1000 {
            for y in 0..1000 {
                if self.squares[x][y] {
                    counter += 1
                }
            }
        }

        counter
    }

    /// dealing with squares2 (part B)
    pub fn switch2(&mut self, start: (usize, usize), end: (usize, usize), state: &str) {
        let doit = match state {
            "off" => -1,
            "on" => 1,
            _ => 2,
        };

        for x in start.0..=end.0 {
            for y in start.1..=end.1 {
                self.squares2[x][y] += doit;

                // ensure we don't have a negative brightness
                if self.squares2[x][y] < 0 {
                    self.squares2[x][y] = 0;
                }
            }
        }
    }

    pub fn count_true_squares2(&self) -> i32 {
        let mut counter = 0;

        for x in 0..1000 {
            for y in 0..1000 {
                counter += self.squares2[x][y];
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
    } else {
        "toggle"
    };

    let re = regex::Regex::new(r"(\d+),(\d+) through (\d+),(\d+)").unwrap();
    let caps = re.captures(input).unwrap();

    let sx = caps
        .get(1)
        .map_or(1001, |m| m.as_str().parse::<usize>().unwrap());
    let sy = caps
        .get(2)
        .map_or(1001, |m| m.as_str().parse::<usize>().unwrap());
    let ex = caps
        .get(3)
        .map_or(1001, |m| m.as_str().parse::<usize>().unwrap());
    let ey = caps
        .get(4)
        .map_or(1001, |m| m.as_str().parse::<usize>().unwrap());

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
fn test_switch_and_count_2() {
    let mut board = Board::new();
    board.switch2((0, 0), (999, 999), "off");
    board.switch2((0, 0), (999, 999), "on");
    assert_eq!(board.count_true_squares2(), 1_000_000);
    board.switch2((0, 0), (999, 0), "off");
    assert_eq!(board.count_true_squares2(), 999_000);
    board.switch2((499, 499), (500, 500), "off");
    assert_eq!(board.count_true_squares2(), 998_996);
    board.switch2((499, 499), (500, 500), "toggle");
    assert_eq!(board.count_true_squares2(), 999_004);
}

#[test]
fn test_process_line() {
    let input = "turn off 660,55 through 986,197";
    assert_eq!(process_line(input), ((660, 55), (986, 197), "off"));
}
