def count_bases(seq):
    """Count the number of bases of the sequence "seq" and introduce it into a dictionary
    """
    dict_bases = {}
    bases = ['A', 'C', 'T', 'G']

    for key in bases:
        dict_bases[key] = seq.count(key)

    return dict_bases


seq = input("Please, introduce a sequence: ")
dict_bases = count_bases(seq)


for key in dict_bases:

    print("Base:", key)
    print("   Counter:", dict_bases[key])

    if len(seq) > 0:
        percentage = round(100.0 * dict_bases[key] / len(seq), 1)
    else:
        percentage = 0

    print("   Percentage: ", percentage)


