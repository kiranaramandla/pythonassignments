
t=(10,20,30,40)
print(len(t))

#unpacking a tuple:

fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#packing a tuple:

a=1
b=2
c=3
d=a,b,c
print(d)


#tuple comprehensive:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "an" in x:
    newlist.append(x)
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if " " in x:
    newlist.append(x)
print(newlist)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "" in x:
    newlist.append(x)
print(newlist)


l=(x*x for x in range(10) if x%2==1)
print(l)
for i in l :
 print(i)


s={10,20,30,40,40,50,60,60,70,100,100}   #duplicates not alloweld
print(s)

#add():

list = {"apple", "banana", "cherry"}   #add item last position
list.add("orange")
print(list)


list = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
list.update(tropical)
print(list)

# copy():

fruits = {"apple", "banana", "cherry"}
x = fruits.copy()
print(x)

f1 = {"apple", "banana", "cherry"}
f2={"mango","papaya","pineapple"}
f3=f1.copy()
f4=f2.copy()
x = f3.copy()
y=f4.copy()
print(x)
print(y)


#pop():
fruits = {"apple", "banana", "cherry"}
print(fruits.pop())
print(fruits.pop())
print(fruits.pop())
#print(fruits.pop())   #error pop is an empty set

#remove():

fruits = {"apple", "banana", "cherry"}
fruits.remove("banana") 
print(fruits)

fruits = {"apple", "banana", "cherry"}
#fruits.remove("")     #key error beacuse no one selection
print(fruits)

ruits = {"apple", "banana", "cherry"}
#fruits.remove("pineapple")  # pineapple not in list
print(fruits)

#discard:
list= {"apple", "banana", "cherry"}
list.discard("banana")
print(list)

list= {"apple", "banana", "cherry"}
list.discard("bat")   #This method is different from the remove() method, because the remove()
print(list)             #   method will raise an error if the specified item does not exist,
                        #     and the discard() method will not.


#clear():

list = {"apple", "banana", "cherry"}   # clear all the data
list.clear()
print(list)












