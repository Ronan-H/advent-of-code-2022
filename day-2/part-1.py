
hand_values = {
    'A': 0,
    'B': 1,
    'C': 2,
    'X': 0,
    'Y': 1,
    'Z': 2
}

winning_hands = {
    0: 2, # rock -> scissors
    1: 0, # paper -> rock
    2: 1, # scissors -> paper
}

lose_points = 0
draw_points = 3
win_points = 6

def calc_points(opp, you):
    opp_hand = hand_values[opp]
    you_hand = hand_values[you]

    points = 0

    if opp_hand == you_hand:
        points += draw_points
    elif winning_hands[you_hand] == opp_hand:
        points += win_points
    else:
        points += lose_points
    
    points += you_hand + 1
    
    return points

with open('./input') as file:
    print(sum(calc_points(line[0], line[2]) for line in file.readlines()))
