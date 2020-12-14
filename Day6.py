def unique_characters(answer_string):
    answer_string = "".join(set(answer_string))
    return answer_string


def question_1(data):
    sum_of_counts = 0
    for string in data:
        sum_of_counts += len(string)

    return sum_of_counts


def question_2(data):
    question_2_answer = 0
    for a in data:
        a_dict = {}
        for characters in a:
            for char in characters:
                if char not in a_dict:
                    a_dict[char] = 1
                else:
                    a_dict[char] += 1

        for key, val in a_dict.items():
            if val == len(a):
                question_2_answer += 1
    return question_2_answer


def main():
    entry = ''
    question_1_data = []
    entities = []
    question_2_data = []

    with open("Inputs/day6.txt", "r") as file:
        for line in file:
            line = line.rstrip()
            if len(line) > 0:
                entry += line
                entities.append(line)
            else:
                question_1_data.append(unique_characters(entry))
                entry = ''
                question_2_data.append(entities)
                entities = []
        question_1_data.append(unique_characters(entry))
        question_2_data.append(entities)

    print(question_1(question_1_data))
    print(question_2(question_2_data))


if __name__ == '__main__':
    main()
