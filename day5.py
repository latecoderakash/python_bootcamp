#Loops

# for loop

# fruits = ["a", "b", "c"]
# for fruit in fruits:
#     print(fruit)

#Highest Score
# scores = [78, 92, 45, 100, 67, 83, 59, 71, 88, 34]
# highest = 0
# for score in scores:
#     if score > highest:
#         highest = score
# print(highest)


#range function
# for number in range(1,10,3):
#     print(number)

# add numbers
# total = 0
# for number in range(1,101):
#     total = total + number
# print(total)

#fizz buzz
# for number in range(1,16):
#     if (number % 3 == 0 and number % 5 == 0):
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)


# password generator
import random

letters = ['A','B','C','D','E','F','G','H','I','J',
           'a','b','c','d','e','f','g','h','i','j']

symbols = ['!', '@', '#', '$', '%', '&', '*']

numbers = [1,2,3,4,5,6,7,8,9]

print("Welcome to the PyPassword Generator")

letter_input = int(input("How many letters would you like in your password?\n"))
symbol_input = int(input("How many symbols would you like?\n"))
numbers_input = int(input("How many numbers would you like?\n"))

password_list = []

for l in range(letter_input):
    random_letter = random.choice(letters)
    password_list.append(random_letter)

for s in range(symbol_input):
    random_symbol = random.choice(symbols)
    password_list.append(random_symbol)

for n in range(numbers_input):
    random_number = str(random.choice(numbers))
    password_list.append(random_number)

random.shuffle(password_list)

final_password = "".join(password_list)

print(final_password)
    

    

