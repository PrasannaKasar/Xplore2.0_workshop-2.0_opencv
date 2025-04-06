import numpy as np

sample = np.array([1, 2, 3, 4, 5])
kernel = np.array([1, 0, -1])

output = np.convolve(sample, kernel, mode='same')  # Options: 'full', 'valid', 'same'
print("1D Convolution Output:", output)
