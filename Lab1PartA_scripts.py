import math
import numpy as np

#Lab 1:

#1Aa:
print("Lab1 Part1A: ")

def count_to_n(n):
    if(n == 3):
        return (str(1) + "\n" + str(2) + "\n" + str(3))

    elif(n == 2):
        return(str(1) + "\n" + str(2))

    else:
        return(str(1))

print(count_to_n(1))
print(count_to_n(2))
print(count_to_n(3))
print("")

def count_to_n_for(n):
    stringer = ""
    for i in range(1, n+1):
        stringer += (str(i) + "\n")

    return stringer

def count_to_n_while(n):
    i = 1
    stringer = ""
    while(i <= n):
        stringer += (str(i) + "\n")
        i += 1

    return stringer

print(count_to_n_for(2))
print(count_to_n_for(10))

print(count_to_n_while(2))
print(count_to_n_while(10))

def sumDivi():
    count = 0
    for i in range(0, 200):
        if(i%2 == 0 and i%7 == 0):
            count += i

    return count

print(sumDivi())
print("")

#Lab 1Ab:
print("Lab1 Part1B: ")
intlist3 = [0,1, 2, 3]
intlist9 = []
for i in range (0,10):
    intlist9.append(i)

two_n = []
for i in range (0,10):
    two_n.append(2**i)

print(two_n)
print(two_n[7])

matrix = [[3,4], [5,6]]
print(matrix[1])
print(matrix[0][0])
print("")
