import numpy as np
import math


class Direction:
    def __init__(self, input_direction):
        self.command = input_direction[0]
        self.magnitude = int(input_direction[1:])


def return_direction(starting_direction, instruction_direction, magnitude, directions_dict):
    # print(starting_direction, magnitude, instruction_direction)
    if instruction_direction == 'L':
        magnitude *= -1
    starting_direction += magnitude
    starting_direction = starting_direction % 360
    # print(starting_direction)
    for key, val in directions_dict.items():
        if val == starting_direction:
            if key == 'n':
                resulting_direction = north
            elif key == 's':
                resulting_direction = south
            elif key == 'e':
                resulting_direction = east
            elif key == 'w':
                resulting_direction = west
    return resulting_direction


def to_degrees(starting_direction):
    if (starting_direction == [0, 1]).all():
        return 0
    elif (starting_direction == [0, -1]).all():
        return 180
    elif (starting_direction == [1, 0]).all():
        return 90
    elif (starting_direction == [-1, 0]).all():
        return 270


input_data = []
with open("Inputs/day12.txt", "r") as file:
    for line in file:
        input_data.append(Direction(line.rstrip()))

north = np.array([0, 1])
south = np.array([0, -1])
east = np.array([1, 0])
west = np.array([-1, 0])

directions = {'n': 0, 'e': 90, 's': 180, 'w': 270}

current_pos = np.array([0, 0])
direction = 90
current_dir = np.array([1, 0])

for instruction in input_data:
    if instruction.command == 'F':
        current_pos += current_dir * instruction.magnitude
    elif instruction.command == 'N':
        current_pos += north * instruction.magnitude
    elif instruction.command == 'S':
        current_pos += south * instruction.magnitude
    elif instruction.command == 'E':
        current_pos += east * instruction.magnitude
    elif instruction.command == 'W':
        current_pos += west * instruction.magnitude
    elif instruction.command in ['L', 'R']:
        current_dir = return_direction(direction, instruction.command, instruction.magnitude, directions)
        direction = to_degrees(current_dir)

print(abs(current_pos[0]) + abs(current_pos[1]))


def magnitude_of_vector(vector):
    magnitude = (vector[0]**2 + vector[1]**2)**0.5
    return magnitude


def angle_of_vector(vector):
    angle = math.degrees(math.atan2(vector[0], vector[1]))
    return angle


def create_new_vector(angle, magnitude):
    new_vector = np.array([0, 0])

    new_vector[0] = int(magnitude * math.sin(math.radians(angle)))
    new_vector[1] = int(magnitude * math.cos(math.radians(angle)))

    return new_vector


def rotate_waypoint(wp_pos, order):
    new_angle = order.magnitude

    if order.command == 'L':
        new_angle *= -1
    new_angle += angle_of_vector(wp_pos)

    vector_magnitude = magnitude_of_vector(wp_pos)
    new_vector = create_new_vector(new_angle, vector_magnitude)

    return new_vector


def question_2(data):
    ship_pos = np.array([0, 0])
    waypoint_pos = np.array([10, 1])

    for instr in data:
        #print(waypoint_pos, ship_pos, instr.command, instr.magnitude)
        if instr.command == 'N':
            waypoint_pos += north * instr.magnitude
        elif instr.command == 'S':
            waypoint_pos += south * instr.magnitude
        elif instr.command == 'E':
            waypoint_pos += east * instr.magnitude
        elif instr.command == 'W':
            waypoint_pos += west * instr.magnitude
        elif instr.command == 'F':
            ship_pos += instr.magnitude * waypoint_pos
        elif instr.command in ['L', 'R']:
            waypoint_pos = rotate_waypoint(waypoint_pos, instr)
        #(waypoint_pos, ship_pos)
    print(abs(ship_pos[0]) + abs(ship_pos[1]))


question_2(input_data)
