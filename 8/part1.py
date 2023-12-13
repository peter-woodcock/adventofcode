with open("input.txt") as f:
    contents = f.read().split("\n")
    directions = contents[0]

    node_map_as_list = contents[2:]
    node_map_as_list = [node.split(' = ') for node in node_map_as_list]
    node_map_as_dict = {node: connected_nodes.strip('()').split(', ') for [node, connected_nodes] in node_map_as_list}

    starting_node = 'AAA'
    target_node = 'ZZZ'

    current_node = starting_node
    number_of_steps = 0
    direction_index = 0

    while current_node != 'ZZZ':
        if direction_index == len(directions):
            direction_index = 0
        direction = directions[direction_index]
        if direction == 'L':
            current_node = node_map_as_dict[current_node][0]
        if direction == 'R':
            current_node = node_map_as_dict[current_node][1]

        direction_index += 1
        number_of_steps += 1

    print(number_of_steps)
