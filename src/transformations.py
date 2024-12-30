def filter_by_predicate(df, column, condition):
    """
    Filters rows in a DataFrame based on a condition.
    :param df: The original DataFrame
    :param column: The column to filter
    :param condition: The condition as a string, e.g., '> 30'
    :return: Filtered DataFrame
    """
    try:
        return df.query(f"{column} {condition}")
    except Exception as e:
        print(f"Error in filtering: {e}")
        return df


def select_columns(df, columns):
    """
    Selects specific columns from a DataFrame.
    :param df: The original DataFrame
    :param columns: List of columns to select
    :return: DataFrame with selected columns
    """
    try:
        return df[columns]
    except KeyError as e:
        print(f"Error: columns {e} do not exist.")
        return df


def sort_by_column(df, column, ascending=True):
    """
    Sorts the DataFrame by a specific column.
    :param df: The original DataFrame
    :param column: The column to sort by
    :param ascending: Whether to sort in ascending order
    :return: Sorted DataFrame
    """
    try:
        return df.sort_values(by=column, ascending=ascending)
    except KeyError as e:
        print(f"Error: column {e} does not exist.")
        return df


def add_column(df, new_column, expression):
    """
    Adds a new column to the DataFrame based on an expression.
    :param df: The original DataFrame
    :param new_column: The name of the new column
    :param expression: The expression to calculate the new column
    :return: DataFrame with the new column
    """
    try:
        df[new_column] = df.eval(expression)
        return df
    except Exception as e:
        print(f"Error adding column: {e}")
        return df


def aggregate(df, group_by_column, agg_column, agg_func):
    """
    Aggregates the DataFrame by a column and applies an aggregation function.
    :param df: The original DataFrame
    :param group_by_column: The column to group by
    :param agg_column: The column to aggregate
    :param agg_func: The aggregation function (e.g., 'sum', 'mean')
    :return: Aggregated DataFrame
    """
    try:
        return df.groupby(group_by_column).agg({agg_column: agg_func}).reset_index()
    except Exception as e:
        print(f"Error in aggregation: {e}")
        return df
