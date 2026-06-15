# if else statment

# print("Welcome to the rollercoster!")
# height = int(input("What is your height in cm? "))
# if height > 120:
#     print("Welcome to the drive")
# else:
#     print("Sorry you need to be tall!")


# check odd or even

# number = float(input("Enter the number you want to check ? "))
# if number % 2 == 0:
#     print("Entered number is even")
# else:
#     print("Entered number is odd")

#pizza delivery(nested if / else /elif)

# print("Welcome to Python Pizza Delivery")
# size = str(input("Which size pizza do you want? S, M or L? "))
# pepperoni = str(input("Do you want pepperoni on your pizza ? Y or N: "))
# cheese= str(input("Do you want extra cheeese? Y or N: "))
# bill = 0
# if size == "S":
#     bill = 15
#     if pepperoni == "Y":
#         bill = bill + 2
#         if cheese == "Y":
#             bill = bill + 1
#     print(f"You have to pay:${bill}")      
# elif size == "M":
#     bill = 20
#     if pepperoni == "Y":
#         bill = bill + 3
#         if cheese == "Y":
#             bill = bill + 1
#     print(f"You have to pay:${bill}")  
# elif size == "L":
#     bill = 25
#     if pepperoni == "Y":
#         bill = bill + 3
#         if cheese == "Y":
#             bill = bill + 1
#     print(f"You have to pay:${bill}")  


# Treasure Island Project
print("Welcome to the Traeaure Island \nYour mission is to find the treasure")
left_or_right = input("Do you want to go left or right? ")
if left_or_right == "left":
    swim_or_wait= input("You want to swim or wait? ")
    if swim_or_wait == "wait":
        door = input("Which door ? Red, Blue or Yellow ")
    else:
        print("Game Over.")
    if (door == "Red" or door == "Blue"):
        print("Game Over")
    else:
        print("You won!")
else:
    print("Game Over.")

