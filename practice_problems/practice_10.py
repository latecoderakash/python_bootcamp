def factorial(number):
    output = 1
    for n in range(number,0,-1):
        output = output * n
    print(output)
factorial(-1)
