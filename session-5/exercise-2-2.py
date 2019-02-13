from Bases import count_bases
seq1 = input("Enter the sequence 1: ")
seq2 = input("Enter the sequence 2: ")
sequences = [seq1, seq2]
num = 0

for a in sequences:
    dict_bases = count_bases(a)
    num += 1
    print("Sequence {} is {} bases in length".format(num, len(a)))

    for key in dict_bases:
        print("Base:", key)
        print("   Counter:", dict_bases[key])

        if len(a) > 0:
            percentage = round(100.0 * dict_bases[key] / len(a), 1)
        else:
            percentage = 0

        print("   Percentage: ", percentage)
