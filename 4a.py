with open("input", "r") as file:
    sum = 0
    for line in file:
        winning_numbers = set()
        points = 0
        right_part = False
        for token in line.split():
            if token == "|":
                right_part = True
            if right_part:
                if token in winning_numbers:
                    if points == 0:
                        points = 1
                    else:
                        points *= 2
            elif token.isdigit():
                winning_numbers.add(token)
        print(points)
        sum += points
    print("Total sum:", sum)