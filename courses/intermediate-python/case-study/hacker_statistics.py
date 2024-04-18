# Import numpy, matplotlib
import numpy as np
import matplotlib.pyplot as plt

# Set seed
np.random.seed(123)

# Initialize all_walks (don't change this line)
all_walks = []

# Simulate random walk five times
for i in range(500):
    # Initialize random_walk
    random_walk = [0]

    # Complete the for loop
    for x in range(100):
        # Set step: last element in random_walk
        step = random_walk[-1]

        # Roll the dice
        dice = np.random.randint(1, 7)

        # Determine next step
        if dice <= 2:
            # Replace below: use max to make sure step can't go below 0
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1, 7)

        # Implement clumsiness
        if np.random.rand() <= 0.005:
            step = 0

        # append next_step to random_walk
        random_walk.append(step)

    # Append random_walk to all_walks
    all_walks.append(random_walk)

# Convert all_walks to NumPy array: np_aw
np_aw = np.array(all_walks)

# Transpose np_aw: np_aw_t
np_aw_t = np.transpose(np_aw)


plt.clf()


# Select last row from np_aw_t: ends
ends = np_aw_t[-1, :]

# Plot histogram of ends, display plot
plt.hist(ends)

plt.ylabel('Total number of times last floor reached ')
plt.xlabel('Last floor after 100 rounds')
plt.title('Dice Challenge')

plt.show()



