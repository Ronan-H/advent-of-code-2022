
calories = 0
calories_max = 0

with open('./input') as file:
    for line in file:
        line = line.rstrip()
        if len(line) == 0:
            calories_max = max(calories, calories_max)
            calories = 0
        else:
            calories += int(line)

print(calories_max)