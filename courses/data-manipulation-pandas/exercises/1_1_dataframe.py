import pandas as pd

data = pd.read_csv('../dataset/homelessness.csv', index_col=0)
df_homeless = pd.DataFrame(data)
print(df_homeless.head())

print(df_homeless.info())

print(df_homeless.shape)

print(df_homeless.describe())

print(df_homeless.values)

print(df_homeless.index)

print(df_homeless.columns)


