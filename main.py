with open("rounds.txt", "r") as file:
    rounds = file.read().split("\n")

play_values_dict = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}

rocks = ["A", "X"]
papers = ["B", "Y"]
scissors = ["C", "Z"]

win = 6
draw = 3
lose = 0

def scorer(play_round: str) -> tuple:
    player_one_score = 0
    your_score = 0

    result = play_round.split()
    player_one = result[0]
    you = result[1]

    match you:
        case "X": # You must lose.
            if player_one == "A": # If rocks
                you = "C"
            elif player_one == "C": # If Scissors
                you = "B"
            else:
                you = "A"
        case "Y": # You must draw.
            you = player_one
        case "Z": # You must win
            if player_one == "C": # If Scissors be Rock
                you = "A"
            elif player_one == "B": # If Paper be scissors
                you = "C"
            else:
                you = "B"

    
    if (player_one in rocks) and (you in scissors):
        player_one_score = win + play_values_dict[player_one]
        your_score = lose + play_values_dict[you]
    elif (player_one in scissors) and (you in rocks):
        player_one_score = lose + play_values_dict[player_one]
        your_score = win + play_values_dict[you]
    elif (player_one in scissors) and (you in papers):
        player_one_score = win + play_values_dict[player_one]
        your_score = lose + play_values_dict[you]
        
    elif (player_one in papers) and (you in scissors):
        player_one_score = lose + play_values_dict[player_one]
        your_score = win + play_values_dict[you]
    elif (player_one in papers) and (you in rocks):
        player_one_score = win + play_values_dict[player_one]
        your_score = lose + play_values_dict[you]
    elif (player_one in rocks) and (you in papers):
        player_one_score = lose + play_values_dict[player_one]
        your_score = win + play_values_dict[you]
    else:
        player_one_score = draw + play_values_dict[player_one]
        your_score = draw + play_values_dict[you]

    return player_one_score, your_score

other_player = 0
you = 0
    
for play in rounds:
    other_player_result, you_result = scorer(play)
    other_player += other_player_result
    you += you_result

if other_player > you:
    print(f"You lost, the other player's score is: {other_player} and your score is: {you}")
elif other_player < you:
    print(f"You Won, the other player's score is: {other_player} and your score is: {you}")
else:
    print(f"It was a draw, the other player's score is: {other_player} and your score is: {you}")
