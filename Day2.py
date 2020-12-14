class Password:
    def __init__(self, password):
        self.min = int(password[0])
        self.pos_1 = int(password[0]) - 1
        self.max = int(password[1])
        self.pos_2 = int(password[1]) - 1
        self.letter = password[2]
        self.word = password[3]


def clean_data(password):
    password = password.replace(': ', ',')
    password = password.replace('-', ',')
    password = password.replace(' ', ',')
    password = password.split(',')
    return password


def task_1(input_data):
    total_count = 0

    for password in input_data:
        password = clean_data(password)
        password = Password(password)

        count = 0
        for letter in password.word:
            if letter == password.letter:
                count += 1

        if password.min <= count <= password.max:
            total_count += 1
    return total_count


def task_2(input_data):
    total_count = 0
    off_count = 0

    for password in input_data:
        pass_string = clean_data(password)
        pass_string = Password(pass_string)
        if (pass_string.word[pass_string.pos_1] == pass_string.letter) \
                or (pass_string.word[pass_string.pos_2] == pass_string.letter):
            if pass_string.word[pass_string.pos_1] == pass_string.word[pass_string.pos_2]:
                continue
            else:
                total_count += 1
        else:
            off_count += 1
    return total_count


def main():
    with open("Inputs/day2.txt", "r") as file:
        inp = []
        for line in file:
            inp.append(line.rstrip())

    print(task_1(inp))
    print(task_2(inp))


if __name__ == '__main__':
    main()
