
import pandas as pd

def df_preprocess(df, year):
    """Renames dataframes for each year to make columns consistent"""
    df = df.rename(columns={
        "FULL NAME": "NAME",
        "USG%Usage RateUsage rate, a.k.a., usage percentage is an estimate of the percentage of team plays used by a player while he was on the floor": "USG%",
        "TO%Turnover RateA metric that estimates the number of turnovers a player commits per 100 possessions": "TO%",
        "eFG%Effective Shooting PercentageWith eFG%, three-point shots made are worth 50% more than two-point shots made. eFG% Formula=(FGM+ (0.5 x 3PM))/FGA": "eFG%",
        "TS%True Shooting PercentageTrue shooting percentage is a measure of shooting efficiency that takes into account field goals, 3-point field goals, and free throws.": "TS%",
        "PPGPointsPoints per game.": "PPG",
        "RPGReboundsRebounds per game.": "RPG",
        "TRB%Total Rebound PercentageTotal rebound percentage is estimated percentage of available rebounds grabbed by the player while the player is on the court.": "TRB%",
        "APGAssistsAssists per game.": "APG",
        "AST%Assist PercentageAssist percentage is an estimated percentage of teammate field goals a player assisted while the player is on the court": "AST%",
        "SPGStealsSteals per game.": "SPG",
        "BPGBlocksBlocks per game.": "BPG",
        "TOPGTurnoversTurnovers per game.": "TPG",
        "VIVersatility IndexVersatility index is a metric that measures a player’s ability to produce in points, assists, and rebounds. The average player will score around a five on the index, while top players score above 10": "VI",
        "ORTGOffensive RatingIndividual offensive rating is the number of points produced by a player per 100 total individual possessions.": "ORTG",
        "DRTGDefensive RatingIndividual defensive rating estimates how many points the player allowed per 100 possessions he individually faced while staying on the court.": "DRTG",
        "ORtg": "ORTG",
        "DRtg": "DRTG"
    })

    feats = ['RANK', 'NAME', 'TEAM', 'POS', 'AGE', 'GP', 'MPG', 'USG%',
        'FTA', 'FT%', '2PA', '2P%', '3PA', '3P%', 'eFG%', 'TS%', 
        'PPG', 'RPG', 'APG', 'SPG', 'BPG','TPG', 'VI', 'ORTG', 'DRTG']

    df = df[feats]
    df = df[df.isnull().sum(axis=1) == 0]
    df['Year'] = year  # initial year
    return df


def read_data_from_files():
    """Read in regular season data from 2020-2023 seasons from excel/csv files"""
    d19 = pd.read_excel("data/nba_stats_1819.xlsx", skiprows=1)
    d19 = df_preprocess(d19, 2019)
    d20 = pd.read_excel("data/nba_stats_1920.xlsx", skiprows=1)
    d20 = df_preprocess(d20, 2020)
    d21 = pd.read_excel("data/nba_stats_2021.xlsx", skiprows=1)
    d21 = df_preprocess(d21, 2021)
    d22 = pd.read_excel("data/nba_stats_2122.xlsx", skiprows=1)
    d22 = df_preprocess(d22, 2022)
    d23 = pd.read_csv("data/nba_stats_2223.csv")
    d23 = df_preprocess(d23, 2023)
    return pd.concat([d19, d20, d21, d22, d23], ignore_index=True)


def clean_data():
    """Return a clean, preprocessed nba dataframe"""
    stats_df = read_data_from_files() #nbastuffer_dataframe(playoffs=False)
    stats_df = stats_df[stats_df['POS'] != 0].copy()  # Nicolo Melli (F) - 2019
    stats_df = stats_df[stats_df["MPG"] >= 10 ].copy()  # players that played at least 10 minutes
    stats_df = stats_df.drop(["RANK", "NAME", "TEAM", "Year"], axis=1)
    stats_df = stats_df[stats_df["POS"].isin(["F", "G", "C"])]
    return stats_df


def main():
    pass


if __name__ == "__main__":
    main()
