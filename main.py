import json

def save_scores_to_file(scores_info, filename):
    with open(filename, 'w') as file:
        json.dump(scores_info, file, indent=4)

def load_scores_from_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def main():
    filename = "scores_info.json"
    try:
        scores_info = load_scores_from_file(filename)
    except FileNotFoundError:
        scores_info = {
            "First Team": 100,
            "Second Team": 90,
            "Third Team": 80,
            "Fourth Team": 50,
            "Fifth Team": 30,
        }
        save_scores_to_file(scores_info, filename)

    team_list = [
        input(f"{i+1}. Enter team name (First Team, Second Team, Third Team, Fourth Team, Fifth Team): \n")
        for i in range(5)
    ]

    if position_checker(scores_info, team_list):
        print("Team positions correct!")
    else:
        print("Team positions incorrect!")

def position_checker(scores_info: dict, team_list: list) -> bool:
    sorted_teams = sorted(scores_info.keys(), key=lambda x: scores_info[x], reverse=True)
    return sorted_teams == team_list

if __name__ == '__main__':
    main()
