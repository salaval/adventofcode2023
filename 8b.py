from math import lcm

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

    path = "".join(path.split())
    startnodes = []
    endnodes = []
    for node in nodes:
        if node[-1] == "A":
            startnodes.append(node)
        if node[-1] == "Z":
            endnodes.append(node)

    print(len(startnodes), "distinct start nodes")
    cycles = []

    for start_node in startnodes:
        print("Start node", start_node)
        #input()
        pathlen = len(path)
        curr_node = start_node
        steps = 0
        direction = path[steps % pathlen]
        curr_node = nodes[curr_node][direction]
        steps += 1

        prologue_detected = False
        prologue_steps = 0
        cycle_detected = False
        while not cycle_detected:

            if prologue_detected and curr_node == end_node:
                cycle_detected = True
                #print("End node after", steps," steps.", curr_node)
                break
            elif prologue_detected and curr_node in endnodes:
                print("Detected another endnode in the cycle!")
            elif curr_node in endnodes:
                prologue_detected = True
                prologue_steps = steps
                end_node = curr_node
                print("Prologue of length", steps)

            direction = path[steps % pathlen]
            steps = steps+1
            curr_node = nodes[curr_node][direction]
        cycle_steps = steps-prologue_steps
        print("Cycle of length", steps-prologue_steps)
        assert prologue_steps == cycle_steps
        cycles.append(cycle_steps)

    print(cycles)

    def lcm_list(nums):
        if len(nums) == 2:
            return lcm(nums[0], nums[1])
        else:
            return lcm(nums[0], lcm_list(nums[1:]))
        
    total_steps = lcm_list(cycles)
    print("Total required steps:", total_steps)