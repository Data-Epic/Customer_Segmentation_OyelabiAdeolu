from customer_segmentation.load import load_data
import pandas as pd
import pytest


def test_load_data_returns_seventy_five_percent(tmp_path):
  # Create a temporary CSV file with 10 data rows + 1 header row
  csv_content = "customer_id,country,total_purchases,sign_up_date\n"
  for i in range(1, 11):
    csv_content += f"{i},Canada,{i * 2},2021-01-01\n"

  file_path = tmp_path / "test_mock.csv"
  file_path.write_text(csv_content, encoding="utf-8")

  # Call load_data pointing to the temp file
  result_df = load_data(file_path)

  # 10 total data rows * 0.75 = 7.5 -> int(7.5) = 7 rows expected
  assert len(result_df) == 7
  assert "customer_id" in result_df.columns