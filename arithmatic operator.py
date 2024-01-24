a=10
b=20
# arithmatic operator
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

#comparision operator
print(a==10)
print(a<=10)
print(a<10)
print(a>10)
print(a>=10)
print(a!=10)
print((a+1)==11)
print((a+1)!=10)

a,b=5,6
#and operator
print(a<6 and b==6)
print(a>4 and b<=6)
print(a<=6 and b!=6)
print(a>=5 and b>=5)
print(a!=5 and b>6)
#or operator
print(a<6 or b==6)
print(a>4 or b<=6)
print(a<=6 or b!=6)
print(a>=5 or b>=5)
print(a!=5 or b>6)
#not operator
print(not(a<6 or b==6))
print(not(a>4 or b<=6))
print(not(a<=6 or b!=6))
print(not(a>=5 or b>=5))
print(not(a!=5 or b>6))
#bitwise operator
a=12
b=6
print(a&b)
print(a|b)
print(a^b)
print(~(a&b))
print(a<<2)
print(a>>3)