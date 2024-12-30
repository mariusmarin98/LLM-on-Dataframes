import pandas as pd
from src.transformations import filter_by_predicate, select_columns, sort_by_column, add_column, aggregate

def apply_transformations(df, transformations):
    """
    Applies a sequence of transformations to a DataFrame.
    :param df: The original DataFrame
    :param transformations: List of transformations
    :return: The transformed DataFrame
    """
    for t in transformations:
        print(f"Applying transformation: {t}")
        try:
            if t['action'] == 'filter_by_predicate':
                df = filter_by_predicate(df, t['column'], t['condition'])
            elif t['action'] == 'select_columns':
                df = select_columns(df, t['columns'])
            elif t['action'] == 'sort_by_column':
                df = sort_by_column(df, t['column'], t.get('ascending', True))
            elif t['action'] == 'add_column':
                df = add_column(df, t['new_column'], t['expression'])
            elif t['action'] == 'aggregate':
                df = aggregate(df, t['group_by_column'], t['agg_column'], t['agg_func'])
            print("Intermediate DataFrame:")
            print(df)
        except Exception as e:
            print(f"Error applying transformation: {e}")
    return df


if __name__ == "__main__":
    df = pd.read_csv("../data/sample_data.csv")

    print("Initial data:")
    print(df)

    transformations = [
        {"action": "filter_by_predicate", "column": "salary", "condition": "> 75000"},
        {"action": "select_columns", "columns": ["name", "salary", "bonus"]},
        {"action": "add_column", "new_column": "bonus", "expression": "salary * 0.1"},
        {"action": "aggregate", "group_by_column": "department", "agg_column": "salary", "agg_func": "sum"}
    ]

    transformed_df = apply_transformations(df, transformations)
    print("\nTransformed data:")
    print(transformed_df)
