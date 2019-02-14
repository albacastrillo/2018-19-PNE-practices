def fibonacci():
    d = int(input())
    c = 1
    while c < n:
        print(c, end = ',')
        c, d = d, c + d
    print()
number = in(input("Introduce a number: "))

fibonacci(number)