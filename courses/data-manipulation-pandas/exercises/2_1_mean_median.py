import pandas as pd
import numpy as np

sales = pd.read_csv('../dataset/sales_subset.csv')
df_sales = pd.DataFrame(sales)

# Print the head of the sales DataFrame
print(df_sales.head())

# Print the info about the sales DataFrame
print(df_sales.info())

# Print the mean of weekly_sales
print(df_sales['weekly_sales'].mean())

# Print the median of weekly_sales
print(df_sales['weekly_sales'].median())

# Print the maximum of the date column
print(df_sales['date'].max())

# Print the minimum of the date column
print(df_sales['date'].min())


# A custom IQR function
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)


# Print IQR of the temperature_c column
print(df_sales['temperature_c'].agg(iqr))


# A custom IQR function
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)


# Update to print IQR of temperature_c, fuel_price_usd_per_l, & unemployment
print(df_sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]].agg(iqr))


# Import NumPy and create custom IQR function
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)


# Update to print IQR and median of temperature_c, fuel_price_usd_per_l, & unemployment
print(df_sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]].agg([iqr, np.median]))

# Sort sales_1_1 by date
df_sales = df_sales.sort_values('date')

# Get the cumulative sum of weekly_sales, add as cum_weekly_sales col
df_sales['cum_weekly_sales'] = df_sales['weekly_sales'].cumsum()

# Get the cumulative max of weekly_sales, add as cum_max_sales col
df_sales['cum_max_sales'] = df_sales['weekly_sales'].cummax()

# See the columns you calculated
print(df_sales[["date", "weekly_sales", "cum_weekly_sales", "cum_max_sales"]])
