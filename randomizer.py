import random

# List of baseball team names
teams = [
     "Cubs",
      "Indians"

]

# teams = [
#     "Yankees", "Red Sox", "Dodgers", "Cubs", "Giants", "Mets", "Cardinals", "Braves",
#     "Astros", "Phillies", "Nationals", "Brewers", "Rays", "Indians", "Athletics", "Twins",
#     "White Sox", "Padres", "Rangers", "Blue Jays", "Pirates", "Rockies", "Mariners", "Angels",
#     "Diamondbacks", "Orioles", "Royals", "Tigers", "Marlins", "Reds"
# ]

# Shuffle the teams
random.shuffle(teams)

# Assign one team to the person
person = teams[0]

# Print the assignment
print(f"Person: {person}")