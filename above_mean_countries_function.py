import pandas as pd
def calculate_countries_above_mean_count(df, output_csv_filename=None):
    """
    Calculate the number of countries with scores above the mean for each goal in the input DataFrame.

    Parameters:
    - df (pd.DataFrame): Input DataFrame containing the SDG data.
    - output_csv_filename (str): Optional filename to save the results to a CSV file.

    Returns:
    - pd.DataFrame: DataFrame containing the number of countries above the mean for each goal.
    """
    # Select only the columns containing goal scores
    goal_columns = df.columns[3:]

    # List to store the number of countries above the mean for each goal
    countries_above_mean_count = []

    # Iterate through each goal score column
    for goal in goal_columns:
        mean_value = df[goal].mean()  # Mean value for the current goal
        num_countries_above_mean = df[df[goal] > mean_value]['country'].nunique()  # Number of countries above the mean
        countries_above_mean_count.append({'Goal': goal, 'Num_Countries_Above_Mean': num_countries_above_mean})

    # Create a DataFrame from the list of dictionaries
    above_mean_count_df = pd.DataFrame(countries_above_mean_count)

    # Save the DataFrame to a CSV file if filename is provided
    if output_csv_filename:
        above_mean_count_df.to_csv(output_csv_filename, index=False)

    # Return the DataFrame
    return above_mean_count_df
