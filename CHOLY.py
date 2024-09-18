X, Y, Z = map(int, input().split())

# Current points of your team
current_points = X * 1 + Y * 0.5

# Total games played
total_games_played = X + Y + Z

# Remaining games
remaining_games = 4 - total_games_played

# Calculate maximum potential points for your team
max_possible_points = current_points + remaining_games * 1  # Assuming winning all remaining games

# Calculate the maximum opponent score if they have the same played games
# We can't determine their exact score, but we need to ensure we can win.
# For the worst case, assume opponent also has some games with the potential for draws/wins.
# The minimum possible score of the opponent is if they won all their remaining games
opponent_points = (Z* 1 + Y * 0.5)  # Worst case where they could have not won any points.

# Your team can only win if your maximum potential score exceeds the opponent's score.
if max_possible_points > opponent_points:
    print("YES")
else:
    print("NO")
