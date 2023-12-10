import re

with open("input") as file:
    sum = 0
    prev = None
    curr = file.readline()
    next = file.readline()
    while curr:
        symbol_pos = set()
        if prev:
            for symbol in re.finditer("[^.\d\n]", prev):
                symbol_pos.add(symbol.span()[0])
        if next:
            for symbol in re.finditer("[^.\d\n]", next):
                symbol_pos.add(symbol.span()[0])
        if curr:
            for symbol in re.finditer("[^.\d\n]", curr):
                symbol_pos.add(symbol.span()[0])
            #print("Checking line:", curr, "Symbols:", symbol_pos)
            for m in re.finditer("\d+", curr):
                left = m.span()[0]-1
                right = m.span()[1]
                #print(left, right)
                if any([left <= symbol <= right for symbol in symbol_pos]):
                    #This number is a machine part.
                    part_no = m.group()
                    sum += int(part_no)
                    print("Part", part_no)
                else:
                    print("Not part", m.group())

        prev = curr
        curr = next
        next = file.readline()
    print("Sum: ", sum)