# Aggregating DataFrames

## Mean and median

Summary statistics are exactly what they sound like - they summarize many numbers in one statistic. 

- `mean()`: function that calculates the average value of a given set of numbers in a series or dataframe.
- `median()`: function that finds the middle value of a given set of numbers in a series or dataframe, dividing the data into two equal halves.

## Summarizing dates

Summary statistics can also be calculated on date columns that have values with the data type `datetime64`.

- `max()`: This function returns the maximum value among the given set of numbers in a series or dataframe. It can also be used on date columns to find the latest date.
- `min()`: This function returns the minimum value among the given set of numbers in a series or dataframe. Similarly, it can be used on date columns to find the earliest date.

## Efficient summaries

While pandas and NumPy have tons of functions, sometimes, you may need a different function to summarize your data.

- `agg()`: allows you to apply your own custom functions to a DataFrame.

```python
# A custom IQR function
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)
    
# Print IQR of the temperature_c column
print(df_sales['temperature_c'].agg(iqr))
```

## Cumulative statistics

Cumulative statistics can also be helpful in tracking summary statistics over time.

- `cumsum()`: This function returns the cumulative sum of a series or dataframe. It adds up the values in the sequence cumulatively, meaning that the sum of a number at a particular index is the sum of the numbers at all indices before it, including the number at the current index. 
- `cummax()`: This function returns the cumulative maximum of a series or dataframe. It compares all the previous values and keeps the maximum value up to the current index.

## Dropping duplicates

Removing duplicates is an essential skill to get accurate counts because often, you don't want to count the same thing multiple times. 

- `drop_duplicates()`: remove duplicate rows from the DataFrame. By default, it considers all columns. However, you can specify particular columns to consider for identifying duplicates. The first occurrence of the duplicate row is kept by default, but you can also specify to keep the last occurrence.


## Counting categorical variables

Counting is a great way to get an overview of your data and to spot curiosities that you might not notice otherwise. 

- `df['column'].value_counts()`: returns a series containing counts of unique values in the specified column, in descending order so that the first element is the most frequently-occurring element. It excludes NA values by default.
- `value_counts(normalize=True)`: returns the relative frequencies of the unique values in the specified column, in descending order. The relative frequencies are the proportions or percentages of the total counts, rather than the counts themselves. 
- `value_counts(sort=True)`: returns a series containing counts of unique values in the specified column, sorted in descending order by count. This is the default behavior of value_counts(), so specifying sort=True is not necessary unless sort=False was previously specified.

## Grouped summary statistics

The .groupby() method makes life much easier.

- `.groupby()`: used to split the data into groups based on some criteria. It can be used to group large amounts of data and compute operations on these groups. The criteria can be any function, series, or dataframe that can be used to split an object into groups.

- `sales_stats = sales.groupby("type")["weekly_sales"].agg([np.min, np.max, np.mean, np.median])`

```python
# Group by the 'type' column
grouped = df_sales.groupby('type')

# Now, perform operations on these groups
grouped_sum = grouped.sum()
```

## Pivot Tables

Pivot tables are the standard way of aggregating data in spreadsheets.

- `.pivot_table()`: This function is used to create a spreadsheet-style pivot table as a DataFrame. The levels in the pivot table will be stored in MultiIndex objects (hierarchical indexes) on the index and columns of the result DataFrame. It can take a number of arguments:  
  - values: a column or a list of columns to aggregate.
  - index: a column, Grouper, array which has the same length as data, or list of them. Keys to group by on the pivot table index. If an array is passed, it is being used as the same manner as column values.
  - columns: a column, Grouper, array which has the same length as data, or list of them. Keys to group by on the pivot table column. If an array is passed, it is being used as the same manner as column values.
  - aggfunc: function to use for aggregation, defaulting to `numpy.mean`.

```python
mean_sales_by_type = sales.pivot_table(values="weekly_sales", index="type")

mean_med_sales_by_type = sales.pivot_table(values="weekly_sales", index="type", aggfunc=[np.mean, np.median]) 

mean_sales_by_type_holiday = sales.pivot_table(values="weekly_sales", index="type", columns="is_holiday")

print(sales.pivot_table(values="weekly_sales", index="department", columns="type", fill_value=0, margins=True))

print(sales.pivot_table(values="weekly_sales", index="department", columns="type", fill_value=0, margins=True).sum())
```


