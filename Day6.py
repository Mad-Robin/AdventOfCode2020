def unique_characters(answer_string):
    answer_string = "".join(set(answer_string))
    return answer_string


entry = ''
answers = []
with open("example.txt", "r") as file:
    for line in file:
        line = line.rstrip()
        if len(line) > 0:
            entry += line
        else:
            answers.append(unique_characters(entry))
            entry = ''
    answers.append(unique_characters(entry))

sum_of_counts = 0
for string in answers:
    sum_of_counts += len(string)

print(sum_of_counts)

# Part 2
ent = []
ans = []
with open("day6.txt", "r") as file:
    for line in file:
        line = line.rstrip()
        if len(line) > 0:
            ent.append(line)
        else:
            ans.append(ent)
            ent = []
    ans.append(ent)

question_2_answer = 0
for a in ans:
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

print(question_2_answer)
