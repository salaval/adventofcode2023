import numpy as np

def add_adj(adj_mat, pos, new_adj):
    if not adj_mat[pos][0].any():
        adj_mat[pos][0] = new_adj
    elif not adj_mat[pos][1].any():
        adj_mat[pos][1] = new_adj
    else:
        print("Fatal: more than two adjacencies!")

with open("test", "r") as file:
    lines = []
    for y, line in enumerate(file):
        adj = []
        for x, token in enumerate(line):
            match token:
                # [Y, X]
                case ".":
                    adj.append([[None, None], [None, None]])
                case "|":
                    adj.append([[-1, 0], [1, 0]])
                case "-":
                    adj.append([[0, -1], [0, 1]])
                case "L":
                    adj.append([[0, 1], [-1, 0]])
                case "F":
                    adj.append([[0, 1], [1, 0]])
                case "J":
                    adj.append([[0, -1], [-1, 0]])
                case "7":
                    adj.append([[0, -1], [1, 0]])
                case "S":
                    start_pos = (y, x)
                    adj.append([[None, None], [None, None]])
        lines.append(adj)
    print(lines)
    adj_mat = np.array(lines)
    if start_pos[0] != 0 and [1, 0] in adj_mat[start_pos[0]-1, start_pos[1]]:
        add_adj(adj_mat, start_pos, [-1, 0])
    if start_pos[0] != adj_mat.shape[0] and [-1, 0] in adj_mat[start_pos[0]+1, start_pos[1]]:
        add_adj(adj_mat, start_pos, [1, 0])
    if start_pos[1] != 0 and [0, 1] in adj_mat[start_pos[0], start_pos[1]-1]:
        add_adj(adj_mat, start_pos, [0, -1])
    if start_pos[1] != adj_mat.shape[1] and [0, -1] in adj_mat[start_pos[0], start_pos[1]+1]:
        add_adj(adj_mat, start_pos, [0, 1])

    print(adj_mat)
    print(adj_mat.shape)
    print(adj_mat[:,:,0,0])
    print(adj_mat[start_pos])

    print("~~~~")

    loop_completed = False
    pos = start_pos
    prev_pos = [None, None]
    steps = 0
    while not loop_completed:
        #input()
        print()
        print(pos)
        adjs = adj_mat[pos]
        for adj in adjs:
            if (pos+adj != prev_pos).any():
                next_pos = tuple(pos+adj)
        print("Next:", next_pos)
        prev_pos = pos
        pos = next_pos
        steps += 1
        
        if (pos == start_pos):
            loop_completed = True
            break
    print("Steps to complete loop:", steps)
    print("Max distance:", steps // 2)
    