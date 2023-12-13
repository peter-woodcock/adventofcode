with open("test_input_1.txt") as f:
    contents = f.read().split("\n")
    directions = contents[0]

    node_map_as_list = [node.split(' = ') for node in contents[2:]]
    node_map_as_dict = {node: connected_nodes.strip('()').split(', ') for [node, connected_nodes] in node_map_as_list}

    number_of_steps = 0
    directions_index = 0
    current_node = 'AAA'
    while current_node != 'ZZZ':
        if directions_index == len(directions):
            directions_index = 0

        direction = directions[directions_index]
        if direction == 'L':
            current_node = node_map_as_dict[current_node][0]
        if direction == 'R':
            current_node = node_map_as_dict[current_node][1]

        directions_index += 1
        number_of_steps += 1

    print(number_of_steps)
