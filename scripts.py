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
