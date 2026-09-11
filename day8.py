# def greet():
#     print("Hello")
#     print("how are you")
#     print("whats your age")
# greet()

#Function with input

# def greet_with_nickname(name):
#     print(f"Hello {name}")
#     print(f"how are you {name}")
#     print(f"whats your age {name}")

# greet_with_nickname("Mohit")

# life in weeks left program
# def life_in_weeks(age):
#     remaining_year = int(90 - age)
#     remaining_week = int(52 * remaining_year)
#     print(f"You have {remaining_week} weeks left.")
# life_in_weeks(20)

#Function with more than 1 input

# def greet_with_nickname(name, Location):
#     print(f"Hello {name}")
#     print(f"how are you {name} and whats you {Location}")
#     print(f"whats your age {name}")

# greet_with_nickname("Mohit","Lucknow")

# Love calculator

# def calculate_love_score(name1, name2):
#     counter1 = 0
#     for name in [name1, name2]:
#         for letter in name:
#             if letter == "t":
#                 counter1 +=1
#             elif letter == "r":
#                 counter1 +=1 
#             elif letter == "u":
#                 counter1 +=1
#             elif letter == "e":
#                 counter1 +=1
#     print(counter1)
#     counter2 = 0
#     for name in [name1, name2]:
#         for letter in name:
#             if letter == "l":
#                 counter2 +=1
#             elif letter == "0":
#                 counter2 +=1 
#             elif letter == "v":
#                 counter2 +=1
#             elif letter == "e":
#                 counter2 +=1
#     print(counter2)
#     print(f"{counter1}{counter2}")
# calculate_love_score("Kanye West", "Kim Kardashian")

#Caesar Cipher
alphabet = [
    "a", "b", "c", "d", "e", "f", "g",
    "h", "i", "j", "k", "l", "m", "n",
    "o", "p", "q", "r", "s", "t", "u",
    "v", "w", "x", "y", "z"
]
direction = input("Type 'encode' to encryt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = input("Type the shift number:\n")
