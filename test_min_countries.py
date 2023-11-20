import pandas as pd
import pytest
from min_countries import identify_min_values_and_countries

# DataFrame for testing
data = {
    'year': [2000, 2001, 2002],
    'country': ['Country1', 'Country2', 'Country3'],
    'goal_1_score': [10, 15, 12],
    'goal_2_score': [5, 8, 6],
    'goal_3_score': [20, 18, 22]
}

df = pd.DataFrame(data)

def test_identify_min_values_and_countries(capsys):
    # Call the function with the test DataFrame
    result_df = identify_min_values_and_countries(df)

    # Check the values and names of countries in the DataFrame
    assert result_df.loc[result_df['Goal'] == 'goal_2_score', 'Min_Value'].values[0] == 5
    assert 'Country1' in result_df.loc[result_df['Goal'] == 'goal_2_score', 'Countries_with_Min_Value'].values[0]

    assert result_df.loc[result_df['Goal'] == 'goal_3_score', 'Min_Value'].values[0] == 18
    assert 'Country2' in result_df.loc[result_df['Goal'] == 'goal_3_score', 'Countries_with_Min_Value'].values[0]

if __name__ == "__main__":
    pytest.main([__file__])