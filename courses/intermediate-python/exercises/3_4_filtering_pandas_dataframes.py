# Import cars data
import pandas as pd
cars = pd.read_csv('../dataset/cars.csv', index_col=0)

# Extract drives_right column as Series: dr
dr = cars["drives_right"]

# Use dr to subset cars: sel
sel = cars[dr]

# Print sel
print(sel)

# --------------------------------------------------------

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col=0)

# Convert code to a one-liner
sel = cars[cars['drives_right']]

# Print sel
print(sel)

# --------------------------------------------------------

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col=0)

# Create car_maniac: observations that have a cars_per_cap over 500
car_maniac = cars[cars['cars_per_cap'] > 500]

# Print car_maniac
print(car_maniac)

# --------------------------------------------------------

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Import numpy, you'll need this
import numpy as np

# Create medium: observations with cars_per_cap between 100 and 500
cpc = cars['cars_per_cap']
between = np.logical_and(cpc >= 100, cpc <= 500)
medium = cars[between]

# Print medium
print(medium)


