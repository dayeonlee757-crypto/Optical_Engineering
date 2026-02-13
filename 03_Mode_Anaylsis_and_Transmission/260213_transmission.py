import meep as mp
import matplotlib.pyplot as plt

# Parameter setting
w = 0.5
h = 0.22
L = 10.0 # length of waveguide
resolution = 32

# Cell and geometry
pml_thick = 1.0
sx = L + 4.0
sy = 4.0
cell = mp.Vector3(sx, sy, 0)

geometry = [mp.Block(size=mp.Vector3(mp.inf, w, mp.inf),
                     center=mp.Vector3(),
                     material=mp.Medium(index=3.45))]

# Light source (Gaussian Pulse)
fcen = 1/1.55
df = 0.1
sources = [mp.EigenModeSource(mp.GaussianSource(fcen, fwidth=df),
                     component=mp.Ey,
                     center=mp.Vector3(-sx/2 + pml_thick + 0.5, 0, 0),
                     size=mp.Vector3(0, 2, 0),
                     direction=mp.X,
                     eig_band=1,
                     eig_match_freq=True)]

# Monitor setting (Input/Output flux)
nfreq = 100 # number of wavelength points
re_in = mp.FluxRegion(center=mp.Vector3(-sx/2 + pml_thick + 1.5, 0, 0), size=mp.Vector3(0, 2, 0))
re_out= mp.FluxRegion(center=mp.Vector3(sx/2 - pml_thick - 1.0, 0, 0), size=mp.Vector3(0, 2, 0))

sim = mp.Simulation(cell_size=cell,
                    geometry=geometry,
                    sources=sources,
                    resolution=resolution,
                    boundary_layers=[mp.PML(1.0)])

# Add monitor
in_flux = sim.add_flux(fcen, df, nfreq, re_in)
out_flux = sim.add_flux(fcen, df, nfreq, re_out)

# Run
sim.run(until_after_sources=mp.stop_when_fields_decayed(50, mp.Ey, mp.Vector3(sx/2-0.5, 0, 0), 1e-6))

# Result
input_powers = mp.get_fluxes(in_flux)
output_powers = mp.get_fluxes(out_flux)

print(f"Transmission at central frequency: {output_powers[nfreq//2] / input_powers[nfreq//2]:.4f}")