#!/usr/bin/env python

# Below is a blank canvas to start your assignments
import numpy as np
import math
#Lab0:

#2A:

print("Part 2A: ")
print("Hello, my name is Kaarthi V.")
print("")

#2B: 
print("2B: ")
my_name = "Kaarthi"
my_age = 16
pi = 3.14
longhorns_rule = True
print("my_name ", my_name, type(my_name))
print("my_age ", my_age, type(my_age))
print("pi ", pi, type(pi))
print("longhorns_rule ", longhorns_rule, type(longhorns_rule))
pi = 3.14159
print("The pi variable has been changed to a more specific number with more decimal points: ", pi)
print("")

#2C:
print("2C: ")
print("Python Interactive Mode: Interactive mdoe is a command line shell which gives immediate feedback for each statement, while running previosuly fed statements in active memory. As new lines are fed into the interpreter, the fed program is evaluated both in part and in whole. This has helped me with its immediate feedback to test little parts of Python I was doubtful about without messing it up in the main script.")
print("")
year = 2023
yearDiff = 2028 - year
print("Age in 2028: ", (my_age + yearDiff), "2028 is ", yearDiff, " years from now, so add that to 'my_age' variable")

yearDiff = year - 2010
print("age in 2010: ", (my_age - yearDiff), "2010 was ", yearDiff, " years ago, so subtract that from 'my_age' variable")
print("")

print((1+2)*(3+4))
print((7+3)**2*(2+3))
print(2/3*4/5)
print("")

print(pi*12**2)
print("")

print("My name is " + my_name + ".")
print("")

print(my_age % 2)

KE = 0.5*5*2**2
PE = 5*9.8*5
print("Total Energy = ", (KE + PE))


#2D: 
print("2D: ")
my_age = float(my_age)
print(my_age)
print("You can tell the difference between and Integer and a Float by using the 'type()' function, or by printing it and seeing if there are decimals at the end of it.")
print(math.sqrt(36))
print((math.exp(3) + math.exp(-2)))
total_energy = 0
PE = 0.5
KE = 0.5*10*(math.pow(5, 2))
total_energy = PE + KE
print(total_energy)
print("")

#2E: 
print("2E: ")

def print_hello():
    return "Hello!"

print(print_hello())

def print_age(age):
    return "I am " + str(age) + " years old"

print(print_age(my_age))

def compute_kinetic_energy(mass, velocity):
    kinetic_energy = 0.5*mass*(math.pow(velocity, 2))
    return kinetic_energy

print(compute_kinetic_energy(10, 10))

def energy(mass, velocity, height):
    kinetic_energy = 0.5*mass*(math.pow(velocity, 2))
    potential_energy = mass*9.8*height
    total_energy = kinetic_energy + potential_energy
    return str(kinetic_energy) + ", " + str(potential_energy) + ", " + str(total_energy)

print(energy(5, 3, 10))
print("")

#2F;
print("2F: ")

if(my_age == 25):
    print(True)
else:
    print(False)

num1 = compute_kinetic_energy(5, 10)
num2 = compute_kinetic_energy(3, 11)
if(num1 <= num2):
    print(True)
else:
    print(False)

def greater_than_5(x):
    if(x > 5 and x%2 == 0):
        return True
    else:
        return False

print(greater_than_5(6))
print("")

#2G: 
print("2G: ")

def even_or_odd(num):
    if(num%2 == 0):
        return str(num) + " is EVEN"
    else:
        return str(num) + " is ODD"

print(even_or_odd(10))
print(even_or_odd(11))

def is_sideC_5(a, b):
    c = math.sqrt(((a**2)+(b**2)))
    if(c == 5):
        return "Side C is equal to 5"
    elif(c > 5):
        return "Side C is greater than 5"
    else:
        return "Side C is less than 5"

print(is_sideC_5(3, 4))
print(is_sideC_5(1, 2))

def morse_potential_energy(De, Re, R):
    a = 5
    morse = (1-2.71828**(-a*(R-Re)))**2*De
    return morse

print(morse_potential_energy(10, 4, 5))
print("")
#_______________________________________________________________________________________________________________________________________________________________________________________________________________________________________






