# Variables
name = 'Zeki'
age = 18
message = f"your name is {name}, your age is {age}"
message1 = "your name is {}, your age is {}".format(name, age)

print(message)

# Text File Output

import sys

#with open("output.txt", "w") as file:
#  sys.stdout = file
#  print("go to the file instead")


# Escape Characters

# \ take the next symbol as its literal meaning
# \n new line, \t tab, \u unicode, \U extended unicode
# \\ backslash adding a slash to string

print("Person1: \tHey how are you?\nPerson2: \tI'm good, thanks for asking! \U0001f604")

# BODMAS

# // 10//3 = 3 - floor division (how many times 3 goes into 10))
# % 10%3 = 1 - modulus (remainder)


# String Methods

print('hello world'.upper())
print('HELLO WORLD'.lower())

print('Hello World'.count('l',0))


# Collections - Storing/Structuring Data

# Lists - ordered/indexed, mutable (can be added to, removed etc), ['a', 2, etc]

# Dictionaries - unordered / not indexed, mutable (can be added to, removed etc), {key: value, 'b':3, etc}

# Tuples - ordered/indexed, immutable (can't be added to, removed etc), x = ('a', 2, etc)

# Sets - unique values, unordered / not indexed, mutable (can be added to, removed etc), {2, 'a', etc}


# Sort

my_list = ['kiwi', 'apple', 'pear', 'banana']
print(my_list)

my_list.sort() # Alphabetical, ascending
print(my_list)

my_list.sort(key=len) # Length - can be any function
print(my_list)


# Dictionaries

drinks = {'Fizzy': 'Sprite', 'Ale': 'Ruddles', 'Sweet': 'Lemonade'}

print(drinks['Fizzy'])

drinks['Alcohol'] = 'Dissarano'
print(drinks)

print(drinks.get('Alcohol'))

# Dictonaries Exercise

#Make a dictionary, 3 authors as keys, multiple books per author as values [].
#Have an input that asks for an author name and print a STRING of the books by the author. (NOT A LIST)

authors_dict = {'J.K. Rowling': ['Harry Potter', 'Fantastic Beasts and where to find them'], 'Leigh Bargudo': ['Six of Crows', 'Shadow and Bone'], 'M.G. Harris': ['The Joshua Files', 'Black Horizon']}

#author_name = input('Enter an author name: ')

#author_books = authors_dict.get(author_name)

#print(', '.join(author_books or ['Author not found']))

# Conditional Statements

#If

is_admin = False
is_verified = False
on_holiday = False
if (is_admin or is_verified) and not on_holiday:
  print(f"Welcome, {name}")
else:
  print("Sorry, you don't have permissions.")

# Elif

temp = 8

if temp >=30:
  print('Very Hot')
elif temp >=20:
  print('Warm')
elif temp >=10:
  print('Cool')
elif temp == 0:
  print('Its freezing')
else:
  print('Its meh')

# Statements Exercise

# User inputs a mark/grade
# Over 80 print disctinction
# Over 60 print pass
# Else fail

#marks = int(input('Enter your marks: '))

#if marks >=80:
  #print('Distinction')
#elif marks >=60:
  #print('Pass')
#else:
  #print('Fail')


# Multiple Comparators

deposit = 99
password = "password123"
 
if 0 < deposit < 100 and password == "password123":
  print("Thank you for your deposit of {deposit}")
else:
  print("Failed ")

# In and not in

name = "root123"

if name in ('root', 'admin', 'user'):
  print("Invalid Username")
else:
  print("Accepted.")

if name not in ('root', 'admin', 'user'):
  print('Accepted.')
else:
  print('Invalid Username')

# Exercise

# Weight converter app
# User to input weight
# Input for kgs or lbs
# If statement to check the unit, convert the value and print

lbs_or_kgs = ''

#while lbs_or_kgs not in ('KGS', 'LBS', 'LB', 'KG', 'POUNDS', 'KILOGRAMS'):
  #lbs_or_kgs = input('Do you want to convert to lbs or kgs ? ')
  #lbs_or_kgs = lbs_or_kgs.upper()

#weight = int(input('Enter a weight: '))

#if lbs_or_kgs in ('LBS', 'LB', 'POUNDS'):
  #weight = weight/2.2
  #print(f'The weight you entered equals {weight} kgs')
#elif lbs_or_kgs in ('KGS', 'KG', 'KILOGRAMS'):
  #weight = weight*2.2
  #print(f'The weight you entered equals {weight} lbs')

# Highest Number with tuple


num = 10
num1 = 20
print((num, num1)[num < num1])


# Iteration

j = 0

while j < 6:
  j += 1
  if j ==3:
    continue # does the next iteration
  print(j)

# For Loops

my_fruit_list = ['apple', 'banana', 'cherry']

#for fruit in my_fruit_list:
  #print(fruit)

la = 0

while la < len(my_fruit_list):
  print(my_fruit_list[1])
  la +=1

for i in range(1,5): # 1-4
  print(i)


# Square and even numbers 

x = 3
numbers = [1,2,3,4,5,6,7,8,9,10]

even_squared_number = [number ** x for number in numbers if number % 2 == 0]

print(even_squared_number)


# Exercise
# Write a loop that takes in 5 names and prints 'name is cool'
# While loop
# For loop
# List comp
# Optional: one line list comp

names = []

# while len(names) < 5:
#   name = input('Enter a name: ')
#   names.append(name)
#   print(f'{name} is cool')

# for i in range(5):
#   name = input('Enter a name: ')
#   names.append(name)
#   print(f'{name} is cool')

# List Comp

new_names = [print(f'{name} is cool') for name in [input('Enter a name: ') for i in range(5)]]

print(new_names)
