import pandas as pd

def identify_max_values_and_countries(df, output_csv_filename=None):
    """
    Find, print, and visualize the maximum values for each SDG goal, 
    including associated countries, and save the results to a CSV file.

    Parameters:
    - df (pd.DataFrame): Input DataFrame containing the SDG data.
    - output_csv_filename (str): Optional filename to save the results to a CSV file.

    Returns:
    - pd.DataFrame: DataFrame containing the maximum values and associated countries.
    """
    # Select only the columns containing goal scores
    goal_columns = df.columns[3:]

    # Find the maximum value for each goal score
    max_values = df[goal_columns].max()

    # List to store dictionaries with goal, max value, and countries
    max_data = []

    # Iterate through each goal score column
    for goal in goal_columns:
        # Maximum value for the current goal
        max_value = df[goal].max()
        # Concatenate unique country names into a string
        countries_with_max_value = ', '.join(df.loc[df[goal] == max_value, 'country'].unique())
        max_data.append({'Goal': goal, 'Max_Value': max_value, 'Countries_with_Max_Value': countries_with_max_value})

    # Create a DataFrame from the list of dictionaries
    max_df = pd.DataFrame(max_data)

    # Print the results row by row
    for index, row in max_df.iterrows():
        print(f"Goal: {row['Goal']}\nMax Value: {row['Max_Value']}\nCountries with Max Value: "
              f"{row['Countries_with_Max_Value']}\n{'='*50}\n")

    # Save the DataFrame to a CSV file if filename is provided
    if output_csv_filename:
        max_df.to_csv(output_csv_filename, index=False)

    # Return the DataFrame
    return max_df
