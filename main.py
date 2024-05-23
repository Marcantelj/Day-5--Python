import random

# lists of letters, numbers, and symbols to pull from.
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# inputs for what they user wants.
print("Welcome to the PyPassword Generator!")
amountletters= int(input("How many letters would you like in your password?\n")) 
amountsymbols = int(input(f"How many symbols would you like?\n"))
amountnumbers = int(input(f"How many numbers would you like?\n"))

# password list that will be generated.
password = []

# generates and randomises letters then adds it to a password.
for letter in range(0, amountletters):
  password += letters[random.randint(0, 51)]
# generates and randomises numbers then adds it to a password.
for number in range(0, amountnumbers):
  password += numbers[random.randint(0, 9)]
# generates and randomises symbols then adds it to a password.
for symbol in range(0, amountsymbols):
  password += symbols[random.randint(0, 8)]
  
newpassword = ""

# shuffles all letters, numbers, and symbols in the password list
random.shuffle(password)

# appends list to a newpassword to be printed to the user
for char in password: 
  newpassword += char

print(f"Here is your generated password: {newpassword}")