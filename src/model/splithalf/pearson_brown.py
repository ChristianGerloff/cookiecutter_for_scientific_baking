import pandas as pd

from scipy.stats import pearsonr


def pearson(h1_data:pd.DataFrame, h2_data: pd.DataFrame, cols: list) -> list:
    """Returns the bivariate bravais pearson correlation coefficient

    Parameters
    ----------
    h1_data : pd.DataFrame
        The data frame containing the relevant vector for the corr.
    h2_data : pd.DataFrame
       The data frame containing the second vector for the corr.
    cols : list
       A list of strings representing the relevant column names.

    Returns
    -------
    list
        A list of floats representing the corr. coefficients for each
        column.
    """
    result = list()
    for c, item in enumerate(cols):
        result.append(pearsonr(h1_data[item], h2_data[item])[0])
    return result


def spearman_brown (h1_data: pd.DataFrame, h2_data: pd.DataFrame, col: str) -> float:
    """Returns Spearman-Brown coefficient"""
    cor, _ = pearsonr(h1_data[col], h2_data[col])
    result = 2.0 * cor / (1.0 + cor)
    return result
