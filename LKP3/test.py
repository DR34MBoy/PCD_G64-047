import matplotlib.pyplot as plt
import numpy as np

# Generate random data from a normal distribution
data = np.random.normal(0, 1, 1000)

# Plot the normalized histogram
n, bins, patches = plt.hist(data, bins=50, density=True, color='blue', alpha=0.7, rwidth=0.85)

# Add a line for the probability density function
y = ((1 / (np.sqrt(2 * np.pi))) * np.exp(-0.5 * (1 / 1) * (bins - 0)**2))
plt.plot(bins, y, '--', color='red', linewidth=1.5)

# Add labels and title
plt.xlabel('X')
plt.ylabel('Probability Density')
plt.title('Normalized Histogram')

# Show the plot
plt.show()