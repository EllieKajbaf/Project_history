import pandas as pd

def calculate_countries_below_quantile_count(df, quantile_threshold=0.1):
    """
    Calculate the number of countries below the quantile for each goal in the input DataFrame.

    Parameters:
    - df (pd.DataFrame): Input DataFrame containing the SDG data.
    - quantile_threshold (float): The quantile threshold.

    Returns:
    - pd.DataFrame: DataFrame containing the number of countries below the quantile for each goal.
    """
    # Select only the columns containing goal scores
    goal_columns = df.columns[3:]

    # List to store the number of countries below the quantile for each goal
    countries_below_quantile_count = []

    # Iterate through each goal score column
    for goal in goal_columns:
        # Calculate the quantile value for the current goal
        quantile_value = df[goal].quantile(quantile_threshold)
        
        # Count the number of countries below the quantile for the current goal
        num_countries_below_quantile = df[df[goal] < quantile_value]['country'].nunique()
        
        # Append the results to the list
        countries_below_quantile_count.append({'Goal': goal, 'Num_Countries_Below_Quantile': num_countries_below_quantile})

    # Create a DataFrame from the list of dictionaries
    below_quantile_count_df = pd.DataFrame(countries_below_quantile_count)

    return below_quantile_count_df
