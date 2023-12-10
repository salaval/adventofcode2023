import numpy as np

def add_adj(adj_mat, pos, new_adj):
    if not adj_mat[pos][0].any():
        adj_mat[pos][0] = new_adj
    elif not adj_mat[pos][1].any():
        adj_mat[pos][1] = new_adj
    else:
        print("Fatal: more than two adjacencies!")

def add_tuples(a, b):
    return (a[0] + b[0], a[1] + b[1])

def apply_four(func, occ_mat, pos, token):
    func(occ_mat, add_tuples(pos, (0,1)), token)
    func(occ_mat, add_tuples(pos, (0,-1)), token)
    func(occ_mat, add_tuples(pos, (1,0)), token)
    func(occ_mat, add_tuples(pos, (-1,0)), token)

def flood_fill(occ_mat, pos, token):
    #print(pos)
    #print(occ_mat.shape)
    #print(pos >= occ_mat.shape)
    #print([pos[i] >= occ_mat.shape[i] for i in range(len(pos))])
    if pos == (74, 58):
        pass
    if any([pos[i] >= occ_mat.shape[i] for i in range(len(pos))]):
        return
    elif occ_mat[pos] == "B":
        return
    elif occ_mat[pos] == "X":
        return
    elif occ_mat[pos] == "P":
        print("Fill", token)
        occ_mat[pos] = token
        apply_four(flood_fill, occ_mat, pos, token)
    elif occ_mat[pos] == token:
        return
    elif occ_mat[pos] == ".":
        print("Fill", token)
        occ_mat[pos] = token
        apply_four(flood_fill, occ_mat, pos, token)
        return
    else:
        print("Error in flood fill:", pos, occ_mat[pos], token)
        return
        
def rotate_left(vec):
    y, x = vec[0], vec[1]
    if y == 0:
        y = x
        x = 0
    elif x == 0:
        x = -y
        y = 0
    else:
        print("error in rotate_left")
    return (y, x)

def rotate_right(vec):
    y, x = vec[0], vec[1]
    if y == 0:
        y = -x
        x = 0
    elif x == 0:
        x = y
        y = 0
    else:
        print("error in rotate_left")
    return (y, x)

with open("input", "r") as file:
    lines = []
    occ_lines = []
    for y, line in enumerate(file):
        adj = []
        occ = []
        for x, token in enumerate(line):
            match token:
                # [Y, X]
                case ".":
                    adj.append([[None, None], [None, None]])
                    occ.append(".")
                case "|":
                    adj.append([[-1, 0], [1, 0]])
                    occ.append("P")
                case "-":
                    adj.append([[0, -1], [0, 1]])
                    occ.append("P")
                case "L":
                    adj.append([[0, 1], [-1, 0]])
                    occ.append("P")
                case "F":
                    adj.append([[0, 1], [1, 0]])
                    occ.append("P")
                case "J":
                    adj.append([[0, -1], [-1, 0]])
                    occ.append("P")
                case "7":
                    adj.append([[0, -1], [1, 0]])
                    occ.append("P")
                case "S":
                    start_pos = (y, x)
                    adj.append([[None, None], [None, None]])
                    occ.append("P")
        lines.append(adj)
        occ_lines.append(occ)
    print(lines)
    adj_mat = np.array(lines)
    occ_mat = np.array(occ_lines)
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
    dir = None
    right_turns = 0
    while not loop_completed:
        #input()
        #print()
        #print(pos)
        adjs = adj_mat[pos]
        for adj in adjs:
            if (pos+adj != prev_pos).any():
                next_pos = tuple(pos+adj)
        #print("Next:", next_pos)
        prev_dir = dir
        prev_pos = pos
        pos = next_pos
        steps += 1

        dir = (pos[0] - prev_pos[0], pos[1] - prev_pos[1])
        occ_mat[pos] = "B"

        if prev_dir and rotate_right(prev_dir) == dir:
            right_turns += 1
        elif prev_dir and rotate_left(prev_dir) == dir:
            right_turns -= 1
        
        if (pos == start_pos):
            loop_completed = True
            break

    if right_turns > 0: #right lap, count "R" tokens
        token = "R"
    else:
        token = "L"

    loop_completed = False
    while not loop_completed:
        #input()
        adjs = adj_mat[pos]
        for adj in adjs:
            if (pos+adj != prev_pos).any():
                next_pos = tuple(pos+adj)
        #print("Next:", next_pos)
        prev_dir = dir
        prev_pos = pos
        pos = next_pos
        dir = (pos[0] - prev_pos[0], pos[1] - prev_pos[1])

        try:
            if token == "L":
                flood_fill(occ_mat, add_tuples(prev_pos, rotate_left(dir)), "L")
                flood_fill(occ_mat, add_tuples(prev_pos, rotate_left(prev_dir)), "L")
            elif token == "R":
                flood_fill(occ_mat, add_tuples(prev_pos, rotate_right(dir)), "R")
                flood_fill(occ_mat, add_tuples(prev_pos, rotate_right(prev_dir)), "R")
        except:
            print("Error! Pos is", pos)
            input()
        np.savetxt("out_temp", occ_mat, fmt="%s")
        #print(occ_mat)

        if (pos == start_pos):
            loop_completed = True
            break


    
    internal_pos = np.count_nonzero(occ_mat == token)

    print("Steps to complete loop:", steps)
    print("Max distance:", steps // 2)
    print("Right_turns:", right_turns)
    print("Internal positions:", internal_pos)

    #print(occ_mat)
    np.savetxt("out", occ_mat, fmt="%s")

    #print(occ_mat)