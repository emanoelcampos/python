import numpy as np

baseball = []

with open('../dataset/baseball.csv', 'r') as baseball_csv:
    lines = baseball_csv.readlines()

for line in lines[1:]:
    values = line.strip().split(',')
    height = int(values[3].strip())
    weight = int(values[4].strip())
    age = float(values[5].strip())
    baseball.append((height, weight, age))

np_baseball = np.array(baseball)

# ------------------------------------------------------

# Create np_height_in from np_baseball
np_height_in = np_baseball[:, 0]

# Print out the mean of np_height_in
print(np.mean(np_height_in))

# Print out the median of np_height_in
print(np.median(np_height_in))

# ------------------------------------------------------

# Print mean height (first column)
avg = np.mean(np_baseball[:, 0])
print("Average: " + str(avg))

# Print median height. Replace 'None'
med = np.median(np_baseball[:, 0])
print("Median: " + str(med))

# Print out the standard deviation on height. Replace 'None'
stddev = np.std(np_baseball[:, 0])
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column. Replace 'None'
corr = np.corrcoef(np_baseball[:, 0], np_baseball[:, 1])
print("Correlation: " + str(corr))

# ------------------------------------------------------

