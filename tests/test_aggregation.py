from customer_segmentation.aggregation import aggregate_data
import pandas as pd
import pytest


def test_aggregate_data_excludes_mexico_and_computes_stats(sample_processed_df):
  # Append a Mexico row to ensure it gets filtered out correctly
  mexico_row = pd.DataFrame({
      "customer_id": [99],
      "country": ["Mexico"],
      "total_purchases": [50],
      "sign_up_date": pd.to_datetime(["2020-01-01"]),
      "loyalty_score": [3],
  })
  test_df = pd.concat([sample_processed_df, mexico_row], ignore_index=True)

  result = aggregate_data(test_df)

  # Verify Mexico is completely excluded from the result
  assert "Mexico" not in result["country"].values

  # Verify expected columns are present
  expected_columns = [
      "country",
      "avg_total_purchases",
      "max_total_purchases",
      "common_loyalty_score",
  ]
  for col in expected_columns:
    assert col in result.columns

  # Verify calculated metrics for Canada (Total purchases: 25 and 4)
  canada_row = result[result["country"] == "Canada"].iloc[0]
  assert canada_row["avg_total_purchases"] == 14.5
  assert canada_row["max_total_purchases"] == 25

  # Verify calculated metrics for USA (Total purchases: 15)
  usa_row = result[result["country"] == "USA"].iloc[0]
  assert usa_row["avg_total_purchases"] == 15.0
  assert usa_row["max_total_purchases"] == 15