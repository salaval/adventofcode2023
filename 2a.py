import re

game_p = "Game (\d+):"
blue_p = "(\d+) blue"
red_p = "(\d+) red"
green_p = "(\d+) green"

blue_max = 14
red_max = 12
green_max = 13

with open("input") as file:
    sum = 0
    for line in file:
        game_c = re.search(game_p, line)
        blue_c = [int(n) for n in re.findall(blue_p, line)]
        red_c = [int(n) for n in re.findall(red_p, line)]
        green_c = [int(n) for n in re.findall(green_p, line)]
        if(max(blue_c)<= blue_max and max(red_c) <= red_max and max(green_c) <= green_max):
            print("Game", game_c[0], "OK")
            sum += int(game_c.group(1))
    print("Total:", sum)