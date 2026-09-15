def count_vowels(text):
    counter = 0
    for n in text:
        if n == "a":
            counter = counter + 1
        elif n == "e":
            counter = counter + 1
        elif n == "i":
            counter = counter + 1
        elif n == "o":
            counter = counter + 1
        elif n == "u":
            counter = counter + 1
        # elif n == "a":
        #     counter = counter + 1
    print(counter)

count_vowels("hello")