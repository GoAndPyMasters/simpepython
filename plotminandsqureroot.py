# this is functon for plotting min and sqrt between random numbers

import matplotlib.pyplot as plt
import numpy as np

# Number of random samples to generate
num_samples = 1000000

# Generate random numbers between 1 and 2000
rand_vals1 = np.random.randint(1, 10000, num_samples)
rand_vals2 = np.random.randint(1, 10000, num_samples)

# Calculate rand()^0.5 and min(rand(), rand())
sqrt_rand_vals = np.sqrt(rand_vals1)  # rand()^0.5
min_vals = np.maximum(rand_vals1, rand_vals2)

# Plotting the distributions
plt.figure(figsize=(14, 6))

# Plot for rand()^0.5
plt.subplot(1, 2, 1)
plt.hist(sqrt_rand_vals, bins=50, color='b', alpha=0.7)
plt.title("Distribution of rand()^0.5")
plt.xlabel("Value")
plt.ylabel("Frequency")

# Plot for min(rand(), rand())
plt.subplot(1, 2, 2)
plt.hist(min_vals, bins=50, color='r', alpha=0.7)
plt.title("Distribution of min(rand(), rand())")
plt.xlabel("Value")
plt.ylabel("Frequency")

# Show the plots
plt.tight_layout()
plt.show()
