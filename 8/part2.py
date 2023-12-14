import numpy as np


def calculate_steps_to_destination(node_map_as_dict, directions, starting_node):
    number_of_steps = 0
    direction_index = 0
    current_node = starting_node

    while current_node[-1] != 'Z':
        if direction_index == len(directions):
            direction_index = 0

        direction = directions[direction_index]
        current_node = node_map_as_dict[current_node][0] if direction == 'L' else node_map_as_dict[current_node][1]

        direction_index += 1
        number_of_steps += 1

    return number_of_steps


with open("input.txt") as f:
    contents = f.read().split("\n")
    directions = contents[0]

    node_map_as_list = [node.split(' = ') for node in contents[2:]]
    node_map_as_dict = {node: connected_nodes.strip('()').split(', ') for [node, connected_nodes] in node_map_as_list}
    starting_nodes = [node for node in node_map_as_dict if node[-1] == 'A']

    steps_to_destination_node = [calculate_steps_to_destination(node_map_as_dict, directions, node)
                                 for node in starting_nodes]

    steps_to_simultaneous_destinations = np.lcm.reduce(steps_to_destination_node)
    print(steps_to_simultaneous_destinations)
