from customer_segmentation.cleaning import (
    clean_sign_up_date,
    filter_canada_purchases,
    remove_consecutive_duplicates,
    rename_columns,
)
import pandas as pd
import pytest


def test_rename_columns():
  df = pd.DataFrame({
      "Customer ID": [1],
      "Country": ["Canada"],
      "Total Purchases": [10],
      "Sign-up Date": ["2021-01-01"],
  })
  result = rename_columns(df)
  expected_cols = ["customer_id", "country", "total_purchases", "sign_up_date"]
  assert list(result.columns) == expected_cols


def test_remove_consecutive_duplicates():
  df = pd.DataFrame({
      "customer_id": [1, 1, 2, 1],
      "country": ["Canada", "Canada", "USA", "Canada"],
  })
  result = remove_consecutive_duplicates(df)
  # Row index 1 is a consecutive duplicate of index 0 -> dropped
  # Row index 3 matches index 0 value-wise, but is non-consecutive -> kept
  assert len(result) == 3
  assert list(result["customer_id"]) == [1, 2, 1]


def test_clean_sign_up_date():
  df = pd.DataFrame({
      "sign_up_date": ["2019-05-10", "2020-01-15", "2021-08-20"]
  })
  result = clean_sign_up_date(df)
  assert pd.api.types.is_datetime64_any_dtype(result["sign_up_date"])
  assert pd.isna(result.loc[1, "sign_up_date"])  # 2020 entry becomes NaT
  assert result.loc[0, "sign_up_date"].year == 2019
  assert result.loc[2, "sign_up_date"].year == 2021


def test_filter_canada_purchases():
  df = pd.DataFrame({
      "customer_id": [1, 2, 3, 4],
      "country": ["Canada", "Canada", "USA", "Canada"],
      "total_purchases": [
          3,
          10,
          2,
          4,
      ],  # Index 0: Canada & <5 (dropped), Index 1: Canada & >=5 (kept), Index 2: USA & <5 (kept), Index 3: Canada & <5 (dropped)
  })
  result = filter_canada_purchases(df)
  assert len(result) == 2
  assert set(result["customer_id"]) == {2, 3}