#Pablo Perez
#1770045

A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
F = int(input())

returnv = ""


for x in range(-10, 11):
    for y in range(-10, 11):
        if ((A*x) + (B*y - C) == 0) and ((D*x) + (E*y) - F == 0):
            returnv = str(x) + " " + str(y)

if returnv == "":
    returnv = "No solution"
print(returnv)

