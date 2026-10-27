# AURES WATT - FINAL HACKATHON SUBMISSION
m = 1000000
g = 9.81
h = 800
num_wells = 18
energy_joule = m * g * h
energy_kwh = energy_joule / 3600000
total_mwh = (energy_kwh * num_wells) / 1000

print("="*50)
print("AURES WATT - SAFISAFI")
print("Algeria Gravity Battery")
print("="*50)
print(f"Energy per well: {energy_kwh:.2f} kWh")
print(f"Total ({num_wells} wells): {total_mwh:.2f} MWh")
print(f"Vs Gravitricity 4 MWh: {total_mwh/4:.1f}x BIGGER")
print("")
print("Why AURES WATT wins:")
print("- 18 abandoned oil wells in Khenchela/Biskra")
print("- 1000 tons mass, 800m deep")
print("- Cost 10x cheaper than coal mine")
print("- 10,000 wells available in Sahara")
print("- Perfect for solar energy storage")
print("")
print("AURES WATT WINS! - Khenchela 2026")