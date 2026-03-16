import numpy as np
import matplotlib.pyplot as plt

# constants
g = 9.81
thrust = 15000
mass = 1000
burn_time = 50

time = np.linspace(0,100,500)

velocity = []
altitude = []

v = 0
h = 0
dt = time[1] - time[0]

for t in time:
    if t < burn_time:
        acceleration = (thrust/mass) - g
    else:
        acceleration = -g
    
    v = v + acceleration * dt
    h = h + v * dt
    
    velocity.append(v)
    altitude.append(h)

# plots
plt.figure()
plt.plot(time, altitude)
plt.xlabel("Time (s)")
plt.ylabel("Altitude (m)")
plt.title("Rocket Altitude vs Time")
plt.show()

plt.figure()
plt.plot(time, velocity)
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.title("Rocket Velocity vs Time")
plt.show()