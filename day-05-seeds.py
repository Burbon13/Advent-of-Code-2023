def read_day_5_data():
    with open('./data/in/day-05-part-1.txt') as my_file:
        seeds = [int(x) for x in my_file.readline().split(':')[1].strip().split(' ')]
        mappings = []
        temp_holder = []
        for line in my_file:
            line = line.strip()
            if line == '':
                continue
            if line[0].isalpha():
                _from, _, _to = line.split(' ')[0].split('-')
                if len(temp_holder) > 0:
                    mappings.append(temp_holder)
                    temp_holder = []
            else:
                dest_start, source_start, length = [int(x) for x in line.split(' ')]
                # Why is the destination first ? ...
                temp_holder.append((dest_start, source_start, length))
    if len(temp_holder) > 0:
        mappings.append(temp_holder)
        temp_holder = []
    return seeds, mappings


def compute_destination_single_seed(seed, mappings):
    position = seed
    for mapping_level in mappings:
        for dest_start, source_start, length in mapping_level:
            if source_start <= position < source_start + length:
                position = dest_start + (position - source_start)
                break
    return position


def solve_day_5_part_1():
    print('Part 1')
    seeds, mappings = read_day_5_data()
    min_dest = min([compute_destination_single_seed(seed, mappings) for seed in seeds])
    print("Min Destination:", min_dest)


def retrieve_min(locations):
    print(locations)
    values = []
    index = 0
    while index < len(locations):
        values.append(locations[index][0])
        index += 2
    return min(values)


def compute_intersection(one_location, one_mapping):
    print(f'one_location:{one_location}')
    print(f'one_mapping:{one_mapping}')

    location_left = one_location[0]
    location_right = one_location[0] + one_location[1] - 1
    begin_map_left = one_mapping[1]
    begin_map_right = one_mapping[1] + one_mapping[2] - 1
    dif_delta = one_mapping[0] - one_mapping[1]

    int_left = max(location_left, begin_map_left)
    int_right = min(location_right, begin_map_right)
    if int_left <= int_right:
        delta = int_right - int_left + 1
        new_left = int_left + dif_delta
        print(f'result:{(new_left, delta)}')
        return new_left, delta
    print(f'result:None')
    return None


def compute_part_2(locations, mappings):
    if len(mappings) == 0:
        return retrieve_min(locations)

    current_level_mapping = mappings[0]

    new_locations = []
    # Intersect with current mappings
    for one_location in locations:
        for one_mapping in current_level_mapping:
            result = compute_intersection(one_location, one_mapping)
            if result is not None:
                new_locations.append(result)
    # Intersect with exterior identity mapping
    leftmost = min([v[0] for v in current_level_mapping])
    rightmost = max([v[0] + v[2] for v in current_level_mapping])  # Excluding
    for one_location in locations:
        left = one_location[0]
        right = one_location[0] + one_location[1] - 1
        if left < leftmost:
            new_locations.append((left, leftmost - left))
        if right > rightmost:
            new_locations.append((right, right - rightmost))
    print('left-right', leftmost, rightmost)

    return compute_part_2(new_locations, mappings[1:])


def solve_day_5_part_2():
    seeds, mappings = read_day_5_data()
    locations = []
    index = 0
    while index < len(seeds):
        locations.append((seeds[index], seeds[index + 1]))
        index += 2
    result = compute_part_2(locations, mappings)
    print('Part 2:', result)


if __name__ == '__main__':
    solve_day_5_part_1()
    solve_day_5_part_2()
