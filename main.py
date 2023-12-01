import re


def solve_day_1_part_1():
    digits = []
    with open('./data/in/day-01-part-1.txt') as my_file:
        for line in my_file:
            temp_digits = []
            for character in line:
                if character.isdigit():
                    temp_digits.append(character)
            digits.append(temp_digits[0])
            digits.append(temp_digits[-1])
    i = 0
    total = 0
    while i < len(digits):
        d1, d2 = int(digits[i]), int(digits[i + 1])
        total += d1 * 10 + d2
        i += 2
    print(total)


def solve_day_1_part_2():
    regex = '(one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9)'
    regex_partial_rev = ')one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9('
    map_vals = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        # 'zero': 0,
        # '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9
    }
    total = 0
    with open('./data/in/day-01-part-2.txt') as my_file:
        for line in my_file:
            results = re.findall(regex, line)
            first_digit = results[0]

            # Reverse the searched string, and the regex
            results = re.findall(regex_partial_rev[::-1], line[::-1])
            last_digit = results[0][::-1]

            val = map_vals[first_digit] * 10 + map_vals[last_digit]
            print(f'{first_digit} + {last_digit} = {val}')
            total = val + total
    print(total)


if __name__ == '__main__':
    solve_day_1_part_2()
