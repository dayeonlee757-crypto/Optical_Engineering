import numpy as np
import matplotlib.pyplot as plt

# Mesh creation
x = np.linspace(-5, 5, 500)
y = np.linspace(-5, 5, 500)
X, Y = np.meshgrid(x, y)

# Parameter
w = 0.5 # beam waist
I0 = 1.5 # maximum intensity

# 2D Gaussian
intensity_2d = I0 * np.exp(-2 * (X**2 + Y**2) / (w**2))

# Visuallization (Heatmap)
plt.figure(figsize=(8, 6))
img = plt.imshow(intensity_2d, extent=[-5, 5, -5, 5], cmap='inferno')

# Colorbar
plt.colorbar(img, label='Intensity (a.u.)')

plt.title(f"2D Gaussian Beam Spot (w={w}mm)")
plt.xlabel("x position (mm)")
plt.ylabel("y position (mm)")

# Save
plt.savefig("260130_my_2d_gaussian_beam", dpi=300)
plt.show()

