import math

# Math module in python
print(math.pi)
print(math.e)
print(math.ceil(3.14))
print(math.floor(3.14))
print(math.trunc(3.14))
print(math.sin(3.14))
print(math.cos(3.14))
print(math.tan(3.14))
print(math.atan(3.14))
print(math.degrees(3.14))
print(math.radians(3.14))
print(math.factorial(2))

print("Hello World")

first_name="Supuni"
second_name="Chathurika"
full_name=first_name+" "+second_name
print(full_name)
full= f"{first_name} {second_name}"
print(full)
charactor_length=f"{len(first_name)} + {len(second_name)}"
print(charactor_length)

mom_name = " Mary "
print("your mom is",mom_name.strip())
print(mom_name.replace("M", "J"))

# Arithmatic
print(round(2.9))
print(abs(-2))

# Escape character
text = "This book is called \"Harry Potter\""
programme = "Python \nprogramme "
print(text)
print(programme)

message = """
Hi Supuni,
How are you doing?
No matter what, keep going.
Cheers!
"""
print(message)

patient_name = "John Smith"
print(patient_name)
print(patient_name.capitalize())
print(len(patient_name))
print(patient_name[0])
print(patient_name[-1])
print(patient_name[0:3])
print(patient_name[:3])
print(patient_name[:])
print(patient_name[0:])
age = 20
print(age)
is_new_patient = True
print(is_new_patient)

#Input functions
name = input("What is your name? ")
print('Hello ' + name)
age = input("What is your age? ")
print('Your age is ' + str(age))
print('Your age in number format is ' + age)

# Type conversion
# Input function always returns a string even we enter a number
# Builtin functions for converting variables --> int(), float(),str(), bool()

birth_year = input("What is your birth year? ")
age = 2025 - int(birth_year)
print('Your age is ' + str(age))

# Basic calculator exercise
first_number = input("What is your first number? This should be a decimal number. ")
second_number = input("What is your second number? ")
summation = float(first_number) + int(second_number)
print("The summation is " + str(summation))

# Another way of doing type conversion
first = float(input("What is your first number? "))
second = float(input("What is your second number? "))
sum = first + second
print("The summation is " + str(sum))
print("sum", sum)

# String methods
course = "Python for Beginners"
print("Course in upper case ", course.upper())
print("Course in lower case ", course.lower())
print("Course title ", course.title())
print("Find y in course", course.find('y'))
print("Course Y in course, Python is case sensitive ", course.find('Y'))
print("Find the word 'for' in course", course.find('for'))
print("Replace the word 'for' with '4' ", course.replace('for', '4'))
print("Check if there is any value exists", 'Python' in course, 'Java' in course)

#Arithmatic operators
print("Summation", 2+2)
print("Subtraction", 3-2)
print("Multiplication", 2*2)
print("Division", 10/3)
print("Floor Division", 10//3)
print("Modulo", 10%3)
print("Exponentiation", 2**3)

# Comparison Operators
x= 2<3
y= 2>3
z= 2==3
a=2!=3
b= 2<=3
c= 2>=3
print(x,y,z,a, b, c)

#Logical Operators
# and (both)
# or (at least one)
# not (inverse)

price = 24
price_2 = 4
print(price > 20 and price < 30)
print(price_2 > 20 or price_2 < 30)
print(not price>20)

# If statement

temperature = float(input("What is the temperature today? "))

if temperature > 30:
    print("It's a sunny and hot day")
elif temperature > 20: #(20,30]
    print("It's a nice day")
elif temperature > 10: # (10, 20]
    print("It's a bit cold day")
else: print("It's a cold day")
print("Thank you")

# Exercise

weight = float(input("Enter your weight: "))
weight_unit = input("Enter your weight unit pounds(L), kilograms(K): ")

if weight_unit.upper() == "L":
    print("Your weight in Kg is", weight * 0.45)
else:
    print("Your weight in Lb is", weight * 2.2)

#Ternary Operator

age = 22
if age >= 18:
    message = "Eligible"
else:
    message = "Not Eligible"
print(message)

message_new = "Eligible" if age >= 18 else "Not Eligible"
print(message_new)

#Chaining comparison operators
age = 10
if 18 <= age <65:
    print("You are old enough to work")
else:
    print("You can't work")

# While loop

i=0
while i<=1_000:
    print(i)
    i=i+1

# While loop exercise

i=0
j=10
while i<=10:
    print(i * "*")
    i=i+1
while j>=0:
    print(j * "*")
    j=j-1

# Lists

names = ["Supuni", "John", "Mary", "Jane", "Nick"]
print("names: ", names)
print("first element of the list: ", names[0])
print("second element of the list: ", names[1])
print("third element of the list: ", names[2], names[-3])
print("last element of the list: ", names[-1], names[4])

names[1] = "Jonathan"
print("names: ", names, names[1])
print("Range of names in the list: ", names[0:3])

# List Methods

elements = [1,2,3,4,5]
print("numbers", elements)
print("Add a new element at the end of the list: ", elements.append(10))
print("Modified elements list :", elements)
print("Insert a new element anywhere in the list: ", elements.insert(0,-1))
print("Modified elements list :", elements)
print("Insert a name in the middle if the list :", elements.insert(3, 'Supuni'))
print("Modified elements list :", elements)
print("Remove an element from the list: ", elements.remove(2))
print("Modified elements list :", elements)
print("Pop an element from the list: ", elements.pop())
print("Modified list: ", elements)
print("Clear the whole list: ", elements.clear())
print("Modified list: ", elements)
print("Check if an element exist in the list: ", 1 in elements )
print("Check if an element exists in the list: ", 10 in elements )
print("Get the number of items in the list: ", len(elements))

# For loop
elements = [1,2,3,4,5]

for item in elements:
    print('Current item is : ', item)

# Range function : Generate a sequence of numbers

print("sequential numbers from 0 to 4")
for number in range(5):
    print(number)
print("sequential numbers from 5 to 9")
for number in range(5, 10):
    print(number)
print("sequential even numbers from 4 to 10")
for number in range(4, 10, 2):
    print(number)
print("sequential odd numbers from 5 to 10")
for number in range(5, 10, 2):
    print(number)

for i in range(1, 11):
    is_successful = i % 2 == 0
    print("Attempt: " , i)
    if is_successful:
        print(f"Attempt {i} is successful")
        break
    else:
        print(f"Attempt {i} is unsuccessful")
        print("Try again")

for x in range(5):
    for y in range(3):
        print(f"({x},{y})")

# nested loops
for x in range(5):
    for y in range(3):
        print(f"({x},{y})")
        print(x* "*", y* "#")

# Tuples: Similar to list, but tuples are immutable which means we can't change tuples later
# Use case of tuple : When we don't something accidentally change in future

numbers_tuples = (1, 2, 3, 4,4,4)
print(numbers_tuples)
print(type(numbers_tuples))
print(numbers_tuples[0])
print(numbers_tuples[-1])
print(numbers_tuples.count(4))
print(numbers_tuples.index(2))

# Functions

def greet(child_name, child_name_2):
    print(f"Hi {child_name} {child_name_2} ")
    print("How are you?")


greet("Supuni", "Chathurika")
greet("Nanon", "Ohm")

# 2 types of functions
# 1. Function to perform a task
# 2. Calculate something and return a value

def get_greeting(guest_name):
    return f"Hi.. {guest_name} greeting!"

greeting_message = get_greeting("Nanon")
print(greeting_message)
file = open("greet.txt", "w")
file.write(greeting_message)

# By using keyword arguments we can make functions more readable

def increment(first_num, by):
    return first_num + by

print(increment(1, by=2))

# Default arguments

def decrement(first_num, by=1):
    return first_num - by

print(decrement(10))
print(decrement(0,4))

