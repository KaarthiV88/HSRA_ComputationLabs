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

#Lab 1Ac: 
print("Lab1 Part1C: ")

two_n_1 = np.zeros((10), dtype= int)
for i in range(0, len(two_n_1)):
    two_n_1[i] = 2**i
print(two_n_1)

two_n_2 = np.empty(0, int)
for i in range(0, 10):
    two_n_2 = np.append(two_n_2, 2**i)
print(two_n_2)

three_n = []
for i in range(0, 9):
    three_n.append(3**i)
    
print(three_n)
for i in range(0, len(three_n)):
    three_n[i] = 3**i - 2**i
    
print(three_n)

array_1 = np.array([1,2])
array_2 = np.array([3, 4])

list_1 = [1,2]
list_2 = [3,4]

print(np.sum(array_1) + np.sum(array_2))
print(np.sum(list_1) + np.sum(list_2))

vector = [5.3, 6.2, 9.5]
print(np.linalg.norm(vector))

def vectorFinder(arr):
    x = np.linalg.norm(arr)
    y = 0
    for i in range(0, len(arr)):
        y += (arr[i]/x)
    
    return "Normal Vector: " + str(x) + "\nUnit Vector: " + str(y)

print(vectorFinder([12, -3, -4]))
print(vectorFinder([5.3, 6.2, 9.5]))