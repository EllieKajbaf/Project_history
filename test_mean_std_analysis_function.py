import pandas as pd
import pytest

# Import
from mean_std_analysis_function import calculate_mean_std  

# Example DataFrame for testing
data = {
    'country_code': ['AFG'] * 12,
    'country': ['Afghanistan'] * 12,
    'year': [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011],
    'sdg_index_score': [36, 36.3, 36.3, 36.7, 37.1, 37.5, 37.6, 38, 37.3, 38.3, 38.8, 38.4],
    'goal_1_score': [28.8] * 12,
    'goal_2_score': [27.3, 30.6, 30.7, 32.5, 32.1, 35.9, 36.5, 39.5, 37.8, 43, 43.2, 42],
    'goal_3_score': [19.2, 19.4, 19.7, 19.9, 21.1, 22.6, 22.7, 24.4, 25.9, 28.1, 31.4, 30.6]
}


df = pd.DataFrame(data)

def test_calculate_mean_std():
    result_df = calculate_mean_std(df)

    # Check if the result DataFrame has the expected columns
    assert all(col in result_df.columns for col in ['Goal', 'Mean', 'Std'])

    # Check if the number of rows in the result DataFrame is equal to the number of goal columns
    assert len(result_df) == len(df.columns) - 3  # Assuming the goal columns start from index 3

    # Check if the means and std deviations are calculated correctly for the provided data
    expected_means = df.iloc[:, 3:].mean().values
    expected_stds = df.iloc[:, 3:].std().values

    assert all(result_df['Mean'].values == expected_means)
    assert all(result_df['Std'].values == expected_stds)

if __name__ == "__main__":
    pytest.main([__file__])
