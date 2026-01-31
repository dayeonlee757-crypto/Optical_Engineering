# Basic Physics Modeling & PIC Layout Design

This folder documents the initial workflow of bridging theoretical optical modeling with practical **Photonic Integrated Circuit ((PIC))** layout generation.

## Key Achievement (Jan 30, 2026)

### 1. Gaussian Beam Profile Simulation
Numerical modeling of Gaussian beam intensity distribution for optical input sources. 
- Developed 1D and 2D intensity profiles using NumPy and Matplotlib.
- Evaluated beam waist ($w$) and peak intensity ($I_0$) through cross-sectional heatmaps.
$$I(x, y) = I_0 \exp\left(-2 \frac{x^2 + y^2}{w^2}\right)$$

#### Simulation Results
| 1D Intensity Profile | 2D Intensity Heatmap |
| :---: | :---: |
| ![1D](./260130_my_1d_gaussian_beam.png) | ![2D](./260130_my_2d_gaussian_beam.png) |

### 2. Adiabatic Waveguide Taper Design
Implementation of an adiabatic taper to minimize transmission loss.
- Utilized **gdsfactory** for a Python-based PDK (Process Design Kit) workflow.
- Validated the generated layout for adiabatic transition using **KLayout**

## Technical Stack
- **Languages**: Python (NumPy, Matplotlib)
- **Design Tools**: gdsfactory, KLayout
- **Physics**: Gaussian Optics, Waveguide Theory

---
*Note: This repository was developed with the assistance of AI to optimize documentation and initial code structuring, allowing for a focused research workflow.