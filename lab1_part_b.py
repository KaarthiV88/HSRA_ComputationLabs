import math
import numpy as np

#Damped Molecular Dynamics

def forceReturn(pos):
    Vlj = 4*1*(-12*(1/pos)**13 + 6 * (1/pos)**7)
    return Vlj

print(forceReturn(0.3))

def accelerationCalc(force, mass):
    return "Acceleration: " + str(float(force/mass))

print(accelerationCalc(10, 7))

def moveCalc(velocity, acceleration):
    delta_t = 0.1
    delta_r = "{:.2f}".format(velocity*delta_t + 0.5*acceleration*(delta_t**2))
    #delta_r = "{:.2f}".format(delta_r)
    new_velocity = "{:.2f}".format(acceleration * delta_t)
    return "Movement: " + str(delta_r) + "m\n" + "New Velocity: " + str(new_velocity) + "m\s"

print(moveCalc(10, 3))
