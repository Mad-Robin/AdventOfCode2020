import pandas as pd

with open("day2.txt", "r") as file:

    inp =[]
    for line in file:
        inp.append(line.rstrip())

def CleanData(password):
    password = password.replace(': ', ',')
    password = password.replace('-', ',')
    password = password.replace(' ', ',')
    password = password.split(',')
    return password
    
def Task1():
    totalCnt = 0

    for password in inp:
        passstr = CleanData(password)

        cnt = 0
        for w in passstr[3]:
            if w == passstr[2]:
                cnt += 1

        if cnt >= int(passstr[0]) and cnt <= int(passstr[1]):
            totalCnt += 1

    print totalCnt

def Task2():
    totalCnt = 0
    offCnt = 0

    for password in inp:
        passstr = CleanData(password)

        try:
            if (passstr[3][int(passstr[0])-1] == passstr[2]) or (passstr[3][int(passstr[1])-1] == passstr[2]):
                if passstr[3][int(passstr[0])-1] == passstr[3][int(passstr[1])-1]:
                    continue
                else:
                    totalCnt += 1
            else:
                offCnt += 1
        except:
            print passstr

    print totalCnt

Task2()
