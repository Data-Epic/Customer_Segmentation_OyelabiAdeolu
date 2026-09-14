import pandas as pd

def rename_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Standardizes column names to lowercase snake_case."""
    return df.rename(
        columns={
            'Customer ID': 'customer_id',
            'Country': 'country',
            'Total Purchases': 'total_purchases',
            'Sign-up Date': 'sign_up_date',
        }
    )


def remove_consecutive_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Removes rows only if they are consecutive duplicates."""
    return df[df.ne(df.shift()).any(axis=1)].copy()


def clean_sign_up_date(df: pd.DataFrame) -> pd.DataFrame:
    """Converts sign-up dates and replaces 2020 entries with NaT."""
    df = df.copy()
    df['sign_up_date'] = pd.to_datetime(df['sign_up_date'])
    df['sign_up_date'] = df['sign_up_date'].mask(df['sign_up_date'].dt.year == 2020)
    return df


def filter_canada_purchases(df: pd.DataFrame) -> pd.DataFrame:
    """Drops rows where total purchases < 5 and country is Canada."""
    df = df.copy()
    condition = (df['total_purchases'] < 5) & (df['country'] == 'Canada')
    return df[~condition]


