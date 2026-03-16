# rocket-motion-simulation
# Rocket Motion Simulation 
## Overview
This project simulates the motion of a rocket using basic physics principles and formulas of newton.
The program calculates the **velocity** and **altitude** of a rocket over time and visualizes the results using graphs.
The simulation considers:
* Thrust produced by the rocket engine
* Gravitational force acting on the rocket
* Engine burn time
* Motion after the fuel burn ends
Two graphs are generated:
1. **Altitude vs Time**
2. **Velocity vs Time**
---
## Objective
The goal of this project is to understand how rocket motion changes over time by applying Newton’s laws of motion and performing a numerical simulation using Python.
---
## Technologies Used
* **Python 3**
* **NumPy** – for numerical calculations
* **Matplotlib** – for plotting graphs
---
## Physics Concept Used
The simulation is based on **Newton’s Second Law of Motion**: [ F = ma ]
Acceleration of the rocket is calculated as: [ a = \frac{Thrust}{Mass} - g ]
Where:
* `Thrust` = force produced by the rocket engine
* `Mass` = mass of the rocket
* `g` = acceleration due to gravity (9.81 m/s²)
After the engine burn time ends, the rocket experiences only gravitational acceleration.
---
## How the Program Works
1. A time array is created from **0 to 100 seconds**.
2. The rocket starts with **initial velocity = 0** and **initial altitude = 0**.
3. During the **burn time**, thrust produces upward acceleration.
4. After the burn time, gravity slows the rocket down.
5. Velocity and altitude are calculated step-by-step.
6. The results are stored and plotted using graphs.
---
## Output
The program generates two plots:
### 1. Altitude vs Time:Shows how the rocket's height changes during the flight.
### 2. Velocity vs Time:Shows how the rocket's velocity changes during acceleration and descent.
---

