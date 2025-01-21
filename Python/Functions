def greet(first_name, last_name, age):
  print(f'{first_name} {last_name} is {age}')

greet('Zeki', 'Gurler', 18)

# *args
# If we don't how how many arguments will be passed through
# Tuple of args is received

def make_pizza(size, *toppings):
  print(f'You ordered a {size}-inch pizza with the following toppings:')
  for topping in toppings:
    print(f'{topping}, ')

make_pizza(12, 'pepperoni', 'mushrooms', 'onions')

# Keyword args
# Order doesn't matter when callin with keyword args (dictionaries)
# Sends args as key-value pairs

def fruit_list(fruit1, fruit2, fruit3):
  print(f'My 1st fav is {fruit1}')
  print(f'My 2nd fav is {fruit2}')
  print(f'My 3rd fav is {fruit3}')

fruit_list(fruit3='apple', fruit1='banana', fruit2='orange')

# **kwargs

def fav_food(**food):
  print('Your fav food is', food["dessert"], 'not', food['meal'])

fav_food(meal='breakfast', dessert='ice cream')

# *args and **kwargs

def combine(*args, **kwargs):
  print('Arguments: ', args)
  print('Keyword arguments ', kwargs)

combine(2, c=3, a=5, b=10)

# Introduced 3.8
# Before the / must be positional args
# After can be keywords but not enforced
# * would enforce keywords after the star

def example(a, b, /, *, c, d):
  print(f'a = {a}, b = {b}, c = {c}, d = {d}')

example('air','bending', c='chakra', d='destiny')


def maths_function(a, b, /, operation="add", *, decimal_place=4):
  if operation == "add":
    result = a + b
  elif operation == "subtract":
    result = a - b
  else:
    raise ValueError("Invalid Operation")
  return round(result, decimal_place)

print(maths_function(10, 15))
print(maths_function(10, 15, operation='subtract'))
print(maths_function(10, 15, operation='subtract', decimal_place=6))

# Lambda argument: expression (iterable)

# add_lamba = lambda x, y: x + y
# print(add_lamba(2, 12))

numbers = [1, 2, 3, 4]

squared = map(lambda x: x**2, numbers)

print(list(squared))
