from math import sqrt, floor, ceil
import re

def find_zero(tmax, dmax):
    t1 = (1/2)*tmax - sqrt((1/4)*tmax**2 - dmax)
    t2 = (1/2)*tmax + sqrt((1/4)*tmax**2 - dmax)
    return (t1, t2)

with open("input", "r") as file:
    for line in file:
        tokens = line.split()
        if "Time" in tokens[0]:
            tmaxs = tokens[1:]
        elif "Distance" in tokens[0]:
            dmaxs = tokens[1:]
        else:
            print("Fatal")

    print(tmaxs)
    print(dmaxs)
    product = 1
    eps = 0.00001
    for i in range(len(tmaxs)):
        t1, t2 = find_zero(int(tmaxs[i]), int(dmaxs[i]))
        print(t1, t2)
        num_wins = floor(t2-eps)-ceil(t1+eps)+1
        product *= num_wins
        print(num_wins)
    print("Total:", product)