import meep as mp
import matplotlib.pyplot as plt

def run_waveguide_simulation(w):
    # Simulation Area
    cell = mp.Vector3(16, 8, 0)

    # Silicon Waveguide
    geometry = [mp.Block(mp.Vector3(mp.inf, w, mp.inf),
                         center=mp.Vector3(),
                         material=mp.Medium(index=3.45))]
    
    # Source
    sources = [mp.Source(mp.ContinuousSource(wavelength=1.55),
                         component=mp.Ez,
                         center=mp.Vector3(-7, 0, 0),
                         size=mp.Vector3(0, 1, 0))]
    
    # Simulation Initialization
    sim = mp.Simulation(cell_size=cell,
                        boundary_layers=[mp.PML(1.0),],
                        geometry=geometry,
                        sources=sources,
                        resolution=20)
    
    # Run
    sim.run(until=50)

    # Visualization
    plt.figure(figsize=(10, 5))
    sim.plot2D(fields=mp.Ez)
    plt.title(f"Waveguide Width: {w} um")

    file_name = f"waveguide_w{w}.png"
    plt.savefig(file_name)
    print(f"Completed width {w}um simulation and Saved as png.")

 # Loop
widths = [0.4, 0.5, 0.6]
for w in widths:
    run_waveguide_simulation(w)