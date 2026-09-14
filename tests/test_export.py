from datetime import datetime
from pathlib import Path
from customer_segmentation.export import export_and_display_results
import pandas as pd
import pytest


def test_export_and_display_results(tmp_path):
  # Create a sample DataFrame containing extra columns to verify filtering
  data = {
      "customer_id": [1, 2, 3, 4, 5],
      "country": ["Canada", "USA", "UK", "Canada", "Germany"],
      "total_purchases": [10, 20, 15, 5, 30],
      "loyalty_score": [1, 2, 3, 1, 3],
      "extra_column": ["drop_me", "drop_me", "drop_me", "drop_me", "drop_me"],
  }
  df = pd.DataFrame(data)

  # Execute export function utilizing the temporary directory fixture
  result_df = export_and_display_results(df, output_dir=str(tmp_path))

  # Verify returned DataFrame keeps only required columns
  required_cols = ["customer_id", "country", "total_purchases", "loyalty_score"]
  assert list(result_df.columns) == required_cols

  # Verify the CSV file was successfully created using the date format pattern
  today_reversed = datetime.now().strftime("%d-%m-%Y")
  expected_filename = f"processed_data_{today_reversed}.csv"
  expected_file_path = tmp_path / expected_filename

  assert expected_file_path.exists()

  # Read back the saved CSV to ensure structural integrity
  saved_df = pd.read_csv(expected_file_path)
  assert list(saved_df.columns) == required_cols
  assert len(saved_df) == 5