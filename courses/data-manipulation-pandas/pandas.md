# Pandas

## Inspecting a DataFrame

When you get a new DataFrame to work with, the first thing you need to do is explore it and see what it contains. There are several useful methods and attributes for this:

- `.head()` returns the first few rows (the “head” of the DataFrame).
- `.info()` shows information on each of the columns, such as the data type and number of missing values.
- `.shape` returns the number of rows and columns of the DataFrame.
- `.describe()` calculates a few summary statistics for each column.

## Parts of a DataFrame

To better understand DataFrame objects, it's useful to know that they consist of three components, stored as attributes:

- `.values`: A two-dimensional NumPy array of values.
- `.columns`: An index of columns: the column names.
- `.index`: An index for the rows: either row numbers or row names.

## Sorting rows

Finding interesting bits of data in a DataFrame is often easier if you change the order of the rows. You can sort the rows by passing a column name to `.sort_values()`.

- `.sort_values('column')`: returns the dataframe sorted by choice column in ascending order by default.
- `.sort_values('column', ascending=False)`: sorting by descending order.
- `.sort_values(['column_1', 'column_2'] ascending=[True, False])`: sorting more than 1 column with different ascending order.

## Subsetting columns

When working with data, you may not need all the variables in your dataset. Square brackets (`[]`) can be used to select only the columns that matter to you in an order that makes sense to you.

- `df_data['column_name']`: returns the `column_name` column.
- `df_data[[column_1', 'column_2']]`: returns multiple columns.
- `dt_data[df_data['column_name'] condition]`: returns a dataframe according to the condition.
  - `] > 10000]`
  - `] == 'Montain'`
  - `] condition) & (condition ]`

## Subsetting rows by categorical variables

Subsetting data based on a categorical variable often involves using the "or" operator (`|`) to select rows from multiple categories.

- `.isin()` method

```python
colors = ["brown", "black", "tan"]
condition = dogs["color"].isin(colors)
dogs[condition]
```

```python
south_mid_atlantic = df_homeless[df_homeless['region'].isin(['South Atlantic', 'Mid-Atlantic'])]
```

```python
canu = ["California", "Arizona", "Nevada", "Utah"]
mojave_homelessness = df_homeless[df_homeless['state'].isin(canu)]
```

## Adding new columns

You aren't stuck with just the data you are given. Instead, you can add new columns to a DataFrame. This has many names, such as transforming, mutating, and feature engineering.

```python
# Add total col as sum of individuals and family_members
df_homeless["total"] = df_homeless["individuals"] + df_homeless["family_members"]

# Add p_individuals col as proportion of total that are individuals
df_homeless["p_individuals"] = df_homeless["individuals"] / df_homeless["total"]
```


