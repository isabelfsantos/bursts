import numpy as np
import matplotlib.pyplot as plt

brain = np.random.rand(100, 100)  # Simulate a brain MRI slice with random data
plt.imshow(brain, cmap='gray')
plt.title("Simulated Brain MRI Slice")
plt.axis('off')
plt.show()