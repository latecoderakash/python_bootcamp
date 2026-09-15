def reverse_string(text):

    output = ""

    for n in range(len(text) - 1, -1, -1):
        output = output + text[n]

    print(output)

reverse_string("hello")
