import pandas as pd

def calculate_countries_above_quantile_count(df, quantile_threshold=0.9):
    """
    Calculate the number of countries above the quantile for each goal in the input DataFrame.

    Parameters:
    - df (pd.DataFrame): Input DataFrame containing the SDG data.
    - quantile_threshold (float): The quantile threshold.

    Returns:
    - pd.DataFrame: DataFrame containing the number of countries above the quantile for each goal.
    """
    # Select only the columns containing goal scores
    goal_columns = df.columns[3:]

    # List to store the number of countries above the quantile for each goal
    countries_above_quantile_count = []

    # Iterate through each goal score column
    for goal in goal_columns:
        # Quantile value for the current goal
        quantile_value = df[goal].quantile(quantile_threshold)
        # Number of countries above the quantile
        num_countries_above_quantile = df[df[goal] > quantile_value]['country'].nunique()
        countries_above_quantile_count.append({'Goal': goal, 'Num_Countries_Above_Quantile': num_countries_above_quantile})

    # Create a DataFrame from the list of dictionaries
    above_quantile_count_df = pd.DataFrame(countries_above_quantile_count)

    return above_quantile_count_df
