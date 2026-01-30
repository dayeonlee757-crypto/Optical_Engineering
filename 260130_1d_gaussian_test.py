import numpy as np
import matplotlib.pyplot as plt

# 1. Data creation
x = np.linspace(-5, 5, 10000)

# Setting parameter
w = 2.0  # beam waist
I0 = 1.0  # maximum intensity of light

# Gaussian beam
intensity = I0 * np.exp(-2 * (x**2) / (w**2))

# Visualization
plt.figure(figsize=(8, 5))
plt.plot(x, intensity, label='Gaussian Beam Profile', color='blue')
plt.title('1D Gaussian Beam Intensity')
plt.xlabel('Position (mm)')
plt.ylabel('Intensity (a.u.)')
plt.grid(True)
plt.legend()
plt.savefig("my_1D_gaussian_beam.png", dpi=300)
plt.show()


