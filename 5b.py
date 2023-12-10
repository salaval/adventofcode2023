import re
import numpy as np
from queue import Queue

def map_interval(pair, interval):
    width = pair[1]
    offset = pair[0] - interval[1]
    mapping = interval[0] + offset
    return (mapping, width)


def map_intervals(sources: Queue, map):
    debug = False
    targets = Queue()
    while not sources.empty():
        pair = sources.get()
        if debug: print(pair)
        lbound_num, rbound_num = pair[0], pair[0]+pair[1]
        untouched = True
        for interval in map:
            lbound_interval = interval[1]
            rbound_interval = interval[1]+interval[2]
            interval_width = interval[2]
            if lbound_interval <= lbound_num and rbound_num <= rbound_interval:
                #Entire source is contained in this interval. Map it.
                if debug: print("Case 1")
                mapping = map_interval(pair, interval)
                targets.put(mapping)
                untouched = False
                break
            elif rbound_num < lbound_interval or rbound_interval < lbound_num:
                #Entire source is outside of this interval. Keep the source as it is.
                if debug: print("Case 2")
                continue
            elif lbound_num < lbound_interval and rbound_interval < rbound_num:
                #The source stretches outside of the interval on both sides. Map the interior and keep the rest.
                if debug: print("Case 3")
                mapping = map_interval((lbound_interval, interval_width), interval)
                targets.put(mapping)
                sources.put((lbound_num, lbound_interval-lbound_num))
                sources.put((rbound_interval, rbound_num-rbound_interval))
                untouched = False
                break
            elif lbound_num < lbound_interval and rbound_num < rbound_interval and rbound_num-lbound_interval != 0:
                #Some numbers to the left of the interval
                if debug: print("Case 4")
                mapping = map_interval((lbound_interval, rbound_num-lbound_interval), interval)
                targets.put(mapping)
                sources.put((lbound_num, lbound_interval-lbound_num))
                untouched = False
                break
            elif lbound_interval < lbound_num and rbound_interval < rbound_num and rbound_interval-lbound_num != 0:
                #Some numbers to the right of the interval
                if debug: print("Case 5")
                mapping = map_interval((lbound_num, rbound_interval-lbound_num), interval)
                #print("Target <- ", mapping)
                targets.put(mapping)
                sources.put((rbound_interval, rbound_num-rbound_interval))
                untouched = False
                #print("Source <- ", (rbound_interval, rbound_num-rbound_interval))
                #input()
                break
        if untouched:
            # This should only be reached if the current source interval is totally outside of mapping intervals.
            targets.put(pair)
    print("Number of intervals:", targets.qsize())
    return targets



seed_pattern = "seeds:"
map_pattern = ".+ map:"
seeds = []
map = []
maps = []

with open("input", "r") as file:
    for line in file:
        if re.match(seed_pattern, line):
            print("Matched seed")
            for token in line.split():
                if token.isdigit():
                    seeds.append(int(token))
            pos = [elem for i, elem in enumerate(seeds) if i % 2 == 0]
            width = [elem for i, elem in enumerate(seeds) if i % 2 == 1]
            nums = list(zip(pos, width))
        elif re.search(map_pattern, line):
            print("Matched map")
            map = []
        else:
            print("Matched nothing")
            if not line.isspace():
                map_line = []
                for token in line.split():
                    if token.isdigit():
                        map_line.append(int(token))
                map.append(map_line)
            elif map:
                maps.append(map)
                print(map)

if map:
    maps.append(map) #Because the last line was not read for some reason?

print(nums)

sources = Queue()
[sources.put(pair) for pair in nums]

print(maps)
for map in maps:
    print()
    print("NEW MAP:")
    targets = map_intervals(sources, map)
    sources = targets

min_location = 9223372036854775807
while not sources.empty():
    interval = sources.get()
    print(interval)
    if interval[0] < min_location:
        min_location = interval[0]
print("Min location:", min_location)
    