/// 123 -> x means that the signal 123 is provided to wire x.
/// x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
/// p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
/// NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.
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
        let args = input.split("->").collect::<Vec<&str>>();

        // ensure rhs is in hashmap with a default zero value if not.
        let rhs: &str = args[1];

        // break down the lhs into its args (1 to 3 expected)
        let lhs: Vec<&str> = args[0].split_whitespace().collect();

        // Deal with only one argument which must be a register w value or JUST a value
        if lhs.len() == 1 {
            let current = lhs[0].parse::<u16>();
            let result = match current {
                Ok(n) => n,
                Err(_) => *self.registers.entry(lhs[0].trim().to_string()).or_insert(0)
            };

            *self.registers.entry(rhs.trim().to_string()).or_insert(0) = result;

        } else if lhs.len() == 2 {

            let current = lhs[1].parse::<u16>();
            let result = match current {
                Ok(n) => n,
                Err(_) => *self.registers.entry(lhs[1].trim().to_string()).or_insert(0)
            };

            *self.registers.entry(rhs.trim().to_string()).or_insert(0) = !result;

        } else {
            let arg_1 = lhs[0].parse::<u16>();
            let arg_2 = lhs[2].parse::<u16>();

            let result1 = match arg_1 {
                Ok(n) => n,
                Err(_) => *self.registers.entry(lhs[0].trim().to_string()).or_insert(0)
            };

            let result2 = match arg_2 {
                Ok(n) => n,
                Err(_) => *self.registers.entry(lhs[2].trim().to_string()).or_insert(0)
            };

            *self.registers.entry(rhs.trim().to_string()).or_insert(0) = match lhs[1].trim() {
                "AND" => result1 & result2,
                "OR" => result1 | result2,
                "LSHIFT" => result1 << result2,
                "RSHIFT" => result1 >> result2,
                _ => panic!("Unexpected pattern found ... ")
            };

        }

        0
    }
}

#[test]
fn test_bitwise_and() {
    let mut circuit = Circuit::new();
    circuit.parse_line("123 -> x");
    circuit.parse_line("456 -> y");
    circuit.parse_line("x AND y -> d");
    circuit.parse_line("x OR y -> e");
    circuit.parse_line("x LSHIFT 2 -> f");
    circuit.parse_line("y RSHIFT 2 -> g");
    circuit.parse_line("NOT x -> h");
    circuit.parse_line("NOT y -> i");
    assert_eq!(circuit.registers["d"], 72);
    assert_eq!(circuit.registers["e"], 507);
    assert_eq!(circuit.registers["f"], 492);
    assert_eq!(circuit.registers["g"], 114);
    assert_eq!(circuit.registers["h"], 65412);
    assert_eq!(circuit.registers["i"], 65079);
    assert_eq!(circuit.registers["x"], 123);
    assert_eq!(circuit.registers["y"], 456);

}