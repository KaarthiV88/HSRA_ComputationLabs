import math
import numpy as np

#Part A: Damped Molecular Dynamics

def forceReturn(pos):
    Flj = 4*1*(-12*(1/pos)**13 + 6 * (1/pos)**7)
    return Flj

print(forceReturn(0.3))

def accelerationCalc(force):
    acceleration = force/1
    return acceleration

print(accelerationCalc(10))


def moveCalc(velocity, acc):
    delta_t = 0.01
    velocity = (acc * delta_t)
    delta_r = velocity * delta_t + 0.5 * float(acc) * delta_t ** 2
    #delta_r = "{:.2f}".format(delta_r)
    
    return delta_r, velocity

print(moveCalc(10, 3))

    

def damper(delta_r, velocity):
    threshold = 0.1
    if(delta_r > threshold):
        threshold = delta_r
        velocity = 0
    
    else:
        velocity = 0.9*velocity
        
    return delta_r, velocity
        
def updater_r(r, delta_r):
    r = r + delta_r
    return r

def get_force(r):
    force = r
    return force

print("__________________________________________")
#___________________________________________________________________________________________________________________________________________________
r = 0.3
velocity = 0
delta_r = 0
acceleration = 0
force = 100
get_delta_r_v = 0
damp_delta_r_v = 0  

while(abs(force) > 0.01):
    force = get_force(force)
    #print(force)
    acceleration = accelerationCalc(force)
    #print(acceleration)
    x = moveCalc(velocity, acceleration)
    velocity = x[1]
    delta_r = x[0]
    #print(velocity)
    #print(delta_r)
    #print(damper(delta_r, velocity))
    r = updater_r(r, delta_r)
    #print(r)
    #print(force)
    force = forceReturn(r)
    #print(force)
    
    print("r = " + str(r) + "\nForce = " + str(force))

