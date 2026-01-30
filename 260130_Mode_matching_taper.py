import gdsfactory as gf
gf.gpdk.PDK.activate()

# Creation Component
c = gf.Component("Gaussian_Input_Structure")

# Taper Creation for matching spot size of beam with waveguide
taper = c << gf.components.taper(length=20, width1=10.0, width2=0.5)

#  Straight waveguide Creation and connection
wg = c << gf.components.straight(length=30, width=0.5)
wg.connect("o1", taper.ports["o2"])

c.show()
c.write_gds("260130_final_taper_design.gds")