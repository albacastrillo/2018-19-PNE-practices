def sumN(n):
    total_sum = 0
    for i in range(n):
        total_sum = total_sum + i + 1

    return total_sum

#main program
num = int(input("Please introduce a number"))
total = sumN(num)
print("The total sum is {}".format(total))

#if we press f8 it wont go back to the function. Instead, we have to press F7. We dont want to repeat this process 100times so we press la flechita hacia abajo and it prints everithing till the end.
