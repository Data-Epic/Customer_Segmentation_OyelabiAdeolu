from datetime import datetime
from customer_segmentation.features import compute_loyalty_score
import pandas as pd
import pytest


def test_compute_loyalty_score_branches():
  current_year = datetime.now().year
  
  data = {
      "total_purchases": [25, 15, 5, 5],
      "sign_up_date": pd.to_datetime([
          f"{current_year - 1}-01-01",  # Score 3: purchases > 20
          f"{current_year - 1}-01-01",  # Score 2: purchases between 10 and 20
          f"{current_year - 5}-01-01",  # Score 2: purchases < 10 but tenure > 3 years
          f"{current_year - 1}-01-01",  # Score 1: purchases < 10 and tenure <= 3 years
      ]),
  }
  df = pd.DataFrame(data)

  result = compute_loyalty_score(df)

  assert "loyalty_score" in result.columns
  assert result.loc[0, "loyalty_score"] == 3
  assert result.loc[1, "loyalty_score"] == 2
  assert result.loc[2, "loyalty_score"] == 2
  assert result.loc[3, "loyalty_score"] == 1
  