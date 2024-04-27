INITIAL_RATING = 1000

# Over the period, teams have changed their names or restarted with a new name altogether with new investers.
team_alias = {
    "Punjab Kings": "Kings XI Punjab",
    "Deccan Chargers": "Sunrisers Hyderabad",
    "Delhi Daredevils": "Delhi Capitals",
    "Rising Pune Supergiant": "Rising Pune Supergiants",
    "Pune Warriors": "Rising Pune Supergiants",
    "Gujarat Lions": "Gujarat Titans",
}

class IPLTeam():
    dict = {}
    def __init__(self, team_name):
        self.team_name = team_name
        self.rating = INITIAL_RATING

    @classmethod
    def get(cls, team_name):
        if team_name in 'NA':
            return None
        team_name = team_alias.get(team_name, team_name)
        if team_name in cls.dict:
            return cls.dict[team_name]
        cls.dict[team_name] = cls(team_name)
        return cls.dict[team_name]

    def __str__(self):
        return f"IPLTeam(team_name={self.team_name}, ratings={self.rating})"
