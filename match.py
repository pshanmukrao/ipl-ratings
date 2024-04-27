from ipl_team import IPLTeam


class Match:
    def __init__(self, ID, City, Date, Season, MatchNumber, Team1, Team2, Venue, TossWinner, WinningTeam,
                 Player_of_Match):
        self.ID = ID
        self.City = City
        self.Date = Date
        self.Season = Season
        self.MatchNumber = MatchNumber
        self.Team1 = IPLTeam.get(Team1)
        self.Team2 = IPLTeam.get(Team2)
        self.Venue = Venue
        self.TossWinner = IPLTeam.get(TossWinner)
        self.WinningTeam = IPLTeam.get(WinningTeam)
        self.Player_of_Match = Player_of_Match

    def __str__(self):
        return f"Match(ID={self.ID}, City={self.City}, Date={self.Date}, Season={self.Season}, MatchNumber={self.MatchNumber}, Team1={self.Team1}, Team2={self.Team2}, Venue={self.Venue}, TossWinner={self.TossWinner}, WinningTeam={self.WinningTeam}, Player_of_Match={self.Player_of_Match})"
