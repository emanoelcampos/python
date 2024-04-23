import pandas as pd

data = pd.read_csv('../dataset/homelessness.csv', index_col=0)
df_homeless = pd.DataFrame(data)

# Add total col as sum of individuals and family_members
df_homeless["total"] = df_homeless["individuals"] + df_homeless["family_members"]

# Add p_individuals col as proportion of total that are individuals
df_homeless["p_individuals"] = df_homeless["individuals"] / df_homeless["total"]
