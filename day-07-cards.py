card_power_mapping = {
    'A': 20, 'K': 19, 'Q': 18, 'J': 2, 'T': 16,
    '9': 15, '8': 14, '7': 13, '6': 12, '5': 11,
    '4': 10, '3': 9, '2': 8
}


def compute_power_of_hand(hand):
    per_card_power = [card_power_mapping[card] for card in hand]
    cards_dict = {}
    jokers = 0
    for card in hand:
        if card != 'J':
            cards_dict[card] = cards_dict.get(card, 0) + 1
        else:
            jokers += 1

    type_power = -1
    counters = sorted(cards_dict.values())
    # We may have a hand full of jokers. Are you joking? :)
    if len(counters) == 0:
        counters = [0]
    # Add the jokers to the most powerful group
    counters[-1] = counters[-1] + jokers
    if counters == [5]:
        type_power = 10
    elif counters == [1, 4]:
        type_power = 9
    elif counters == [2, 3]:
        type_power = 8
    elif counters == [1, 1, 3]:
        type_power = 7
    elif counters == [1, 2, 2]:
        type_power = 6
    elif counters == [1, 1, 1, 2]:
        type_power = 5
    elif counters == [1, 1, 1, 1, 1]:
        type_power = 4
    else:
        type_power = 3

    return type_power, per_card_power


def solve_day_7_part_1():
    with open('./data/in/day-07-part-1.txt') as my_file:
        data = []
        for line in my_file:
            hand, bid = line.strip().split(' ')
            data.append((hand, int(bid)))
        sorted_hands = sorted([(compute_power_of_hand(in_data[0]), in_data[1]) for in_data in data])
        result = 0
        for index, result_hand in enumerate(sorted_hands):
            result += (index + 1) * result_hand[1]
        print('Part 1:', result)


card_power_mapping_jokers = {
    'A': 20, 'K': 19, 'Q': 18, 'J': 3, 'T': 16,
    '9': 15, '8': 14, '7': 13, '6': 12, '5': 11,
    '4': 10, '3': 9, '2': 8
}


def solve_day_7_part_2():
    with open('./data/in/day-07-part-1.txt') as my_file:
        pass


if __name__ == '__main__':
    solve_day_7_part_1()
    solve_day_7_part_2()
