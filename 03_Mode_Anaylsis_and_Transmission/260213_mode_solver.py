import meep as mp
from meep import mpb
import numpy as np
import matplotlib.pyplot as plt

# Parameter setting
w = 0.5 # waveguide width (um)
h = 0.22 # Si thickness (standard SOI)
n_si = 3.45
n_so2 = 1.45

# Define ROI and geometry
geometry_lattice = mp.Lattice(size=mp.Vector3(0, 4, 4)) # 2D cross-section
geometry = [mp.Block(size=mp.Vector3(mp.inf, w, h),
                     center=mp.Vector3(),
                     material=mp.Medium(index=n_si))]

# Mode solver setting
ms = mpb.ModeSolver(
    geometry_lattice=geometry_lattice,
    geometry=geometry,
    default_material=mp.Medium(index=n_so2),
    resolution=32
)

# Find a k-point at a target wavelength (1.55um)
target_freq = 1/1.55
k_result = ms.find_k(mp.NO_PARITY, target_freq, 1, 1, mp.Vector3(1, 0, 0), 1e-6, target_freq*2.5, target_freq*1.1, target_freq*3.5)

# Result
n_eff = k_result[0] / target_freq
print(f"--- Result ---")
print(f"Effective Index (n_eff) at 1.55um: {n_eff:.4f}")

# E-field (Ey data from first band
e_field = ms.get_efield(1)
ey_data = e_field[0, :, :, 1]


# 2D plotting
plt.figure(figsize=(8, 6))
# Find intensity distribution using absolute values
plt.imshow(np.abs(ey_data).T, cmap='magma', origin='lower', extent=[-2, 2, -2, 2])
plt.gca().set_aspect('equal')
plt.colorbar(label='Electric Field Intensity')
plt.title(f"TE-like Mode Profile (n_eff={n_eff:.4f})")
plt.xlabel("y (um)")
plt.ylabel("z (um)")
plt.xlim(-1, 1)
plt.ylim(-0.5, 0.5)

plt.savefig("mode_profile.png")
plt.show()

print("Completed!")

