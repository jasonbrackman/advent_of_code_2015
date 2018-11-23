use std::collections::HashMap;

pub struct Circuit {
    pub registers: HashMap<String, u16>
}

impl Circuit {
    pub fn new() -> Circuit {
        Circuit {
            registers: HashMap::new()
        }
    }

    // args can be:
    // 1. a register; ie: ab
    // 2. a value; ie: 4
    // 3. bitwise operator; ie: AND, OR, NOT
    // 4. an assignment value ->
    pub fn parse_line(&mut self, input: &str) -> i32 {
        let mut problems = 0;

        let args = input.split("->").collect::<Vec<&str>>();

        // ensure rhs is in hashmap with a default zero value if not.
        let rhs: &str = args[1];

        // break down the lhs into its args (1 to 3 expected)
        let lhs: Vec<&str> = args[0].split_whitespace().collect();


        if lhs.len() == 1 { // must be a number!
            match lhs[0].parse::<u16>() {
                Ok(n) => *self.registers.entry(rhs.trim().to_string()).or_insert(0) = n,
                Err(_) => if self.registers.contains_key(lhs[0].trim()) {
                    *self.registers
                        .entry(rhs.trim().to_string())
                        .or_insert(0) = self.registers[lhs[0].trim()];
                } else {
                    problems += 1
                }
            };

        } else if lhs.len() == 2 {

            match lhs[1].parse::<u16>() {
                Ok(n) => *self.registers.entry(rhs.trim().to_string()).or_insert(0) = !n,
                Err(_) => {
                    if self.registers.contains_key(lhs[1].trim()) {
                        *self.registers
                            .entry(rhs.trim().to_string())
                            .or_insert(0) = !self.registers[lhs[1].trim()];
                    } else {
                        problems += 1;
                    }
                }
            };

        } else {
            let arg_1 = lhs[0].parse::<u16>();
            let arg_2 = lhs[2].parse::<u16>();

            let mut result1 = 0;
            if arg_1.is_ok() {
                result1 = arg_1.unwrap();
            } else if self.registers.contains_key(lhs[0].trim()) {
                result1 = self.registers[lhs[0].trim()];
            } else { problems += 1;}

            let mut result2 = 0;
            if arg_2.is_ok() {
                result2 = arg_2.unwrap();
            } else if self.registers.contains_key(lhs[2].trim()) {
                result2 = self.registers[lhs[2].trim()];
            } else {
                problems += 1;
            }

            if problems == 0 {
                *self.registers.entry(rhs.trim().to_string()).or_insert(0) = match lhs[1].trim() {
                    "AND" => result1 & result2,
                    "OR" => result1 | result2,
                    "LSHIFT" => result1 << result2,
                    "RSHIFT" => result1 >> result2,
                    _ => panic!("Unexpected pattern found ... ")
                };
            }
        }

        problems
    }
}

#[test]
fn test_bitwise_and() {
    let mut circuit = Circuit::new();
    let mut total = -1;
    while total != 0 {
        total = 0;

        total += circuit.parse_line("123 -> x");
        total += circuit.parse_line("456 -> y");
        total += circuit.parse_line("x AND y -> d");
        total += circuit.parse_line("x OR y -> e");
        total += circuit.parse_line("x LSHIFT 2 -> f");
        total += circuit.parse_line("y RSHIFT 2 -> g");
        total += circuit.parse_line("NOT x -> h");
        total += circuit.parse_line("NOT y -> i");
    }
    assert_eq!(circuit.registers["d"], 72);
    assert_eq!(circuit.registers["e"], 507);
    assert_eq!(circuit.registers["f"], 492);
    assert_eq!(circuit.registers["g"], 114);
    assert_eq!(circuit.registers["h"], 65412);
    assert_eq!(circuit.registers["i"], 65079);
    assert_eq!(circuit.registers["x"], 123);
    assert_eq!(circuit.registers["y"], 456);
}

#[test]
fn test_get_parent_values() {
    let mut circuit = Circuit::new();
    let mut total = -1;
    while total != 0 {
        total = 0;
        total += circuit.parse_line("NOT eo -> z");
        total += circuit.parse_line("9 -> eo");

    }
    println!("total: {} -> z: {}", total, circuit.registers["z"]);

}