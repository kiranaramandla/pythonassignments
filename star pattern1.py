n=int(input("enter value:"))

for i in range(n):
    for j in range (i+1):
        print("*",end=" ")
    print()

n=int(input("enter value:"))
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print("*", end=" ")
    print()
    

n=int(input("enter value:"))
for i in range(5,0,-1):
    for j in range (5,i,-1):
        print(" ",end=" ")
    for k in range (1,i+1):
        print("*",end=" ")
    print()

n=int(input("enter value:"))
for i in range(5,0,-1):
    for j in range (5,i,-1):
        print(" ",end=" ")
    for k in range (1,i+1):
        print("*",end=" ")
    print()

n=int(input("enter value:"))
for i in range(1,6):
    for j in range (5,i,-1):
        print(" ",end=" ")
    for k in range (1,i+1):
        print("*",end=" ")
    print()