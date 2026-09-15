def count_character(text, character):
    counter = 0
    for n in text:
        if n == character:
            counter = counter + 1
    print(counter)
count_character("tomato", "t")