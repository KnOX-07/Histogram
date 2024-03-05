import matplotlib.pyplot as plt
import numpy as np

#Generate random data for demonstration
data = np.random.randn(1000)

#Plotting the histogram
plt.hist(data, bins = 20, color = 'blue', alpha = 0.7)

#Adding labels and title
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram')

#show the plot
plt.show()
