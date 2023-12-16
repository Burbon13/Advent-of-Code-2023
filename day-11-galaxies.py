def empty_rows_and_cols(the_map):
    empty_rows = []
    for i, row in enumerate(the_map):
        if set(row) == {'.'}:
            empty_rows.append(i)
    empty_cols = []
    for j in range(len(the_map[0])):
        if set([the_map[i][j] for i in range(len(the_map))]) == {'.'}:
            empty_cols.append(j)
    return empty_rows, empty_cols


def get_all_galaxy_pos(the_map):
    positions = []
    for i in range(len(the_map)):
        for j in range(len(the_map[i])):
            if the_map[i][j] == '#':
                positions.append((i, j))
    return positions


def compute_distance(pos1, pos2, empty_rows, empty_cols):
    # Manhattan distance
    distance = abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
    # Plus galaxy expansion
    min_row, max_row = min(pos1[0], pos2[0]), max(pos1[0], pos2[0])
    for i in range(min_row, max_row):
        if i in empty_rows:
            # distance += 1
            distance += (1000000 - 1)
    min_col, max_col = min(pos1[1], pos2[1]), max(pos1[1], pos2[1])
    for j in range(min_col, max_col):
        if j in empty_cols:
            # distance += 1
            distance += (1000000 - 1)
    return distance


def solve_day_11():
    with open('./data/in/day-11.txt') as my_file:
        the_map = [line.strip() for line in my_file]
    empty_rows, empty_cols = empty_rows_and_cols(the_map)
    galaxy_pos = get_all_galaxy_pos(the_map)

    total = 0
    for i in range(len(galaxy_pos)):
        for j in range(i + 1, len(galaxy_pos)):
            total += compute_distance(galaxy_pos[i], galaxy_pos[j], empty_rows, empty_cols)

    print(empty_rows, empty_cols)
    print(galaxy_pos)
    print('Result:', total)


if __name__ == '__main__':
    solve_day_11()
