directions = {
    '|': ((-1, 0), (1, 0)),
    '-': ((0, -1), (0, 1)),
    'L': ((-1, 0), (0, 1)),
    'J': ((-1, 0), (0, -1)),
    '7': ((0, -1), (1, 0)),
    'F': ((1, 0), (0, 1)),
    '.': (),
    'S': ((-1, 0), (1, 0), (0, 1), (0, -1)),
}

left_right = {
    'L': 'R',
    'J': 'L',
    '7': 'L',
    'F': 'R',
}

up_down = {
    'L': 'U',
    'J': 'U',
    '7': 'D',
    'F': 'D',
}


def pos_s(pipe_map):
    for i_row, row in enumerate(pipe_map):
        for i_col, col in enumerate(row):
            if pipe_map[i_row][i_col] == 'S':
                return i_row, i_col
    raise Exception('S NOT FOUND')


def count_consecutive_diffs(alist):
    index = 0
    diffs = 0
    while index < len(alist):
        if alist[index] != alist[index + 1]:
            diffs += 1
        index += 2
    return diffs


def is_enclosed(i, j, pipe_map, visited):
    nr_rows = len(pipe_map)
    nr_cols = len(pipe_map[0])

    # Up
    up_count = len([pipe_map[i1][j] for i1 in range(i) if (i1, j) in visited and pipe_map[i1][j] == '-'])
    corners = [left_right[pipe_map[i1][j]] for i1 in range(i) if (i1, j) in visited and pipe_map[i1][j] in left_right]
    up_count += count_consecutive_diffs(corners)

    # Down
    down_count = len([pipe_map[i1][j] for i1 in range(i + 1, nr_rows) if (i1, j) in visited and pipe_map[i1][j] == '-'])
    corners = [left_right[pipe_map[i1][j]] for i1 in range(i + 1, nr_cols) if
               (i1, j) in visited and pipe_map[i1][j] in left_right]
    down_count += count_consecutive_diffs(corners)

    # Left
    left_count = len([pipe_map[i][j1] for j1 in range(j) if (i, j1) in visited and pipe_map[i][j1] == '|'])
    corners = [up_down[pipe_map[i][j1]] for j1 in range(j) if (i, j1) in visited and pipe_map[i][j1] in up_down]
    left_count += count_consecutive_diffs(corners)

    # Right
    right_count = len(
        [pipe_map[i][j1] for j1 in range(j + 1, nr_cols) if (i, j1) in visited and pipe_map[i][j1] == '|'])
    corners = [up_down[pipe_map[i][j1]] for j1 in range(j + 1, nr_cols) if
               (i, j1) in visited and pipe_map[i][j1] in up_down]
    right_count += count_consecutive_diffs(corners)

    return up_count % 2 == 1 and down_count % 2 == 1 and left_count % 2 == 1 and right_count % 2 == 1


def what_for_s(where_s, n1, n2):
    di1 = where_s[0] - n1[0]
    dj1 = where_s[1] - n1[1]
    di2 = where_s[0] - n2[0]
    dj2 = where_s[1] - n2[1]
    for k in directions:
        if (-di1, -dj1) in directions[k] and (-di2, -dj2) in directions[k]:
            return k
    raise Exception(f'Cannot find pipe for {where_s} and {n1}, {n2}')


def solve_day_10():
    pipe_map = []
    with open('./data/in/day-10.txt') as my_file:
        for line in my_file:
            pipe_map.append(line.strip())
    where_s = pos_s(pipe_map)

    visited = {where_s}
    queue = [where_s]
    nexsts = []
    while len(queue) > 0:
        current_pos = queue[0]
        queue = queue[1:]

        for next_possible_pos in directions[pipe_map[current_pos[0]][current_pos[1]]]:
            next_i = current_pos[0] + next_possible_pos[0]
            next_j = current_pos[1] + next_possible_pos[1]

            if (next_i, next_j) in visited:
                continue

            try:
                next_pipe = pipe_map[next_i][next_j]
                for comeback_pos in directions[next_pipe]:
                    comeback_i = next_i + comeback_pos[0]
                    comeback_j = next_j + comeback_pos[1]
                    if comeback_i == current_pos[0] and comeback_j == current_pos[1]:
                        visited.add((next_i, next_j))
                        queue.append((next_i, next_j))
                        nexsts.append((next_i, next_j))
                        break
            except:
                pass

    result = len(visited) // 2
    print('Part 1:', result)

    # Part 2
    # Replace S with proper pipe
    print('Nexst:', nexsts[:2])
    proper_pipe = what_for_s(where_s, nexsts[0], nexsts[1])
    pipe_map[where_s[0]] = pipe_map[where_s[0]].replace('S', proper_pipe)

    print(pipe_map)

    enclosed = 0
    for i in range(len(pipe_map)):
        for j in range(len(pipe_map[i])):
            if (i, j) not in visited and is_enclosed(i, j, pipe_map, visited):
                enclosed += 1
                print('Enclosed:', (i, j))
    print('Part 2:', enclosed)


if __name__ == '__main__':
    solve_day_10()
