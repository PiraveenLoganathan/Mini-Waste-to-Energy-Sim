

import matplotlib.pyplot as plt
import numpy as np


daily_waste_kg = [50, 60, 55, 70, 65, 60, 75]  # Example: one week

# Constants
biogas_yield_m3_per_kg = 0.5  # m³ biogas per kg of organic waste
energy_kwh_per_m3 = 6          # kWh per m³ of biogas
efficiency_levels = [0.75, 0.85, 0.95]  # Scenario analysis: low, normal, high efficiency


energy_outputs = {}
cumulative_outputs = {}

for eff in efficiency_levels:
    daily_energy = [waste * biogas_yield_m3_per_kg * energy_kwh_per_m3 * eff for waste in daily_waste_kg]
    energy_outputs[eff] = daily_energy
    cumulative_outputs[eff] = np.cumsum(daily_energy)

print("Energy Output Table (kWh) for Different Efficiencies")
print("Day | 75% Eff | 85% Eff | 95% Eff")
print("-----------------------------------")
for i in range(len(daily_waste_kg)):
    print(f"{i+1:3} | {energy_outputs[0.75][i]:7.2f} | {energy_outputs[0.85][i]:7.2f} | {energy_outputs[0.95][i]:7.2f}")


print("\nSummary Statistics:")
for eff in efficiency_levels:
    print(f"Efficiency {int(eff*100)}%: Total={sum(energy_outputs[eff]):.2f} kWh, "
          f"Average={np.mean(energy_outputs[eff]):.2f} kWh, Max={max(energy_outputs[eff]):.2f} kWh, "
          f"Min={min(energy_outputs[eff]):.2f} kWh")


days = [f"Day {i}" for i in range(1, len(daily_waste_kg)+1)]
colors = ['#6aa84f', '#93c47d', '#f1c232']  # Green shades for bars

plt.figure(figsize=(12,7))


bar_width = 0.25
x = np.arange(len(days))
for idx, eff in enumerate(efficiency_levels):
    plt.bar(x + idx*bar_width, energy_outputs[eff], width=bar_width, color=colors[idx],
            label=f"{int(eff*100)}% Efficiency")
   
    for i, val in enumerate(energy_outputs[eff]):
        plt.text(i + idx*bar_width, val + 1, f"{val:.1f}", ha='center', fontsize=9)


for eff in efficiency_levels:
    plt.plot(x + bar_width, cumulative_outputs[eff], linestyle='--', marker='o', label=f"Cumulative {int(eff*100)}%")

plt.xticks(x + bar_width, days)
plt.title("Daily & Cumulative Energy Output from Organic Waste", fontsize=16)
plt.xlabel("Day", fontsize=12)
plt.ylabel("Energy Output (kWh)", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()
