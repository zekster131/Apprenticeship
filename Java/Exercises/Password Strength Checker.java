# Make a class

# Logic that checks a pasword and returns a rating (very weak, weak, medium, strong, very strong) - check against common passwords and if it matches it should be weak
# Object to call a method that checks the password (object will pass through the password)

# class Students:
#   def __init__(self, first, last, age):
#     self.first = first
#     self.last = last
#     self.age = age
#     self.full = first + ' ' + last

# student1 = Students('John', 'Doe', 20)
# student2 = Students('Jane', 'Doe', 21)

# print(student1.age)
# print(student2.first)
# print(student2.full)

# Make a class

# Logic that checks a pasword and returns a rating (very weak, weak, medium, strong, very strong) - check against common passwords and if it matches it should be weak
# Object to call a method that checks the password (object will pass through the password)

class PasswordChecker:
  def __init__(self):
    self.common_passwords = ["password", "123456", "qwerty", "admin", "password123"]

  def check_password(self, password):
    if password in self.common_passwords:
      return "very weak"
    elif len(password) < 8:
      return "weak"
    elif len(password) >= 8 and any(char.isdigit() for char in password) and any(char.isupper() for char in password) and any(char.islower() for char in password):
      return "strong"
    else:
      return "medium"
