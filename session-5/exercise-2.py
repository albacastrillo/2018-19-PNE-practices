def count_bases(seq):
    """Count the number of bases of the sequence "seq" and introduce it into a dictionary
    """
    dict_bases = {}
    bases = ['A', 'C', 'T', 'G']

    for key in bases:
        dict_bases[key] = seq.count(key)

    return dict_bases


seq1 = input("Enter the sequence 1: ")
seq2 = input("Enter the sequence 2: ")
sequences = [seq1, seq2]
#dict_bases = count_bases(seq)
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
