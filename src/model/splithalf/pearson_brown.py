import pandas as pd

from scipy.stats import pearsonr

def pearson(h1_data: pd.DataFrame, h2_data: pd.DataFrame, cols:list) -> list:
    query = list()
    for c, item in enumerate(cols):
        query.append(pearsonr(h1_data[item], h2_data[item])[0])
    return query

def pearson_brown(h1_data: pd.DataFrame, h2_data: pd.DataFrame, col:str) -> float:
    cor, _ = pearsonr(h1_data[col], h2_data[col])
    result = 2.0 * cor / (1.0 + cor)
    return result