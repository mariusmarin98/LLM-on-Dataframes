import pandas as pd
from src.transformations import (
    filter_by_predicate, select_columns, sort_by_column,
    add_column, aggregate
)

def test_filter_by_predicate():
    data = {'name': ['Alice', 'Bob'], 'age': [25, 35]}
    df = pd.DataFrame(data)
    filtered_df = filter_by_predicate(df, 'age', '> 30')
    assert len(filtered_df) == 1
    assert filtered_df.iloc[0]['name'] == 'Bob'

def test_select_columns():
    data = {'name': ['Alice', 'Bob'], 'age': [25, 35]}
    df = pd.DataFrame(data)
    selected_df = select_columns(df, ['name'])
    assert list(selected_df.columns) == ['name']

def test_sort_by_column():
    data = {'name': ['Alice', 'Bob'], 'salary': [50000, 60000]}
    df = pd.DataFrame(data)
    sorted_df = sort_by_column(df, 'salary', ascending=False)
    assert sorted_df.iloc[0]['name'] == 'Bob'

def test_add_column():
    data = {'salary': [50000, 60000]}
    df = pd.DataFrame(data)
    updated_df = add_column(df, 'bonus', 'salary * 0.1')
    assert 'bonus' in updated_df.columns
    assert updated_df['bonus'].iloc[0] == 5000.0

def test_aggregate():
    data = {'department': ['HR', 'Engineering', 'Engineering'], 'salary': [50000, 60000, 70000]}
    df = pd.DataFrame(data)
    aggregated_df = aggregate(df, 'department', 'salary', 'sum')
    assert len(aggregated_df) == 2
    assert aggregated_df.loc[aggregated_df['department'] == 'Engineering', 'salary'].iloc[0] == 130000
