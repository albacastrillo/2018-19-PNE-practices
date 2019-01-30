def lenth_seq():
    sequence = input("Introduce a sequence of DNA")
    sequence = sequence.upper()
    num_total = 0
    num_A = 0
    num_C = 0
    num_T = 0
    num_G = 0
    for i in sequence:
        num_total += 1
        if i == "A":
            num_A += 1
        elif i == "C":
            num_C += 1
        elif i == "T":
            num_T += 1
        elif i == "G":
            num_G += 1

    print("Total lenth:", num_total)
    print("A:", num_A)
    print("C:", num_C)
    print("T:", num_T)
    print("G:", num_G)

lenth_seq()



