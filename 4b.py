def no_matches(scratchcard):
    winning_numbers = set()
    matches = 0
    right_part = False
    for token in scratchcard.split():
        if token == "|":
            right_part = True
        if right_part:
            if token in winning_numbers:
                matches += 1
        elif token.isdigit():
            winning_numbers.add(token)
    return(matches)

with open("input", "r") as file:
    for no_lines, line in enumerate(file):
        pass
    file.seek(0)
    scratchcards = 0
    copies = [1] * (no_lines+1)
    for i, scratchcard in enumerate(file):
        matches = no_matches(scratchcard)
        #print(matches)
        #print(copies)
        for j in range(matches):
            copies[i+1+j] += copies[i]
        #copies[i+1:i+2+matches] += [copies[i]]*matches

    print(copies)
    print(sum(copies))
