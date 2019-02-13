def count_bases(seq):
    """Count the number of bases of the sequence "seq" and introduce it into a dictionary
    """
    dict_bases = {}
    bases = ['A', 'C', 'T', 'G']

    for key in bases:
        dict_bases[key] = seq.count(key)

    return dict_bases