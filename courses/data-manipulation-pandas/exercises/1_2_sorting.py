import pandas as pd

data = pd.read_csv('../dataset/homelessness.csv', index_col=0)
df_homeless = pd.DataFrame(data)

df_homeless.sort_values('individuals')

df_homeless.sort_values('family_members', ascending=False)

df_homeless.sort_values(['region', 'family_members'], ascending=[True, False])

