def count_consonants(text):
    counter = 0
    for n in text:
        if n != "a" and n != "e" and n != "i" and n != "o" and n != "u":
            counter = counter + 1
    print(counter)

count_consonants("hello")