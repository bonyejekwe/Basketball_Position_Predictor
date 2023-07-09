
import pandas as pd


def get_data(start=3):
    """Return dataframe"""
    df_list = []
    for i in range(start, 24):
        year = str(i).zfill(2)  # zero padding if necessary
        d = pd.read_csv(f"data/br{year}.txt")
        d["Year"] = 2000 + i
        df_list.append(d)

    full_df = pd.concat(df_list, ignore_index=True)
    full_df = full_df[full_df.isnull().sum(axis=1) == 0]  # non-null rows
    full_df = full_df[full_df["Pos"].isin(["PG", "SG", "SF", "PF", "C"])]
    return full_df


def filter_data(df, five_pos=True, games_played=0, games_started=0, minutes_played=0):
    """Filter dataframe"""
    df = df[df["G"] >= games_played]
    df = df[df["GS"] >= games_started]
    df = df[df["MP"] >= minutes_played]
    df = df.reset_index().drop(["index", "Rk", "Player", "Tm", "Player-additional", "Year"], axis=1)
    if not five_pos:
        df = df.replace({"PF": "F", "SF": "F", "PG": "G", "SG": "G"})
    return df
