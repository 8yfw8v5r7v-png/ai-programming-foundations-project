"""
Unit tests for preprocessing module.
"""

import pandas as pd
import pytest
from src.preprocessing.preprocessing import handle_missing_values, normalize_features


def test_handle_missing_values_drop():
    """Test handle_missing_values with drop strategy."""
    df = pd.DataFrame({'A': [1, 2, None], 'B': [4, None, 6]})
    result = handle_missing_values(df, strategy='drop')
    assert len(result) == 1
    assert result.isna().sum().sum() == 0


def test_handle_missing_values_mean():
    """Test handle_missing_values with mean strategy."""
    df = pd.DataFrame({'A': [1.0, 2.0, None], 'B': [4.0, 5.0, 6.0]})
    result = handle_missing_values(df, strategy='mean')
    assert result.isna().sum().sum() == 0


def test_normalize_features():
    """Test normalize_features function."""
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50]})
    result = normalize_features(df, ['A', 'B'])
    assert result['A'].min() == 0.0
    assert result['A'].max() == 1.0
    assert result['B'].min() == 0.0
    assert result['B'].max() == 1.0
