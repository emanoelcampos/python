import pandas as pd

data = pd.read_csv('../dataset/homelessness.csv', index_col=0)
df_homeless = pd.DataFrame(data)

south_mid_atlantic = df_homeless[df_homeless['region'].isin(['South Atlantic', 'Mid-Atlantic'])]

canu = ["California", "Arizona", "Nevada", "Utah"]

mojave_homelessness = df_homeless[df_homeless['state'].isin(canu)]
