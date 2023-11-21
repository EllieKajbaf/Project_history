import pandas as pd
import pytest
from above_mean_countries_function import calculate_countries_above_mean_count

# Mock DataFrame for testing
data = {
    'year': [2000, 2001, 2002, 2003, 2004, 2005],
    'country': ['A', 'B', 'C', 'D', 'E', 'F'],
    'gsd_index_score': [10, 15, 12, 18, 38, 39],
    'goal_1_score': [10, 15, 12, 18, 38, 39],
    'goal_2_score': [5, 8, 6, 9, 40, 41],
    'goal_3_score': [20, 18, 22, 30, 89, 90]
}

df = pd.DataFrame(data)

def test_calculate_countries_above_mean_count():
    # Call the function with the mock DataFrame
    result_df = calculate_countries_above_mean_count(df)

    # Check the values in the DataFrame
    assert result_df.loc[result_df['Goal'] == 'goal_1_score', 'Num_Countries_Above_Mean'].values[0] == 2
    assert result_df.loc[result_df['Goal'] == 'goal_2_score', 'Num_Countries_Above_Mean'].values[0] == 2
    assert result_df.loc[result_df['Goal'] == 'goal_3_score', 'Num_Countries_Above_Mean'].values[0] == 2
    