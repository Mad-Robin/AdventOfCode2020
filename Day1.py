def two_numbers(input_data):
    for num in input_data:
        neg_num = 2020 - num
        if neg_num in input_data:
            return neg_num * num
            break
        else:
            continue


def three_numbers(input_data):
    answer = []
    for num1 in input_data:
        for num2 in input_data:
            for num3 in input_data:
                if (num1+num2+num3) == 2020:
                    if len(answer) == 0:
                        answer.append(num1 * num2 * num3)
                    break
    return answer[0]


def main():
    with open("Inputs/day1.txt", "r") as file:
        inp = []
        for line in file:
            inp.append(int(line.rstrip()))

    print(two_numbers(inp))
    print(three_numbers(inp))


if __name__ == '__main__':
    main()