#  MIT License
#
#  Copyright (c) 2019 Jason Brackman
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.


from python import helpers

registers = {"a": 0, "b": 0, None: 0}

functions = {
    "hlf": lambda index, r, j: (index + 1, r // 2),
    "tpl": lambda index, r, j: (index + 1, r * 3),
    "inc": lambda index, r, j: (index + 1, r + 1),
    "jmp": lambda index, r, j: (index + r, r),
    "jio": lambda index, r, j: (index + j, r) if r == 1 else (index + 1, r),
    "jie": lambda index, r, j: (index + j, r) if r % 2 == 0 else (index + 1, r),
}


def main():
    instructions = helpers.get_lines(r"../data/day_23.txt")

    # Part01
    result_registers = process_instructions(instructions)
    assert result_registers["b"] == 255

    # Part02
    # - reset registers
    registers["a"] = 1
    registers["b"] = 0
    result_registers = process_instructions(instructions)
    assert result_registers["b"] == 334


def process_instructions(instructions):
    index = 0
    while index < len(instructions):

        instruction: str = ""
        register: str = ""
        index_jump: int = 1

        items = instructions[index].split()
        if len(items) == 2:
            instruction = items[0]

            is_negative = items[1].startswith("-")
            test = items[1].strip("+-")
            test = int(test) if test.isdigit() else test
            register = test * -1 if is_negative else test

        elif len(items) == 3:
            instruction, register, index_jump = (
                items[0],
                items[1].strip(","),
                int(items[2]),
            )

        current_register = (
            registers.get(register, None) if isinstance(register, str) else register
        )
        index, register_value = functions[instruction](
            index, current_register, index_jump
        )
        if register in registers:
            registers[register] = register_value

    # print("Index:", index, "Registers:", registers)

    return registers


if __name__ == "__main__":
    main()
