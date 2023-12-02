import re


def solve_day_2_part_1():
    red_limit = 12
    green_limit = 13
    blue_limit = 14
    answer = 0
    with (open('./data/in/day-02-part-1.txt') as my_file):
        for line in my_file:
            game_in, rest_data = line.strip().split(':')
            game_nr = int(game_in.split(' ')[1])
            plays = rest_data.split(';')
            max_dict = {
                'red': 0,
                'green': 0,
                'blue': 0
            }
            for grab in plays:
                cubes = grab.split(',')
                for one_color_cubes in cubes:
                    number, color = one_color_cubes.strip().split(' ')
                    int_number = int(number)
                    max_dict[color] = max(max_dict[color], int_number)
            if max_dict['red'] <= red_limit \
                    and max_dict['green'] <= green_limit \
                    and max_dict['blue'] <= blue_limit:
                answer += game_nr
    print(answer)


def solve_day_2_part_2():
    answer = 0
    with (open('./data/in/day-02-part-1.txt') as my_file):
        for line in my_file:
            game_in, rest_data = line.strip().split(':')
            game_nr = int(game_in.split(' ')[1])
            plays = rest_data.split(';')
            max_dict = {
                'red': 0,
                'green': 0,
                'blue': 0
            }
            for grab in plays:
                cubes = grab.split(',')
                for one_color_cubes in cubes:
                    number, color = one_color_cubes.strip().split(' ')
                    int_number = int(number)
                    max_dict[color] = max(max_dict[color], int_number)
            answer += max_dict['red'] * max_dict['green'] * max_dict['blue']
    print(answer)


if __name__ == '__main__':
    # solve_day_2_part_1()
    solve_day_2_part_2()
