def fibonacci(n):
    c, d = 0, 1
    while c < n:
        print(c, end = ',')
        c, d = d, c+d
    print()
fibonacci(int(input("Introduce a number: ")))