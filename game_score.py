player_name=input("Enter player's name:")
games_played=int(input("Enter the number of games played:"))
score_achieved=int(input("Enter the total score achieved:"))

average_score=score_achieved/games_played

print(f"Player:{player_name}")
print(f"Games Played:{games_played}")
print(f"Total Score:{score_achieved}")
print(f"Average Score:{average_score}")    