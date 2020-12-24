class Mask:
    def __init__(self, instruction):
        instruction = instruction.split(' = ')
        self.type = instruction[0]
        self.mask = instruction[1]


class Memory:
    def __init__(self, instruction):
        instruction = instruction.split(' = ')
        self.type = 'mem'
        address = [s for s in instruction[0] if s.isdigit()]
        self.address = int("".join(address))
        self.value = int(instruction[1])


def get_binary(value, length):
    return format(value, 'b').zfill(length)


def apply_mask(binary, mask):
    binary = list(binary)
    mask = list(mask)
    for i in range(0, len(mask)):
        if mask[i] == 'X':
            continue
        elif mask[i] in ['0', '1']:
            binary[i] = mask[i]
    result = "".join(binary)
    return result


def apply_memory_bitmask(memory, mask):
    memory = list(memory)
    mask = list(mask)

    results = []
    count_x = 0
    float_replacements = []
    for i in range(0, len(mask)):
        if mask[i] == 'X':
            count_x += 1

    for i in range(0, 2**count_x):
        float_replacement = list(get_binary(i, count_x))
        float_replacements.append(float_replacement)

    for j in range(0, len(float_replacements)):
        k = 0

        for i in range(0, len(mask)):
            if mask[i] == '0':
                continue
            elif mask[i] == '1':
                memory[i] = '1'
            else:
                memory[i] = float_replacements[j][k]
                k += 1

        memory_string = "".join(memory)

        results.append(to_int(memory_string))

    return results


def to_int(binary):
    value = int(binary, 2)
    return value


def question_1(instructions):
    current_mask = ''
    addresses = {}
    for command in instructions:
        if command.type == 'mask':
            current_mask = command.mask
        else:
            binary_value = get_binary(command.value, 36)
            masked_binary = apply_mask(binary_value, current_mask)
            addresses[command.address] = to_int(masked_binary)

    answer = 0
    for key, val in addresses.items():
        answer += val

    print(answer)


def question_2(instructions):
    current_mask = ''
    addresses = {}
    for command in instructions:
        if command.type == 'mask':
            current_mask = command.mask
        else:
            binary_value = get_binary(command.address, 36)
            memory_addresses = apply_memory_bitmask(binary_value, current_mask)
            for i in range(0, len(memory_addresses)):
                addresses[memory_addresses[i]] = command.value

    answer = 0
    for key, val in addresses.items():
        answer += val

    print(answer)


def main():
    inp = []
    with open("Inputs/day14.txt", "r") as file:
        for line in file:
            inp.append(line.rstrip())

    instructions = []
    for entry in inp:
        if entry.split(" = ")[0] == 'mask':
            instructions.append(Mask(entry))
        else:
            instructions.append(Memory(entry))

    question_1(instructions)
    question_2(instructions)


if __name__ == '__main__':
    main()
