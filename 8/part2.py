import numpy as np

with open("input.txt") as f:
    contents = f.read().split("\n")
    directions = contents[0]

    node_map_as_list = [node.split(' = ') for node in contents[2:]]
    node_map_as_dict = {node: connected_nodes.strip('()').split(', ') for [node, connected_nodes] in node_map_as_list}
    starting_nodes = [node for node in node_map_as_dict if node[-1] == 'A']

    steps_to_destination_node = []
    for node in starting_nodes:
        number_of_steps = 0
        direction_index = 0
        while node[-1] != 'Z':
            if direction_index == len(directions):
                direction_index = 0

            direction = directions[direction_index]
            if direction == 'L':
                node = node_map_as_dict[node][0]
            if direction == 'R':
                node = node_map_as_dict[node][1]

            direction_index += 1
            number_of_steps += 1

        steps_to_destination_node.append(number_of_steps)

    print(np.lcm.reduce(steps_to_destination_node))
