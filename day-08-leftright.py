from math import gcd


def solve_one(start, map_nodes, directions):
    direction_index = 0
    position_now = start
    steps = 0

    while position_now[-1] != 'Z':
        if directions[direction_index] == 'L':
            position_now = map_nodes[position_now][0]
        else:
            position_now = map_nodes[position_now][1]
        direction_index = (direction_index + 1) % len(directions)
        steps += 1

    return steps


def solve_part_2(map_nodes, directions):
    positions_now = []
    for pos in map_nodes.keys():
        if pos[-1] == 'A':
            positions_now.append(pos)

    multipliers = [solve_one(pos, map_nodes, directions) for pos in positions_now]

    lcm = 1
    for i in multipliers:
        lcm = lcm * i // gcd(lcm, i)

    print('Part 2 Steps', lcm)


def solve_day_8():
    with open('./data/in/day-08.txt') as my_file:
        directions = my_file.readline().strip()
        map_nodes = {}
        my_file.readline()
        line = my_file.readline().strip().replace('(', '').replace(')', '')
        while line:
            position, remaining = line.split('=')
            position = position.strip()
            left_option, right_option = remaining.strip().split(',')
            left_option = left_option.strip()
            right_option = right_option.strip()

            # print(position, left_option, right_option)
            map_nodes[position] = (left_option, right_option)

            line = my_file.readline().strip().replace('(', '').replace(')', '')

        # Part 1
        # solve_part_1(map_nodes, directions)

        # Part 2
        solve_part_2(map_nodes, directions)


if __name__ == '__main__':
    solve_day_8()
