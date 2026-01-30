import gdsfactory as gf
gf.gpdk.PDK.activate()
# 1. Creation of circuit
c =gf.Component("My_first_circuit")

s = c << gf.components.straight(length=10, width=0.5)
b = c << gf.components.bend_circular(radius=5, width=0.5)

# Connection
b.connect("o1", s.ports["o2"])


# Visualization
c.show()