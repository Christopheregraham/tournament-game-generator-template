# Write your code here.

def get_number_of_teams():
    team_num = 0
    while team_num < 2:
        try:
            team_num = int(
                input("Enter the number of teams in the tournament: "))
            if team_num < 2:
                print("The value must be greater than or equal to 2.")
        except ValueError:
            print("Please enter a valid interger.")
    return team_num


def get_team_names(num_teams):
    teams = []
    i = 1
    while len(teams) != num_teams:
        team_name = input(f"Enter the name for team #{i}: ")
        if len(team_name) >= 2 and team_name.count(" ") <= 1:
            teams.append(team_name)
            i += 1
        elif len(team_name) < 2:
            print("Team names must have at least 2 characters, try again.")
        elif team_name.count(" ") > 1:
            print("Team names may have at most 2 words, try again.")
    return teams


def get_number_of_games_played(num_teams):
    game_num = 0
    while game_num < 1:
        try:
            game_num = int(
                input("Enter the number of games played by each team: "))
            if game_num < 1:
                print(
                    "Invalid number of games. Each team plays each other at least once in the regular season, try again.")
        except ValueError:
            print("Please enter a valid interger.")
    return game_num


def get_team_wins(team_names, games_played):
    team_record = {}
    i = 0
    while len(team_names) != len(team_record):
        team = team_names[i]
        wins = input(f"Enter the number of wins Team {team} had: ")
        if wins.isdigit() and int(wins) >= 0 and int(wins) <= games_played:
            team_record[team] = wins
            i += 1
        else:
            print(f"Please enter a valid number, less than the {games_played}")
    return team_record


# It is not necessary to use the functions defined above. There are simply here
# to help give your code some structure and provide a starting point.
num_teams = get_number_of_teams()
team_names = get_team_names(num_teams)
games_played = get_number_of_games_played(num_teams)
team_wins = get_team_wins(team_names, games_played)

print("Generating the games to be played in the first round of the tournament...")


def create_tournament_bracket(team_wins):
    sorted_teams = sorted(team_wins.items(), key=lambda x: x[1], reverse=True)
    num_teams = len(sorted_teams)
    matchups = []

    for i in range(num_teams // 2):
        home_team = sorted_teams[i][0]
        away_team = sorted_teams[num_teams - i - 1][0]
        matchup = f"Home: {home_team} VS Away: {away_team}"
        matchups.append(matchup)

    return matchups


matchups = create_tournament_bracket(team_wins)

for matchup in matchups:
    print(matchup)
