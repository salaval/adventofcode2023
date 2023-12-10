
with open("input", "r") as file:
    nodes = dict()
    for steps, line in enumerate(file):
        if steps == 0:
            path = line
        elif not line.isspace():
            node = line[0:3]
            left = line[7:10]
            right = line[12:15]
            nodes[node] = {'L': left, 'R': right}
    print(nodes)
    print(path)
    path = "".join(path.split())
    curr_node = "AAA"
    end_node = "ZZZ"
    steps = 0
    pathlen = len(path)
    while curr_node != end_node:
        direction = path[steps % pathlen]
        print(steps, direction)
        steps = steps+1
        curr_node = nodes[curr_node][direction]
    print("Steps:", steps)