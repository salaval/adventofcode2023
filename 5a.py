import re
import numpy as np

def avbilda(nums, map):
    #for num in nums:
    target = nums.copy()
    map = np.expand_dims(map, -1)
    source_distances = nums - map[:,1]
    allowed_distances = map[:,2]
    in_interval = np.logical_and(source_distances >= 0, source_distances < allowed_distances)
    source_in_some_interval = in_interval.any(axis=0)
    which_interval = np.where(in_interval)[0]
    target_range_start = map[which_interval,0,].squeeze()
    target[source_in_some_interval] = target_range_start + source_distances[in_interval]
    return target

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
            nums = np.array(seeds)
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
                maps.append(np.array(map))
                print(map)

if map:
    maps.append(np.array(map)) #Because the last line was not read for some reason?

#print(maps)
for map in maps:
    nums = avbilda(nums, map)
    print(nums)
print(min(nums))


#nums = np.array([79, 14, 55, 13])
#map = np.array([[50, 98, 2], [52, 50, 48]])

#avbilda(nums, map)