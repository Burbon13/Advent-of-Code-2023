def compute_ways_to_win(time, distance):
    total = 0
    for seconds_pressed in range(time + 1):
        traveled_distance = (time - seconds_pressed) * seconds_pressed
        if traveled_distance > distance:
            total += 1
    return total


# Used for both part 1 and 2. Just change the input file to have the numbers concatenated.
def solve_day_6_part_1():
    result = 1
    with open('./data/in/day-06-part-1.txt') as my_file:
        times = my_file.readline().strip().split(' ')
        distances = my_file.readline().strip().split(' ')
        times = [int(x) for x in times]
        distances = [int(x) for x in distances]
        for time, distance in zip(times, distances):
            result *= compute_ways_to_win(time, distance)
    print('Part 1:', result)


if __name__ == '__main__':
    solve_day_6_part_1()
    solve_day_6_part_2()
