# Part 2 state:
stars_dict = {}
numbers_dict = {}


def is_special_char(c, row, col, initial_row, initial_col):
    if c.isdigit():
        return False
    if c == '.':
        return False
    if c == '*':
        # Part 2 addition: Add to global map state
        actual_list = stars_dict.get((row, col), [])
        actual_list.append((initial_row, initial_col))
        stars_dict[(row, col)] = actual_list
    return True


def char_in_vicinity(matrix, row, col, nr_row, nr_col, initial_row, initial_col):
    d1 = [-1, -1, -1, 0, 1, 1, 1, 0]
    d2 = [-1, 0, 1, 1, 1, 0, -1, -1]

    drow = [x + row for x in d1]
    dcol = [x + col for x in d2]

    for i1, i2 in zip(drow, dcol):
        if 0 <= i1 < nr_row and 0 <= i2 < nr_col and is_special_char(matrix[i1][i2], i1, i2, initial_row, initial_col):
            return True
    return False


def compute_number(matrix, row, col, nr_row, nr_col):
    initial_row, initial_col = row, col
    is_valid = False
    value = 0
    while col < nr_col and matrix[row][col].isdigit():
        value = value * 10 + int(matrix[row][col])
        is_valid = is_valid or char_in_vicinity(matrix, row, col, nr_row, nr_col, initial_row, initial_col)
        col = col + 1
    return is_valid, value


def solve_day_3_part_1():
    answer = 0
    matrix = []
    with open('./data/in/day-03-part-1.txt') as my_file:
        for line in my_file:
            matrix.append(line.strip())
    nr_row = len(matrix)
    nr_col = len(matrix[0])
    for row in range(nr_row):
        for col in range(nr_col):
            c = matrix[row][col]
            if c.isdigit() and (col == 0 or not matrix[row][col - 1].isdigit()):
                is_valid, number = compute_number(matrix, row, col, nr_row, nr_col)
                print(number, is_valid)
                if is_valid:
                    answer += number
                    # For Part 2
                    numbers_dict[(row, col)] = number
    print('Answer Part 1:', answer)


def solve_day_3_part_2():
    answer = 0
    for k in stars_dict:
        if len(stars_dict[k]) == 2:
            gear_mul = 1
            for num_key in stars_dict[k]:
                gear_mul *= numbers_dict[num_key]
            answer += gear_mul
    print('Answer Part 2:', answer)


if __name__ == '__main__':
    solve_day_3_part_1()
    solve_day_3_part_2()
