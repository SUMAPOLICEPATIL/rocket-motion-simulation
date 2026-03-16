# Rocket Motion Simulation & Telemetry Anomaly Detection 

## Overview
This project simulates the motion of a rocket using basic physics principles and analyzes the generated telemetry data using machine learning techniques.
The program calculates the **velocity**, **altitude**, and **acceleration** of a rocket over time and visualizes the results using graphs. Additionally, the project applies **anomaly detection** on rocket telemetry data to identify unusual behavior in the rocket's velocity.
The simulation considers:

* Thrust produced by the rocket engine
* Gravitational force acting on the rocket
* Engine burn time
* Motion after the fuel burn ends
* Telemetry anomaly detection using machine learning

The program generates visualizations for:
1. **Altitude vs Time**
2. **Velocity vs Time**
3. **Telemetry Anomaly Detection**
---
## Objective
The goal of this project is to:
* Simulate rocket motion using Newton’s laws of motion.
* Generate telemetry data such as altitude, velocity, and acceleration.
* Detect anomalies in rocket telemetry using **Isolation Forest**, an unsupervised machine learning algorithm.
This type of analysis is useful in **aerospace monitoring systems**, where abnormal telemetry values can indicate potential system failures.
---
## Technologies Used
* **Python 3**
* **NumPy** – numerical calculations
* **Pandas** – telemetry data handling
* **Matplotlib** – graph visualization
* **Scikit-learn** – anomaly detection using Isolation Forest
---
## Physics Concept Used
The simulation is based on **Newton’s Second Law of Motion**: F = ma
Acceleration of the rocket is calculated as: a = (Thrust / Mass) - g
Where:
* `Thrust` = force produced by the rocket engine
* `Mass` = mass of the rocket
* `g` = acceleration due to gravity (9.81 m/s²)
During the **burn phase**, the rocket accelerates due to engine thrust
After the **burn time**, the rocket experiences only gravitational acceleration.
---
## Machine Learning Concept Used
The project uses **Isolation Forest**, an unsupervised machine learning algorithm for anomaly detection.
Isolation Forest works by:
* Randomly selecting features
* Randomly splitting data points
* Isolating abnormal observations faster than normal data
In this project:
* A sudden drop in velocity is artificially introduced
* The model detects these abnormal values as **anomalies**
---
## How the Program Works
1. A time array is created from **0 to 120 seconds**.
2. The rocket starts with **initial velocity = 0** and **initial altitude = 0**.
3. During the **burn time**, thrust produces upward acceleration.
4. After the burn time, gravity slows the rocket down.
5. Velocity, altitude, and acceleration are calculated step-by-step.
6. Telemetry data is stored in a **Pandas DataFrame**.
7. Artificial anomalies are introduced in the velocity data.
8. An **Isolation Forest model** detects abnormal telemetry values.
9. Graphs are generated to visualize the rocket motion and detected anomalies.
---
## Output
The program generates three plots:
### 1. Altitude vs Time : Shows how the rocket's height changes during the flight.
### 2. Velocity vs Time : Shows how the rocket's velocity changes during acceleration and descent.
### 3. Telemetry Anomaly Detection : Displays velocity data with detected anomalies highlighted in **red**.
---
