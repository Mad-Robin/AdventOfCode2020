import numpy as np


def check_adjacent(x, y, array):
    occupied_seats = 0
    empty_seats = 0
    width = array.shape[0]
    height = array.shape[1]

    for ii in range(x-1, x+2):
        for jj in range(y-1, y+2):
            if 0 <= ii < width and 0 <= jj < height:
                if ii == x and jj == y:
                    continue
                elif array[ii, jj] in ["L", "."]:
                    empty_seats += 1
                elif array[ii, jj] == "#":
                    occupied_seats += 1

    # print("This:", this_seat, "Occupied:", occupied_seats, "Empty:", empty_seats)
    return occupied_seats


def check_all_adjacent(x, y, array):
    occupied_seats = 0
    empty_seats = 0
    # this_seat = array[x, y]
    width = array.shape[0]
    height = array.shape[1]

    for i in range(x-1, x+2):
        for j in range(y - 1, y + 2):
            if 0 <= i < width and 0 <= j < height:
                if i == x and j == y:
                    continue
                else:
                    if array[i, j] == "L":
                        empty_seats += 1
                    elif array[i, j] == "#":
                        occupied_seats += 1
                    elif array[i, j] == ".":
                        a = 0
                        b = 0
                        while True:
                            a += (i - x)
                            b += (j - y)
                            # print(x, y, i, j, a, b, i+a, j+b)
                            if 0 <= (i+a) < width and 0 <= (j+b) < height:
                                next_value = find_value(i+a, j+b, array)
                                # print(next_value)
                                if next_value == "L":
                                    empty_seats += 1
                                    break
                                elif next_value == "#":
                                    occupied_seats += 1
                                    break
                            else:
                                break

    # print("This:", this_seat, "Occupied:", occupied_seats, "Empty:", empty_seats)
    return occupied_seats


def find_value(x, y, array):
    return array[x, y]


def explode_string(string):
    characters = []
    for character in string:
        characters.append(character)

    return characters


def check_seats(starting_array):
    resulting_array = np.chararray((starting_array.shape[0], starting_array.shape[1]), unicode=True)

    for i in range(0, resulting_array.shape[0]):
        for j in range(0, resulting_array.shape[1]):
            seats_occupied = check_adjacent(i, j, starting_array)
            if starting_array[i, j] == '.':
                resulting_array[i, j] = '.'
            elif starting_array[i, j] == 'L' and seats_occupied == 0:
                resulting_array[i, j] = '#'
            elif starting_array[i, j] == '#' and seats_occupied >= 4:
                resulting_array[i, j] = 'L'
            else:
                resulting_array[i, j] = starting_array[i, j]
    return resulting_array


def check_all_seats(array):
    resulting_array = np.chararray((array.shape[0], array.shape[1]), unicode=True)

    for i in range(0, resulting_array.shape[0]):
        for j in range(0, resulting_array.shape[1]):
            seats_occupied = check_all_adjacent(i, j, array)
            if array[i, j] == '.':
                resulting_array[i, j] = '.'
            elif array[i, j] == 'L' and seats_occupied == 0:
                resulting_array[i, j] = '#'
            elif array[i, j] == '#' and seats_occupied >= 5:
                resulting_array[i, j] = 'L'
            else:
                resulting_array[i, j] = array[i, j]
    return resulting_array


def total_occupied_seats(array):
    answer = 0
    for i in range(0, array.shape[0]):
        for j in range(0, array.shape[1]):
            if array[i, j] == '#':
                answer += 1
    print(answer)


def question_1(original_array):
    iteration_data = check_seats(original_array)
    while True:
        if (iteration_data == check_seats(iteration_data)).all():
            break
        iteration_data = check_seats(iteration_data)

    total_occupied_seats(iteration_data)


def question_2(array):
    iteration_data = check_all_seats(array)
    iterations = 0
    while True:
        if (iteration_data == check_all_seats(iteration_data)).all():
            break
        else:
            iterations += 1

        iteration_data = check_all_seats(iteration_data)

    total_occupied_seats(iteration_data)


def main():
    inp = []
    with open("day11.txt", "r") as file:
        for line in file:
            inp.append(explode_string(line.rstrip()))

    data = np.array(inp)

    # question_1(data)
    question_2(data)


if __name__ == '__main__':
    main()
