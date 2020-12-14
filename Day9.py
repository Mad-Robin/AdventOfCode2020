
def check_preamble(preamble, data):
    check = []
    for i in range(0, len(preamble)):
        if data - preamble[i] in preamble and 2 * preamble[i] != data:
            check.append(True)
        else:
            check.append(False)

    if True in check:
        return True
    else:
        return False


def contiguous_sum(data_set, target):
    values = []
    for i in range(0, len(data_set)):
        if sum(values) == target and len(values) > 1:
            return min(values) + max(values)
        elif sum(values) > target:
            break
        else:
            sum(values) < target
            values.append(data_set[i])


def main():
    inp = []
    with open("Inputs/day9.txt", "r") as file:
        for line in file:
            inp.append(int(line.rstrip()))

    # part_1
    i = 0
    data_set = []
    for data in inp[25:]:
        preamble = inp[i:i+25]

        if check_preamble(preamble, data) is True:
            i += 1
        else:
            data_set.append(data)
    print(data_set[0])

    # part_2
    for i in range(0, len(inp)):
        result = contiguous_sum(inp[i:], data_set[0])
        if result is not None:
            print(result)


if __name__ == '__main__':
    main()
