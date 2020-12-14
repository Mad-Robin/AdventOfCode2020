import pandas as pd
import numpy as np

inp = []

with open("day3.txt", "r") as file:
    for line in file:
        line = list(line.rstrip()) * 100
        inp.append(line)

data = np.array(inp)


def trees_hit(x_inc, y_inc):
    poi = []
    start_x = 0
    start_y = 0
    iterations = len(data[:])
    
    for i in range(0, iterations):
        try:
            if str(data[[start_y], [start_x]]) == "['.']":
                poi.append(0)
            else:
                poi.append(1)
        except:
            break
        start_x += x_inc
        start_y += y_inc

    return sum(poi)

TH = TreesHit(1,1)*TreesHit(3,1)*TreesHit(5,1)*TreesHit(7,1)*TreesHit(1,2)
print(TH)
