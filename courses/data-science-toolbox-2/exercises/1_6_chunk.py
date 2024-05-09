import pandas as pd

result = []
for chunk in pd.read_csv('../dataset/tweets.csv', chunksize=100):
    result.append(sum(chunk['x']))
total = sum(result)
print(total)

total = 0
for chunk in pd.read_csv('../dataset/tweets.csv', chunksize=100):
    total += sum(chunk['x'])
print(total)
