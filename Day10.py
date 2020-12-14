

inp = [0]
with open("example.txt", "r") as file:
    for line in file:
        inp.append(int(line.rstrip()))

inp.sort()

inp.append(max(inp) + 3)
print(inp)

jolt_differences = []
for i in range(0, len(inp) - 1):
    jolt_difference = inp[i+1] - inp[i]
    jolt_differences.append(jolt_difference)

print(jolt_differences)

ones = 0
threes = 0
for i in jolt_differences:
    if i == 1:
        ones += 1
    elif i == 3:
        threes += 1

print(ones * threes)

joltage_lists = []
joltage_list = []

for i in inp:
    for j in inp:
        if inp[j] < inp[i] <= inp[j] + 3:
            print(inp[j])