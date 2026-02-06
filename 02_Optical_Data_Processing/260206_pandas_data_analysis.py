import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Data Creation (Voltage vs. Phase shift)
data = {
    'Voltage_V' : np.linspace(0, 10, 20),
    'Phase_Shift_rad' : [0, 0, 0, 0.1, 0.5, 1.2, 2.5, 3.8, 4.5, 5.2, 
                        5.8, 6.1, 6.3, 6.4, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5]
}
df = pd.DataFrame(data)

# 2. Exploring Data: Print 5 rows 
print("--- Data Preview ---")
print(df.head())

# 3. Filtering Data: Extract the region only if phase shift > 1.0 rad
significant_phase = df[df['Phase_Shift_rad'] > 1.0]
print("\n--- High Phase Shift Region ---")
print(significant_phase)

# 3. Analysis: Threshold Voltage
# when phase shift > 0.2 rad
v_th = df[df['Phase_Shift_rad'] > 0.2]['Voltage_V'].iloc[0]
phase_mean = df['Phase_Shift_rad'].mean()
phase_max = df['Phase_Shift_rad'].max()
print(f"\nEstimated Threshold Voltage (V_th): {v_th} V")
print(f"Average Phase Shift: {phase_mean:.2f} rad")
print(f"Maximum Phase Shift: {phase_max:.2f} rad")

# Visualization
plt.figure(figsize=(8, 5))
plt.plot(df['Voltage_V'], df['Phase_Shift_rad'], 'o-', label='LC Phase Response')
plt.axvline(x=v_th, color='r', linestyle='--', label=f'V_th ≈ {v_th:.2f}V')
plt.title('Voltage-dependent Phase Shift')
plt.xlabel('Voltage (V)')
plt.ylabel('Phase Shift (rad)')
plt.legend()
plt.grid(True)
plt.show()