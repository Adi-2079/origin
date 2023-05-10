import random

briefcases = list(range(1,27))
winning_amounts = [0.01, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10000, 250000, 500000, 750000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000]
chosen_cases = []
players = []
multiplayer = ()

def print_board():
    print("Here are the remaining briefcases:")
    for briefcase in briefcases:
        if briefcase not in chosen_cases:
            print(briefcase, end='')
    print("\n")

def offer():
    total_winning_amount = sum(winning_amounts)
    average_winning_amount= total_winning_amount / len(briefcases)
    offer_amount = round(average_winning_amount * 0.5, 2 )
    return offer_amount

def play_game():
    num_players = int(input("How many players? "))

    for i in range(num_players):
        player_name = input(f"What is player {i+1}'s name? ")
        players.append(player_name)

for player_name in players:
    chosen_case = random.choice(briefcases)
    chosen_cases.append(chosen_case)
    briefcases.remove(chosen_case)
    print(f"{player_name}, your chosen briefcase is: {chosen_case}")

num_rounds = 6
for round_num in range(num_rounds):
    print(f"\n\nRound {round_num+1}")
    print_board()
    for player_num, player_name in enumerate(players):
        print(f"\n{player_num}, it's your turn!")
        chosen_briefcase = int(input("Which briefcase do you choose? "))
        briefcases.remove(chosen_briefcase)
        winning_amount = winning_amounts.pop(random.randrange(len(winning_amounts)))
        print(f"You have won ${winning_amount}!")
        if chosen_briefcase == chosen_cases[player_num]:
            print(f"\n{player_name}, you have won ${winning_amount} and your orginial briefcase is worth ${chosen_briefcase}!")
              