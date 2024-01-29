n=int(input("enter number of rows needed:"))
for i in range(n):
    print(" "*(n-i-1),end=" ")
    print("* "*(i+1))

