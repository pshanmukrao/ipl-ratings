from ipl_team import IPLTeam


def calculate_dynamic_kfactor(team_rating):
    """
    Calculates a dynamic K-factor based on team rating.

    Args:
        team_rating (float): Current rating of the team.

    Returns:
        float: Dynamic K-factor.
    """
    # Define rating thresholds for different K-factors
    low_rating_threshold = 1400
    high_rating_threshold = 2000

    if team_rating < low_rating_threshold:
        return 40
    elif team_rating > high_rating_threshold:
        return 16
    else:
        # Linear interpolation between low and high thresholds
        slope = (16 - 40) / (high_rating_threshold - low_rating_threshold)
        return 40 + slope * (team_rating - low_rating_threshold)


def calculate_elo_rating(team1: IPLTeam, team2: IPLTeam, winning_team: IPLTeam):
    """
    Calculates the updated Elo rating for two teams after a match.

    Args:
        team1 (IPLTeam): Team 1.
        team2 (IPLTeam): Team 2.
        winning_team (IPLTeam): Winning team.

    Returns:
        tuple: Updated ratings for team 1 and team 2.
    """
    result = 1 if team1 == winning_team else 0

    team1_rating = team1.rating
    team2_rating = team2.rating
    k_factor_team1 = calculate_dynamic_kfactor(team1_rating)
    k_factor_team2 = calculate_dynamic_kfactor(team2_rating)

    expected_score_team1 = 1 / (1 + 10 ** ((team2_rating - team1_rating) / 400))
    expected_score_team2 = 1 - expected_score_team1

    updated_rating_team1 = team1_rating + k_factor_team1 * (result - expected_score_team1)
    updated_rating_team2 = team2_rating + k_factor_team2 * ((1 - result) - expected_score_team2)

    team1.rating = updated_rating_team1
    team2.rating = updated_rating_team2
