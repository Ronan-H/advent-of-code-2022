
calories = 0
calorie_sums = []

with open('./input') as file:
    for line in file:
        line = line.rstrip()
        if len(line) == 0:
            calorie_sums.append(calories)
            calories = 0
        else:
            calories += int(line)

print(sum(sorted(calorie_sums)[-3:]))