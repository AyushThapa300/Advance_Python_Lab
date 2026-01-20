#Class-2 Simple function

def greet(name):
    return f"Hello, {name}!"  

# Calling the function to test it
print(greet("Alice"))  

def Greet(name="World"):
    return f"Hello, {name}!"

print(Greet())

#Function using keyqord Arguements
def introduce(first_name, last_name):
    return f"My name is {first_name} {last_name}."

print(introduce(last_name="Thapa Magar", first_name="Ayush"))

#arbitrary arguments
def fruits(*args):
    return "I like " + ", ".join(args) + "."
print(fruits("apple", "banana", "cherry"))

#kwargs
def details(**kwargs):
    info = ", ".join(f"{key}: {value}" for key, value in kwargs.items())
    return f"Details - {info}"
print(details(name="Alice", age=30, city="New York"))

#function within function
def outer_function(msg):    
    def inner_function():
        return f"Inner says: {msg}"
    return inner_function()
print(outer_function("Hello from the outer function!"))

#pass by reference
def modify_list(lst):
    lst.append(4)
    return lst
my_list = [1, 2, 3]
print(modify_list(my_list))

#pass by value
def modify_number(num):
    num = 10
my_number = 5
print(modify_number(my_number))

def modify_number(num):
    num = 10
    return num
my_number = 5
print(modify_number(my_number))

#Recursive function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))  

#Lambda function
square = lambda x: x * x
print(f"Square : {square(6)}")

#Function to find maximum numbers
def find_max(num1,num2):
    return num1 if num1>num2 else num2

print("Maximum number is : ")
print(find_max(19,20))

#function to find length of a word
def find_length(name):
    return len(name)
print("Length of your name is : ")
print(find_length("Ayush Thapa Magar"))

#Slice
list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
sliced_list = list1[2:9:2]
print("Sliced List is : ")
print(sliced_list)

#append
list2 = [1, 2, 3]
list2.append(4)
print("List after append is : ")
print(list2)

#count
list3 = [1, 2, 2, 3, 4, 2]
count_of_2 = list3.count(2)
print("Count of 2 in list3 is : ")
print(count_of_2)

#copy
list4 = [5, 6, 7]  
copied_list = list4.copy()
print("Copied List is : ")
print(copied_list)

#extend
list5 = [1, 2, 3]
list5.extend([4, 5, 6])
print("Extended List is : ")
print(list5)

#insert
list6 = [1, 2, 4, 5]
list6.insert(2, 13)
print("List after insert is : ")
print(list6)

#remove
list7 = [1, 2, 3, 4, 5]
list7.remove(3)
print("List after remove is : ")
print(list7)

#reverse
list8 = [1, 2, 3, 4, 5]
list8.reverse()
print("Reversed List is : ")
print(list8)

#sort
list9 = [5, 2, 9, 1, 5, 6]
list9.sort()
print("Sorted List is : ")
print(list9)

#tuples
tuple1 = (1, 2, 3, 4, 5)
print("Tuple is : ")
print(tuple1)

#concatination of tuples
tuple2 = (6, 7, 8)
concatenated_tuple = tuple1 + tuple2
print("Concatenated Tuple is : ")
print(concatenated_tuple)

#slicing of tuples
sliced_tuple = tuple("ZOOMING")
print("Sliced Tuple is : ")
print(sliced_tuple[1:])
print(sliced_tuple[::-1])
print(sliced_tuple[2:5])

#enumerate
list10 = ['a', 'b', 'c', 'd']
for index, value in enumerate(list10):
    print(f"Index: {index}, Value: {value}")

#filter
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers are : ")
print(even_numbers)

#dictionary
dict1 = {"name": "Alice", "age": 30, "city": "New York"}
print("Dictionary is : ")
print(dict1)

#adding items to dictionary
dict1["profession"] = "Engineer"   
print("Dictionary after adding profession is : ")
print(dict1)

#removing items from dictionary
del dict1["age"]
print("Dictionary after removing age is : ")
print(dict1)

#accessing items from dictionary
print("Name from dictionary is : ")
print(dict1["name"])

#looping through dictionary
print("Looping through dictionary : ")
for key, value in dict1.items():
    print(f"{key}: {value}")

#dictionary methods
keys = dict1.keys()
print("Keys in dictionary are : ")
print(keys)

values = dict1.values()
print("values in dictionary are : ")
print(values)