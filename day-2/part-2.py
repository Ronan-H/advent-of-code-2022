
# Why waste time write lot code when few code do trick? ¯\_(ツ)_/¯
cheat_sheet = {
    'A X': 3,
    'A Y': 4,
    'A Z': 8,
    'B X': 1,
    'B Y': 5,
    'B Z': 9,
    'C X': 2,
    'C Y': 6,
    'C Z': 7
}

with open('./input') as file:
    print(sum(cheat_sheet[line.rstrip()] for line in file.readlines()))
