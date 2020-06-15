#!/usr/bin/env python3

import matplotlib.pyplot as plt


def interpolate(y1, y2, x1, x2, x_val):
    return y1 + (y2 - y1) / (x2 - x1) * (x_val - x1)


def idealgas_P(V, T):
    # PV = RT => P = RT/V
    gas_constant = 0.4615
    return gas_constant * T / V


vapor_dome_VP = [
    (0.001000, 1.0),
    (0.001010, 10),
    (0.001043, 100),
    (0.001127, 1000),
    (0.001276, 5000),
    (0.001452, 10000),
    (0.001657, 15000),
    (0.002038, 20000),
    (0.002207, 21000),
    (0.002703, 22000),
    (0.003106, 22064),
    (0.003644, 22000),
    (0.005862, 20000),
    (0.018028, 10000),
    (0.039448, 5000),
    (0.099587, 2000),
    (0.19436, 1000),
    (0.37483, 500),
    (0.60582, 300),
    (1.6941, 100),
    (6.2034, 25),
    (14.670, 10),
    (66.990, 2),
    (129.19, 1),
]

# T_sat = 20C
iso_20C = [
    (0.001002, 20000),
    (0.001002, 2.3392),
    (57.762, 2.3392),
]
iso_20C_extrap = [
    (57.762, 2.3392),
    (500.0, idealgas_P(500, 20 + 273.15)),
]

iso_350C = [
    (0.001741, 20000),
    (0.001741, 16529),
    (0.008806, 16529),
    (0.05197, 5000),
    (0.28250, 1000),
    (interpolate(26.446, 31.063, 300, 400, 350), 10),
]

# T_sat = 6.97
iso_1kPa = [
    (0.001000, 20000),
    (0.001000, 1.0),
    (129.19, 1.0),
]
iso_1kPa_extrap = [(129.19, 1.0), (500.0, idealgas_P(500, 6.97 + 273.13))]

# T_sat = 100C
iso_1atm = [
    (0.001043, 20000),
    (0.001043, 101.325),
    (1.6734, 101.325),
    (1.6959, 100),
    (3.4187, 50),
    (17.196, 10),
]

# T_sat = 311.00C
iso_10000kPa = [
    (0.001452, 20000),
    (0.001452, 10000),
    (0.018028, 10000),
    (interpolate(0.05197, 0.05784, 300, 350, 311), 5000),
    (interpolate(0.25799, 0.28250, 300, 350, 311), 1000),
    (interpolate(26.446, 31.063, 300, 400, 311.00), 10),
]

iso_500C = [
    (0.002952, 60000),
    (0.008691, 30000),
    (0.014793, 20000),
    (0.020828, 15000),
    (0.032811, 10000),
    (0.06858, 5000),
    (0.13999, 2500),
    (0.35411, 1000),
    (3.5655, 100),
    (35.680, 10),
]

iso_1000C = [
    (0.009504, 60000),
    (0.019240, 30000),
    (0.029020, 20000),
    (0.038808, 15000),
    (0.058391, 10000),
    (0.11715, 5000),
    (0.23466, 2500),
    (0.58721, 1000),
    (5.8755, 100),
    (58.758, 10),
]

fig = plt.figure()
plt.title("Pressure-Specific Volume Relationship for Water")
plt.xlabel("Specific Volume (m^3/kg)")
plt.ylabel("Pressure (kPa)")
plt.xscale("log")
plt.yscale("log")

vapor_dome_V_vals = list(list(zip(*vapor_dome_VP))[0])
vapor_dome_P_vals = list(list(zip(*vapor_dome_VP))[1])
plt.plot(vapor_dome_V_vals, vapor_dome_P_vals, color="#0000FF")

iso_1kPa_V_vals = list(list(zip(*iso_1kPa))[0])
iso_1kPa_P_vals = list(list(zip(*iso_1kPa))[1])
plt.plot(iso_1kPa_V_vals, iso_1kPa_P_vals, color="#00FFFF")

iso_20C_V_vals = list(list(zip(*iso_20C))[0])
iso_20C_P_vals = list(list(zip(*iso_20C))[1])
plt.plot(iso_20C_V_vals, iso_20C_P_vals, color="#008000")

iso_1atm_V_vals = list(list(zip(*iso_1atm))[0])
iso_1atm_P_vals = list(list(zip(*iso_1atm))[1])
plt.plot(iso_1atm_V_vals, iso_1atm_P_vals, color="#FF00FF")

iso_10000kPa_V_vals = list(list(zip(*iso_10000kPa))[0])
iso_10000kPa_P_vals = list(list(zip(*iso_10000kPa))[1])
plt.plot(iso_10000kPa_V_vals, iso_10000kPa_P_vals, color="#00FF00")

iso_350C_V_vals = list(list(zip(*iso_350C))[0])
iso_350C_P_vals = list(list(zip(*iso_350C))[1])
plt.plot(iso_350C_V_vals, iso_350C_P_vals, color="#FF0000")

iso_500C_V_vals = list(list(zip(*iso_500C))[0])
iso_500C_P_vals = list(list(zip(*iso_500C))[1])
plt.plot(iso_500C_V_vals, iso_500C_P_vals, color="#C0C0C0")

iso_1000C_V_vals = list(list(zip(*iso_1000C))[0])
iso_1000C_P_vals = list(list(zip(*iso_1000C))[1])
plt.plot(iso_1000C_V_vals, iso_1000C_P_vals, color="#800080")

plt.plot(vapor_dome_V_vals[10], vapor_dome_P_vals[10], color="#0000FF", marker="o")

iso_20C_extrap_V_vals = list(list(zip(*iso_20C_extrap))[0])
iso_20C_extrap_P_vals = list(list(zip(*iso_20C_extrap))[1])
plt.plot(
    iso_20C_extrap_V_vals, iso_20C_extrap_P_vals, color="#008000", linestyle="--",
)

iso_1kPa_extrap_V_vals = list(list(zip(*iso_1kPa_extrap))[0])
iso_1kPa_extrap_P_vals = list(list(zip(*iso_1kPa_extrap))[1])
plt.plot(
    iso_1kPa_extrap_V_vals, iso_1kPa_extrap_P_vals, color="#00FFFF", linestyle="--",
)

plt.legend(
    [
        "Vapour Dome",
        "6.97 C (1 kPa)",
        "20 C",
        "100 C (1 atm)",
        "311.00 C (10000 kPa)",
        "350 C",
        "500 C",
        "1000 C",
    ],
    loc="upper right",
)

plt.show()
