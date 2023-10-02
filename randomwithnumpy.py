import random

def roll_dice():
    return random.randint(1, 6)

# Example usage:
result = roll_dice()
print("You rolled a dice and got:", result)
# _______________________________________________________________________________________________________________________________

import numpy as np
import random
# Initialize random_walk
random_walk = [0]
for x in range(100) :
    # Set step: last element in random_walk
    step = random_walk[-1]
    # Roll the dice
    dice = np.random.randint(1,7)

    # Determine next step
    if dice <= 2:
        step = step - 1
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    # append next_step to random_walk
    random_walk.append(step)

# Print random_walk
print(random_walk)
import matplotlib.pyplot as plt

plt.plot(random_walk)
plt.show()
#
# _______________________________________________________________________________________________________________________________

#
rows = 4

for i in range(1, rows+1):
    for j in range(1, i+1):
        if i < j:
            continue
        else:
            print(i*j, end ='')
    print()
#
# house list of lists
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Build a for loop from scratch
for area in house:
    print('The ' +str(area[0]) +'is ' +
    str(area[1]) +"sqm")
# _______________________________________________________________________________________________________________________________


# Definition of dictionary
europe = {'spain': 'madrid', 'france': 'paris', 'germany': 'berlin',
          'norway': 'oslo', 'italy': 'rome', 'poland': 'warsaw', 'austria': 'vienna'}

# Iterate over europe
for country, capital in europe.items():
    print('the capital of ' + str(country) + " is " + str(capital))
# _______________________________________________________________________________________________________________________________


import numpy as np
import random
np.random.seed(123)
result = [0]
for x in range(10):
    coin = np.random.randint(0,2)
    result.append(result[x] + coin)

print(result)

# _______________________________________________________________________________________________________________________________

numpy and matplotlib imported, seed set.

initialize and populate all_walks
import random
import matplotlib.pyplot as plt
import numpy as np
all_walks = []
for i in range(5) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)
    all_walks.append(random_walk)

# Convert all_walks to NumPy array: np_aw
np_aw = np.array(all_walks)

# Plot np_aw and show
plt.plot(np_aw)
plt.show()
plt.clf()

# Clear the figure
plt.clf()
plt.show()

# _______________________________________________________________________________________________________________________________

# numpy and matplotlib imported, seed set.
import matplotlib.pyplot as plt

# initialize and populate all_walks
all_walks = []
for i in range(5) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)
    all_walks.append(random_walk)

# Convert all_walks to NumPy array: np_aw
np_aw = np.array(all_walks)

# Plot np_aw and show
plt.plot(np_aw)
plt.show()

# Clear the figure
plt.clf()

# Transpose np_aw: np_aw_t
np_aw_t = np.transpose(np_aw)

# Plot np_aw_t and show
plt.plot(np_aw_t)
plt.show()


# _______________________________________________________________________________________________________________________________

# numpy and matplotlib imported, seed set

# Simulate random walk 500 times
all_walks = []
for i in range(500) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        if np.random.rand() <= 0.001 :
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))

# Select last row from np_aw_t: ends
ends = np_aw_t[-1, :]

# Plot histogram of ends, display plot
plt.hist(ends)
plt.show()

# _______________________________________________________________________________________________________________________________
