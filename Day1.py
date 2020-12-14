with open("day1.txt", "r") as file:

    inp =[]
    for line in file:
        inp.append(int(line.rstrip()))

def TwoNumbers(): 
    for num in inp:
        negNum = 2020 - num
        if negNum in inp:
            print negNum * num
            break
        else:
            continue

def ThreeNumbers():
    for num1 in inp:
        for num2 in inp:
            for num3 in inp:
                if (num1+num2+num3) == 2020:
                    print num1, num2, num3
                    print num1 * num2 * num3
                    break

ThreeNumbers()
