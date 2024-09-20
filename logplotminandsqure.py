import matplotlib.pyplot as plt
import numpy as np

# Number of random samples to generate
num_samples = 10000

# Generate random numbers between 1 and 2000
rand_vals1 = np.random.randint(1, 2001, num_samples)
rand_vals2 = np.random.randint(1, 2001, num_samples)

# Calculate rand() * rand() and min(rand(), rand())
product_vals = rand_vals1 * rand_vals2
min_vals = np.minimum(rand_vals1, rand_vals2)

# Plotting the distribution of rand() * rand()
plt.figure(figsize=(14, 6))

# Plot for rand() * rand()
plt.subplot(1, 2, 1)
plt.hist(product_vals, bins=50, color='b', alpha=0.7)
plt.title("Distribution of rand() * rand()")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.yscale('log')  # Set y-axis to log scale

# Plot for min(rand(), rand())
plt.subplot(1, 2, 2)
plt.hist(min_vals, bins=50, color='r', alpha=0.7)
plt.title("Distribution of min(rand(), rand())")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.yscale('log')  # Set y-axis to log scale

# Show the plots
plt.tight_layout()
plt.show()
