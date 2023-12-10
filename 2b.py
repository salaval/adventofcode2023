import re

game_p = "Game (\d+):"
blue_p = "(\d+) blue"
red_p = "(\d+) red"
green_p = "(\d+) green"

with open("input") as file:
    sum = 0
    for line in file:
        game_c = re.search(game_p, line).group(1)
        blue_c = [int(n) for n in re.findall(blue_p, line)]
        red_c = [int(n) for n in re.findall(red_p, line)]
        green_c = [int(n) for n in re.findall(green_p, line)]
        power = max(blue_c) * max(red_c) * max(green_c) 
        print("Power for game", game_c, ":", power)
        sum += power
    print("Total:", sum)