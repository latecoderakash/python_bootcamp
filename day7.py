#hangman Game
import random
words_list = ["Akash","Swapnil","Anurag","Shreya"]
random_word = random.choice(words_list)
print(random_word)
placeholder = ""
word_length = len(random_word)
for position in range(word_length):
    placeholder = placeholder + "_"
print(placeholder)
letter_selected = input("Guess a letter: ").lower()
# print(letter_selected)
display = ""
for i in random_word:
    if letter_selected == i:
        display = display + letter_selected
    else:
        display = display + "_"
print(display)

