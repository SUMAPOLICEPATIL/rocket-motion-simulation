import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest


g = 9.81
thrust = 20000
mass = 1200
burn_time = 60

time = np.linspace(0,120,600)
dt = time[1]-time[0]

velocity = []
altitude = []
acceleration_list = []

v = 0
h = 0

for t in time:
    
    if t < burn_time:
        acceleration = (thrust/mass) - g
    else:
        acceleration = -g
        
    v = v + acceleration*dt
    h = h + v*dt
    
    velocity.append(v)
    altitude.append(h)
    acceleration_list.append(acceleration)

data = pd.DataFrame({
    "time": time,
    "altitude": altitude,
    "velocity": velocity,
    "acceleration": acceleration_list
})

data.loc[300:310,"velocity"] = data["velocity"]*0.2

model = IsolationForest(contamination=0.02)

features = data[["altitude","velocity","acceleration"]]

data["anomaly"] = model.fit_predict(features)

plt.figure()
plt.plot(data["time"],data["altitude"])
plt.xlabel("Time")
plt.ylabel("Altitude")
plt.title("Rocket Altitude vs Time")
plt.show()

plt.figure()
plt.plot(data["time"],data["velocity"])
plt.xlabel("Time")
plt.ylabel("Velocity")
plt.title("Rocket Velocity vs Time")
plt.show()

# Highlight anomalies
anomalies = data[data["anomaly"]==-1]

plt.figure()
plt.scatter(data["time"],data["velocity"],label="Normal")
plt.scatter(anomalies["time"],anomalies["velocity"],color="red",label="Anomaly")
plt.legend()
plt.title("Telemetry Anomaly Detection")
plt.show()