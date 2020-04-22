import pandas as pd

from scipy.stats import pearsonr

def pearson_brown(h1_data: pd.DataFrame, h2_data: pd.DataFrame, col:str) -> pd.DataFrame:
    cor, _ = pearsonr(h1_data[col], h2_data[col])
    result = 2.0 * cor / (1.0 + cor)
    return result