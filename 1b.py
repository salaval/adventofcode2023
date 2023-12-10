digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
rdigits = [digit[::-1] for digit in digits]

def scan(s: str, r: bool = False):
    active_index = [0]*9
    if r:
        s = reversed(s)
        currdigits = rdigits
    else:
        currdigits = digits
    for c in s:
        print(c, active_index)
        if c.isdigit():
            return c
        for i, digit in enumerate(currdigits):                
            if c == digit[active_index[i]]:
                if active_index[i] + 1 == len(digit):
                    return str(i + 1)
                else:
                    active_index[i] += 1
            elif c == digit[0]:
                active_index[i] = 1
            else:
                active_index[i] = 0


def rscan(s: str):
    return scan(s, True)

with open("input") as f:
    sum = 0
    toprint = False
    for line in f:
        s = scan(line) + rscan(line)
        assert len(s) == 2
        assert s[0].isdigit() and s[1].isdigit()
        assert s[0] != 0 and s[1] != 0
        sum = sum + int(s)
        #print(line)
        if sum == 11320:
            toprint = True
        if toprint:
            print(line)
            print(s)
        if sum > 12500:
            toprint = False
        #print(int(scan(line) + rscan(line)))
        #input()
    print(sum)
