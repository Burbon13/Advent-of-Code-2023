def solve_day_4_part_1():
    total = 0
    with open('./data/in/day-04-part-1.txt') as my_file:
        for line in my_file:
            left, actual_numbers_str = line.strip().split('|')
            card, win_numbers_str = left.strip().split(':')
            win_numbers_int = [int(x) for x in win_numbers_str.strip().split(' ') if x != '']
            actual_numbers_int = [int(x) for x in actual_numbers_str.strip().split(' ') if x != '']
            matches = sum([1 for x in actual_numbers_int if x in win_numbers_int])
            if matches > 0:
                total += 2 ** (matches - 1)
    print('Part 1:', total)
    print()


def solve_day_4_part_2():
    total = 0
    number_cards = {}
    with open('./data/in/day-04-part-1.txt') as my_file:
        for card_number, line in enumerate(my_file):
            if card_number not in number_cards:
                number_cards[card_number] = 1
            multiplier = number_cards.get(card_number, 1)

            left, actual_numbers_str = line.strip().split('|')
            card, win_numbers_str = left.strip().split(':')
            win_numbers_int = [int(x) for x in win_numbers_str.strip().split(' ') if x != '']
            actual_numbers_int = [int(x) for x in actual_numbers_str.strip().split(' ') if x != '']
            matches = sum([1 for x in actual_numbers_int if x in win_numbers_int])

            for x in range(card_number + 1, card_number + 1 + matches):
                existing = number_cards.get(x, 1)
                number_cards[x] = existing + multiplier

    print('Part 2:', sum([number_cards[x] for x in number_cards]))


if __name__ == '__main__':
    solve_day_4_part_1()
    solve_day_4_part_2()
