from datetime import datetime
import pandas as pd
import pytest


@pytest.fixture
def sample_raw_df():
  """Provides a raw DataFrame with Title Case columns matching the input structure."""
  data = {
      "Customer ID": [1, 2, 3, 4],
      "Country": ["Canada", "Mexico", "Canada", "USA"],
      "Total Purchases": [25, 3, 4, 15],
      "Sign-up Date": ["2019-05-10", "2020-01-15", "2021-08-20", "2022-03-11"],
  }
  return pd.DataFrame(data)


@pytest.fixture
def sample_processed_df():
  """Provides a processed DataFrame featuring snake_case columns and loyalty_score."""
  data = {
      "customer_id": [1, 3, 4],
      "country": ["Canada", "Canada", "USA"],
      "total_purchases": [25, 4, 15],
      "sign_up_date": pd.to_datetime(
          ["2019-05-10", "2021-08-20", "2022-03-11"]
      ),
      "loyalty_score": [3, 1, 2],
  }
  return pd.DataFrame(data)