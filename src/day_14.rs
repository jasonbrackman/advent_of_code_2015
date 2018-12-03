use std::collections::HashMap;

pub struct Rule {
    name: String,
    speed: i32,
    speed_time: i32,
    rest_time: i32
}

fn parse_line_to_components(input: &str) -> Vec<&str> {
    input.split_whitespace().map(|s| s.trim_right_matches('.')).collect()
}

pub fn race(rules: Vec<Rule>, rounds: i32) -> HashMap<String, Vec<i32>>{
    let mut hmap = HashMap::new();

    for rule in rules.iter() {
        let r = hmap.entry(rule.name.to_string()).or_insert(Vec::new());
        println!("Processing: {}", rule.name);
        let mut total = 0;
        let mut round = 0;

        while round <= rounds {  // 864 too low.
            for fly in 0..rule.speed_time {
                total += rule.speed;
                round += 1;
                r.push(total);
                if fly == rule.speed_time-1 {
                    for _rest in 0..rule.rest_time {
                        round += 1;
                        r.push(total);
                        if round >= rounds {
                            //println!("Name: {} -> Distance Travelled: {} -> in {} round of {} rounds.", rule.name, total, round, rounds);
                            break;
                        }
                    }
                }

                if round == rounds {
                    println!("Name: {} -> Distance Travelled: {} -> in {} round of {} rounds.", rule.name, total, round, rounds);
                    break;
                }
            }
        }
    }

    hmap
}

pub fn award_point_for_each_win(hmap: HashMap<String, Vec<i32>>) {
    //let new_totals = HashMap::new();
    let mut max = 0;
    for i in 0..1 {
        for (unit, times) in hmap.iter() {
            let temp_time = times[i];
            if temp_time >= max {
                max = temp_time;
                println!("{}->{}", unit, temp_time);
            }
            println!("{}: {}: {}", i, unit, times[i]);
        }

    }
    println!("{}", hmap.keys().len());
}
pub fn prepare_rules(input: &str) -> Vec<Rule> {
    let mut reindeer = Vec::new();
    for line in input.lines() {

        let components = parse_line_to_components(line);
        let x = Rule{
            name: String::from(components[0]),
            speed: components[3].parse::<i32>().unwrap(),
            speed_time: components[6].parse::<i32>().unwrap(),
            rest_time: components[13].parse::<i32>().unwrap()
        };
        reindeer.push(x);
    }

    reindeer
}

#[test]
fn test_parse_line_to_components() {
    let input = "this is a line.";
    assert_eq!(parse_line_to_components(input), vec!("this", "is", "a", "line"));
}

