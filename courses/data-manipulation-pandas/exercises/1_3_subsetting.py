import pandas as pd

data = pd.read_csv('../dataset/homelessness.csv', index_col=0)
df_homeless = pd.DataFrame(data)

individuals = df_homeless['individuals']

homeless_reg_fam = df_homeless[['region', 'family_members']]

ind_state = df_homeless[['individuals', 'state']]

ind_gt_10k = df_homeless[df_homeless['individuals'] > 10000]

mountain_reg = df_homeless[df_homeless['region'] == 'Mountain']

fam_lt_1k_pac = df_homeless[(df_homeless['family_members'] < 1000) & (df_homeless['region'] == 'Pacific')]
