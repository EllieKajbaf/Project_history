def calculate_mean_std(df):
    import pandas as pd

    # Select only the columns containing goal scores
    goal_columns = df.columns[3:]

    # Calculate the mean and standard deviation for each goal score
    mean_values = df[goal_columns].mean()
    std_values = df[goal_columns].std()

    # A new DataFrame to store the results
    result_df = pd.DataFrame({'Goal': mean_values.index, 'Mean': mean_values.values, 'Std': std_values.values})

    # Return the result_df
    return result_df
