
import pandas as pd


def get_data(year):
    """Get the data for the season corresponding to the specified year"""
    link = f'https://www.nbastuffer.com/{year}-{year + 1}-nba-player-stats/'  # data source
    df = pd.read_html(link)[0]
    df = clean_data(df, year)
    return df


def clean_data(d, year):
    """Clean the specified dataframe for the specified year"""
    d['Year'] = year  # initial year

    if year in [2019, 2020, 2021]:
        d = d.rename(columns={
            "TO%Turnover RateA metric that estimates the number of turnovers a player commits per 100 possessions": "TO%"})
    elif year == 2018:
        d = d.rename(columns={
            "Tor%Turnover RateA metric that estimates the number of turnovers a player commits per 100 possessions": "TO%"})
    else:  # year == 2017:
        d = d.rename(columns={
            "TOrTurnover RateA metric that estimates the number of turnovers a player commits per 100 possessions": "TO%"})

    # clean up the verbose column names
    d = d.rename(columns={
        "FULL NAME": "NAME",
        "MIN%Minutes PercentagePercentage of team minutes used by a player while he was on the floor": "MIN%",
        "USG%Usage RateUsage rate, a.k.a., usage percentage is an estimate of the percentage of team plays used by a player while he was on the floor": "USG%",
        "eFG%Effective Shooting PercentageWith eFG%, three-point shots made are worth 50% more than two-point shots made. eFG% Formula=(FGM+ (0.5 x 3PM))/FGA": "eFG%",
        "TS%True Shooting PercentageTrue shooting percentage is a measure of shooting efficiency that takes into account field goals, 3-point field goals, and free throws.": "TS%",
        "PPGPointsPoints per game.": "PPG",
        "RPGReboundsRebounds per game.": "RPG",
        "TRB%Total Rebound PercentageTotal rebound percentage is estimated percentage of available rebounds grabbed by the player while the player is on the court.": "TRB%",
        "APGAssistsAssists per game.": "APG",
        "AST%Assist PercentageAssist percentage is an estimated percentage of teammate field goals a player assisted while the player is on the court": "AST%",
        "SPGStealsSteals per game.": "SPG",
        "BPGBlocksBlocks per game.": "BPG",
        "TOPGTurnoversTurnovers per game.": "TOPG",
        "VIVersatility IndexVersatility index is a metric that measures a player’s ability to produce in points, assists, and rebounds. The average player will score around a five on the index, while top players score above 10": "VI",
        "ORTGOffensive RatingIndividual offensive rating is the number of points produced by a player per 100 total individual possessions.": "ORTG",
        "DRTGDefensive RatingIndividual defensive rating estimates how many points the player allowed per 100 possessions he individually faced while staying on the court.": "DRTG"
    })

    return d


def get_full_dataframe():
    """Join all the data into one dataframe"""
    data = [get_data(i) for i in range(2017, 2022)]  # all data from 2017-2018 to 2021-2022 seasons

    # add all data from 2017-2018 to 2021-2022 seasons into one dataframe
    # print([d.shape for d in data])
    df = pd.concat(data, ignore_index=True)
    df = df[df.isnull().sum(axis=1) < 2]  # get rid of rows w/o sufficient data
    return df


def main():
    stats_data = get_full_dataframe()
    # print(stats_df)

    # print(stats_df.isnull().sum(), '\n')
    # print(stats_df.isnull().sum(axis=1).sort_values(ascending=False))


if __name__ == "__main__":
    main()
