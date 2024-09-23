# Assigning name to "Team"
team = "Toronto Blue Jays"
# Assigning a certain date to the current date
current_date = "July 18, 2021"
# Assigning a certain name to the player
player = "Vladimir Guerrero Jr."
# Assigning a set number
home_runs_to_date = 31
games_played = 88
total_season_games = 162
home_run_record = 73

games_remaining = total_season_games - games_played
home_runs_per_game = home_runs_to_date / games_played
projected_home_runs = home_runs_per_game * total_season_games
can_break_record = projected_home_runs > home_run_record

print(f"{player} of the {team}")
print(f"currently has {home_runs_to_date} home runs as of {current_date}.")
print(f"The current MLB record for most home runs in a season is {home_run_record}.")
print(f"With {games_remaining} games remaining and an average of {round(home_runs_per_game, 2)} home runs per game,")
print(f"it is {can_break_record} that he is on pace to break the record.")
print(f"{player} is projected to hit {round(projected_home_runs, 2)} home runs this season.")

# There are blank lines to make the code much easier to read. For instance, the first part shows the values, the second part shows the calculations, and the third part shows the results.

# The line games_remaining = total_season_games - games_played must be correct as if you have a total amount of something, and then minus something that's already been done, you can get the remaining amount, which is the total games remaining.