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

# ----------------------------------------------------------------

# Create baseball, a list of lists
baseball_1 = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball_1)

# Print out the type of np_baseball
print(type(np_baseball))

# Print out the shape of np_baseball
print(np_baseball.shape)

# ----------------------------------------------------------------

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the shape of np_baseball
print(np_baseball.shape)

# ----------------------------------------------------------------

# Create np_baseball (2 cols)
np_baseball = np.array(baseball)

# Print out the 50th row of np_baseball
print(np_baseball[49])

# Select the entire second column of np_baseball: np_weight_lb
np_weight_lb = np_baseball[:, 1]

# Print out height of 124th player
print(np_baseball[123, 0])

# ----------------------------------------------------------------

# Create np_baseball (3 cols)
np_baseball = np.array(baseball)

# Print out addition of np_baseball and updated
print(np_baseball + updated)

# Create numpy array: conversion
conversion = [0.0254, 0.453592, 1]

# Print out product of np_baseball and conversion
print(np_baseball * conversion)

