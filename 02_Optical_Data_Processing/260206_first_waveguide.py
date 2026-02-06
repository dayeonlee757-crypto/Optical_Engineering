import meep as mp
import matplotlib.pyplot as plt

# 1. Simulation cell size
cell = mp.Vector3(16, 8, 0)

# 2. Silicon Waveguide
# n = 3.45, x-axis, thickness = 0.5um
geometry = [mp.Block(mp.Vector3(mp.inf, 0.5, mp.inf),
                    center=mp.Vector3(),
                    material=mp.Medium(index=3.45))]

# 3. Light Source: Continuous source, wavelength = 1.55um
sources = [mp.Source(mp.ContinuousSource(wavelength=1.55), 
                    component=mp.Ez,
                    center= mp.Vector3(-7, 0, 0),
                    size=mp.Vector3(0, 1, 0))]

# 4. Boundary condition & Resolution
# Perfectly matched layer (100% absorb the light)
sim = mp.Simulation(cell_size=cell,
                     boundary_layers=[mp.PML(1.0)],
                     sources=sources,
                     resolution=20) # 20 grids/um

# 5. Visualization
plt.figure(figsize=(10, 5))
sim.plot2D()
plt.title("Waveguide Geometry Setup")
plt.show()

# 6. Run simulation (until the light propagates enough)
sim.run(until=50)

# 7. Visualization E-field
plt.figure(figsize=(10, 5))
sim.plot2D(fields=mp.Ez)
plt.title("Electric Field (Ez) Distribution")
plt.savefig('260206_waveguide-ez-field.png', dpi=300)
print("Saved a image")
plt.show()