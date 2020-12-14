import numpy as np


def tress_hit(x_inc, y_inc, data):
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


def main():
    inp = []
    with open("Inputs/day3.txt", "r") as file:
        for line in file:
            line = list(line.rstrip()) * 100
            inp.append(line)
    data = np.array(inp)

    paths = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    total_trees_hit = 1
    for path in paths:
        total_trees_hit *= tress_hit(path[0], path[1], data)

    print(tress_hit(3, 1, data))
    print(total_trees_hit)


if __name__ == '__main__':
    main()
