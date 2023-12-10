import re

# Return numbers which are adjacent to the symbol at position pos
def adjacent(spans, pos):
    return [span for span in spans if span[0][0]-1 <= pos <= span[0][1]]

with open("input") as file:
    sum = 0
    prev = None
    curr = file.readline()
    next = file.readline()
    while curr:
        numbers_pos = list()
        if prev:
            for number in re.finditer(r"(\d+)", prev):
                numbers_pos.append((number.span(), number.group()))
        if next:
            for number in re.finditer(r"(\d+)", next):
                numbers_pos.append((number.span(), number.group()))
        if curr:
            for number in re.finditer(r"(\d+)", curr):
                numbers_pos.append((number.span(), number.group()))
            
            #print("Checking line:", curr, "Symbols:", symbol_pos)
            for m in re.finditer("\*", curr):
                #print("Found * at pos", m.span()[0])
                #print("Comparing with numbers at pos", numbers_pos)
                adjacent_nums = adjacent(numbers_pos, m.span()[0])
                
                if len(adjacent_nums) == 2:
                    gear_ratio = int(adjacent_nums[0][1]) * int(adjacent_nums[1][1])
                    print("Gear:", adjacent_nums, gear_ratio)
                    sum += gear_ratio


        prev = curr
        curr = next
        next = file.readline()
    print("Sum: ", sum)