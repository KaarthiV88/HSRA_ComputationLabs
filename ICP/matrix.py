import random
matrix1 = [[i*j for i in range(10000)] for j in range(10000)]
total = 0
for x in range(0,len(matrix1)):
    for y in range(0, len(matrix1[x])):
        matrix1[x][y] = random.randint(1, 25)

print("matrix1 is: ", matrix1)

for r in range(0, len(matrix1)):
    for c in range(0, len(matrix1)):
        total += matrix1[r][c]
        
print(str(total))