import math
import numpy as np

def forceReturn(pos):
    Vlj = 4*1*(-12*(1/pos)**13 + 6 * (1/pos)**7)
    return Vlj

print(forceReturn(0.3))

def accelerationCalc(force, mass):
    return "Acceleration: " + str(float(force/mass))

print(accelerationCalc(10, 7))
