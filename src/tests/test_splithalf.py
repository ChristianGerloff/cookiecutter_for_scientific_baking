import pytest
import sys
import numpy as np
import pandas as pd
import seaborn as sns
sys.path.append('../model')
import splithalf as sp


@pytest.mark.parametrize('split', [0.1, 0.5, 0.9, 1])
def test_len_splithalf(split):
    observations = pd.DataFrame(np.random.randint(low=6,high=50, size=(100, 2)), columns=['A','B'])
    s1_subsample, s2_subsample = sp.simple_split_half(observations, split=split)
    assert len(s1_subsample)+len(s2_subsample) == len(observations)