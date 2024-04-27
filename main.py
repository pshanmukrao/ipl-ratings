# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import csv
from typing import Iterator

from elo_rating import calculate_elo_rating
from ipl_team import IPLTeam
from match import Match


def read_matches(csv_fname: str) -> Iterator[Match]:
    with open(csv_fname, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield Match(ID=row["ID"], City=row["City"], Date=row["Date"], Season=row["Season"],
                        MatchNumber=row["MatchNumber"], Team1=row["Team1"], Team2=row["Team2"], Venue=row["Venue"],
                        TossWinner=row["TossWinner"], WinningTeam=row["WinningTeam"],
                        Player_of_Match=row["Player_of_Match"])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    wins = {}
    for match in read_matches("data/IPL_Matches_2008_2022.csv"):
        if match.WinningTeam is None:
            continue
        calculate_elo_rating(match.Team1, match.Team2, match.WinningTeam)
        wins[match.WinningTeam] = wins.get(match.WinningTeam, 0) + 1

    for team, win in wins.items():
        print(f"{team.team_name} wins {win} matches")

    for team in IPLTeam.dict.values():
        print(team)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
