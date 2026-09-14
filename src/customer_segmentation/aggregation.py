import pandas as pd


def aggregate_data(df: pd.DataFrame) -> pd.DataFrame:
    """Groups data by country, excluding Mexico, and computes statistics."""
    filtered_df = df[df["country"] != "Mexico"]
    return (
        filtered_df.groupby("country")
        .agg(
            avg_total_purchases=("total_purchases", "mean"),
            max_total_purchases=("total_purchases", "max"),
            common_loyalty_score=(
                "loyalty_score",
                lambda x: x.mode()[0] if not x.empty else None,
            ),
        )
        .reset_index()
    )