# Number 1: I think the output says this because if you look at the code, you can clearly see the += symbols which signify a point being gained or lost, and the "both teams" section just means that if they're the same points at the end of the game, it will display that.
# Number 2: Elif is making it display another outcome if the variables were different, and else makes it like "otherwise, then" or if neither of the options in the if and the elif are met in the final outcome.
# Number 3: The word "Tie" appears. This is because its no longer accounting for if the first variable is incorrect, then it'll switch over to the next one, which means since both are now if statements, one will just keep increasing score until they both are tied.
team_a_points = 25
team_a_wins = 15

team_b_points = 20
team_b_wins = 16

if team_a_points > team_b_points:
    print("Team A wins!")
    team_a_wins += 1
elif team_b_points > team_a_points:
    print("Team B wins!")
    team_b_wins += 1
else:
    print("Tie.")

if team_a_wins > team_b_wins:
    print("Team A has more wins than Team B.")
elif team_b_wins > team_a_wins:
    print("Team B has more wins than Team A.")
else:
    print("Both Teams A and B have the same number of wins.")
