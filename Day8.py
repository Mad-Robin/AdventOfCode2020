class Line:
    def __init__(self, instruction):
        self.operation = instruction[0]
        self.argument = int(instruction[1])


def question_1(instructions):
    q1_accumulator = 0
    i_checked = []
    i = 0

    while True:
        if i in i_checked:
            break
        else:
            i_checked.append(i)
            print(instructions[i].operation, instructions[i].argument)
            if instructions[i].operation == 'nop':
                i += 1
            elif instructions[i].operation == 'jmp':
                i += instructions[i].argument
            elif instructions[i].operation == 'acc':
                q1_accumulator += instructions[i].argument
                i += 1

    print(q1_accumulator)


def question_2(instructions):
    for i in range(0, len(instructions)):
        temp_instructions = []
        temp_instruction = []

        for j in range(0, len(instructions)):
            if i == j:
                if instructions[i].operation == 'nop':
                    if instructions[i].argument != 0:
                        temp_instruction.append('jmp')
                    else:
                        temp_instruction.append('nop')
                elif instructions[i].operation == 'jmp':
                    temp_instruction.append('nop')
                else:
                    temp_instruction.append('acc')
                temp_instruction.append(instructions[j].argument)
            else:
                temp_instruction.append(instructions[j].operation)
                temp_instruction.append(instructions[j].argument)

            temp_instructions.append(Line(temp_instruction))
            temp_instruction = []

        attempt_to_run_code(temp_instructions)


def attempt_to_run_code(instr):
    q2_accumulator = 0
    i_checked = []
    i = 0

    while True:
        if i == len(instr):
            print(q2_accumulator)
            return q2_accumulator
        elif i in i_checked:
            break
        else:
            i_checked.append(i)

            if instr[i].operation == 'nop':
                i += 1
            elif instr[i].operation == 'jmp':
                i += instr[i].argument
            elif instr[i].operation == 'acc':
                q2_accumulator += instr[i].argument
                i += 1


def main():
    instructions = []
    with open("Inputs/day8.txt", "r") as file:
        for line in file:
            instructions.append(Line(line.rstrip().split(' ')))
    question_2(instructions)


if __name__ == '__main__':
    main()
