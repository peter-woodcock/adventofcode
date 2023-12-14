def find_differences(list_of_readings, final_numbers_in_all_lists):
    if len(set(list_of_readings)) == 1:
        return final_numbers_in_all_lists
    else:
        differences = []
        for i in range(len(list_of_readings[:-1])):
            differences.append(list_of_readings[i+1] - list_of_readings[i])
        final_numbers_in_all_lists.append(differences[-1])
        return find_differences(differences, final_numbers_in_all_lists)


def find_next_value_for_differences(next_value, final_numbers_in_all_lists):
    if not final_numbers_in_all_lists:
        return next_value
    else:
        next_value = next_value + final_numbers_in_all_lists[-1]
        final_numbers_in_all_lists = final_numbers_in_all_lists[:-1]
        return find_next_value_for_differences(next_value, final_numbers_in_all_lists)


with open("input.txt") as f:
    lines = f.read().split("\n")
    running_total = 0
    for line in lines:
        readings = [int(reading) for reading in line.split()]
        final_numbers_in_all_lists = find_differences(readings, [readings[-1]])
        running_total += find_next_value_for_differences(0, final_numbers_in_all_lists)
    print(running_total)

