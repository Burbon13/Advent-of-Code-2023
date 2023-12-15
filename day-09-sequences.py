def subtract_end(numlist):
    if set(numlist) == {0}:
        return 0

    new_list = []
    index = 1
    while index < len(numlist):
        new_list.append(numlist[index] - numlist[index - 1])
        index += 1

    return numlist[-1] + subtract_end(new_list)


def subtract_begin(numlist):
    if set(numlist) == {0}:
        return 0

    new_list = []
    index = 1
    while index < len(numlist):
        new_list.append(numlist[index] - numlist[index - 1])
        index += 1

    return numlist[0] - subtract_begin(new_list)


def solve_day_9():
    with open('./data/in/day-09.txt') as my_file:
        result_end = 0
        result_begin = 0
        for line in my_file:
            numbers = [int(x) for x in line.strip().split(' ')]
            result_end += subtract_end(numbers)
            result_begin += subtract_begin(numbers)
            print(result_end, result_begin)
        print()
        print('Part 1:', result_end)
        print('Part 2:', result_begin)


if __name__ == '__main__':
    solve_day_9()
