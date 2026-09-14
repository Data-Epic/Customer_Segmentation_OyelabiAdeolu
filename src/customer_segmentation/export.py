from datetime import datetime
from pathlib import Path
import pandas as pd


def export_and_display_results(
    df: pd.DataFrame, output_dir: str = "."
) -> pd.DataFrame:
  """Saves the processed DataFrame using standardized snake_case columns

  and a reversed date filename, then displays 10 shuffled rows.
  """
  today_reversed = datetime.now().strftime("%d-%m-%Y")
  filename = f"processed_data_{today_reversed}.csv"
  output_path = Path(output_dir) / filename

  required_cols = ["customer_id", "country", "total_purchases", "loyalty_score"]

  export_df = df[required_cols].copy()

  export_df.to_csv(output_path, index=False, encoding="utf-8")
  print(f"File successfully saved to: {output_path.resolve()}")

  shuffled_display = export_df.sample(frac=1, random_state=42).head(10)
  print("\nFirst 10 Shuffled Rows of Processed Data:")
  print(shuffled_display)

  return export_df
