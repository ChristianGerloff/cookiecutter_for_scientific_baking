import numpy as np
import pandas as pd


def simple_split_half(data: pd.DataFrame, split: float = 0.5, seed: int = 19700421) -> pd.DataFrame:
    """Segment the data frame into two sub sets."""

    n_sample = np.round((1-split) * len(data)).astype(int)

    np.random.seed(seed)
    h1_idx = np.random.choice(data.index.values,
                              size=n_sample, replace=False)

    h1_subsample = data.drop(index=h1_idx)
    h2_subsample = data.loc[h1_idx, :]

    # Postprocessing
    h1_subsample['subsample'] = 's1'
    h2_subsample['subsample'] = 's2'
    return h1_subsample, h2_subsample
