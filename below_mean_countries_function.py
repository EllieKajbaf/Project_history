import pandas as pd

def calculate_countries_below_mean_count(df):
    """
    Calculate the number of countries with scores below the mean for each goal in the input DataFrame.

    Parameters:
    - df (pd.DataFrame): Input DataFrame containing the SDG data.

    Returns:
    - pd.DataFrame: DataFrame containing the number of countries below the mean for each goal.
    """
    # Select only the columns containing goal scores
    goal_columns = df.columns[3:]

    # Find the mean value for each goal score
    mean_values = df[goal_columns].mean()

    # List to store the number of countries below the mean for each goal
    countries_below_mean_count = []

    # Iterate through each goal score column
    for goal in goal_columns:
        # Mean value for the current goal
        mean_value = df[goal].mean() 
        # Number of countries below the mean
        num_countries_below_mean = df[df[goal] < mean_value]['country'].nunique() 
        countries_below_mean_count.append({'Goal': goal, 'Num_Countries_Below_Mean': num_countries_below_mean})

    # Create a DataFrame from the list of dictionaries
    below_mean_count_df = pd.DataFrame(countries_below_mean_count)

    # Return the DataFrame
    return below_mean_count_df
