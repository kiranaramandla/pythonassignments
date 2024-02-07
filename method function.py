#append():     Adds an element at the end of the list
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)

a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)
print(a)

a = ["apple", "banana", "cherry"]
b = ["1", "2", "3"]
a.append(b)
print(a)

#clear():       Remove all the elements from the list
a = ["apple", "banana", "cherry"]
a.clear()
print(a)


#copy():       Returns a copy of the list
fruits = ["apple", "banana", "cherry"]
x = fruits.copy()
print(x)

#extend():      Add the elements of a list to the end of the current list

fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)

fruits = ['apple', 'banana', 'cherry']
numbers = (1 ,2 ,3, 4 ,5)
fruits.extend(numbers)
print(fruits)

#index():   Returns the index of the first elements with the specified values

fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
print(x)


fruits = [4, 5, 6, 7, 9, 10]
x = fruits.index(10)
print(x)

#insert():    Adds an elements at the specified position

fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
print(fruits)

fruits = ['apple', 'banana', 'cherry']
fruits.insert(3,"mango")
print(fruits)

#pop():        Removes the elements at the specified position

fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
print(fruits)

fruits = ['apple', 'banana', 'cherry'] # not  specified any value  default value is -1 which remove the last item
x = fruits.pop()
print(x)

#remove():        Removes the item with the specified value

fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")
print(fruits)

#Reverse():        Reverser the order of the list

fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)


# sort():        sorts the list

cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)






