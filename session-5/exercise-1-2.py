from Bases import count_bases
seq = input("Introduce a sequence: ")
dict_bases = count_bases(seq)
print("This sequence is {} bases in length.".format(len(seq)))
for key in dict_bases:

    print("Base:", key)
    print("   Counter:", dict_bases[key])

    if len(seq) > 0:
        percentage = round(100.0 * dict_bases[key] / len(seq), 1)
    else:
        percentage = 0

    print("   Percentage: ", percentage)


