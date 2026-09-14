from pathlib import Path
import pandas as pd


def load_data(file_path="data/MOCK_DATA.csv") -> pd.DataFrame:
    """Counts total rows using pathlib and loads only the first 75% into a DataFrame."""
    path = Path(file_path)

    # Stream lines using pathlib's open method to count rows without full memory load
    with path.open("r", encoding="utf-8") as f:
        total_rows = sum(1 for _ in f) - 1  # Exclude header row

    limit = int(total_rows * 0.75)
    return pd.read_csv(path, nrows=limit)
