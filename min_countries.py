import pandas as pd

def identify_min_values_and_countries(df, output_csv_filename='min_values_countries.csv'):
    """
    Identify the minimum values for each goal score in the DataFrame,
    along with the countries that achieved these minimum values.
    Print the results and save them to a CSV file.

    Parameters:
    - df (pd.DataFrame): Input DataFrame.
    - output_csv_filename (str): Output CSV filename to save the results. Default is 'min_values_countries.csv'.
    """
    # Select only the columns containing goal scores
    goal_columns = df.columns[3:]

    # Find the minimum value for each goal score
    min_values = df[goal_columns].min()

    # List to store dictionaries with goal, min value, and countries
    min_data = []

    # Iterate through each goal score column
    for goal in goal_columns:
        min_value = df[goal].min()  # Minimum value for the current goal
        # Concatenate unique country names into a string
        countries_with_min_value = ', '.join(df.loc[df[goal] == min_value, 'country'].unique())  
        min_data.append({'Goal': goal, 'Min_Value': min_value, 'Countries_with_Min_Value': countries_with_min_value})

    # DataFrame from the list of dictionaries
    min_df = pd.DataFrame(min_data)

    # Print the results row by row
    for index, row in min_df.iterrows():
        print(f"Goal: {row['Goal']}\nMin Value: {row['Min_Value']}\nCountries with Min Value: {row['Countries_with_Min_Value']}\n{'='*50}\n")

    # Save the DataFrame to a CSV file
    min_df.to_csv(output_csv_filename, index=False)

    # Return the DataFrame with the minimum values and countries
    return min_df
