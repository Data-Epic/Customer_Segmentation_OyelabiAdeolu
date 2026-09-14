from datetime import datetime
import pandas as pd


def compute_loyalty_score(df: pd.DataFrame) -> pd.DataFrame:
    """Calculates loyalty score and returns the dataframe for chaining."""
    df = df.copy()
    current_date = pd.Timestamp(datetime.now())

    def assign_score(row):
        tp = row["total_purchases"]
        su_date = row["sign_up_date"]
        if pd.notnull(su_date):
            tenure_years = (current_date - su_date).days / 365.25
        else:
            tenure_years = 0

        if tp > 20:
            return 3
        elif 10 <= tp <= 20:
            return 2
        else:
            return 2 if tenure_years > 3 else 1

    df["loyalty_score"] = df.apply(assign_score, axis=1)
    return df
