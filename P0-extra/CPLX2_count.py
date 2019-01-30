f = open('Gene')
sequence = f.read()
num_A = 0
num_C = 0
num_T = 0
num_G = 0
i = 0
while i < len(sequence):
    base = sequence[i]
    if base == '>':
        i += (sequence[i:].find('\n'))
    elif base == "A":
        num_A += 1
        i += 1
    elif base == "C":
        num_C += 1
        i += 1
    elif base == "T":
        num_T += 1
        i += 1
    elif base == "G":
        num_G += 1
        i += 1
    else:
        i += 1

print("A:", num_A)
print("C:", num_C)
print("T:", num_T)
print("G:", num_G)