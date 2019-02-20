from Seq import Seq

seq1 = Seq("ATTCGATCC")
seq2 = Seq("AAAGG")
seq3 = Seq(seq1.complement())
seq4 = Seq(seq3.reverse())

seq_list = [seq1, seq2, seq3, seq4]
counter = 1
bases = ['A', 'C', 'T', 'G']

for seq in seq_list:
    print("Sequence", counter, ": {}".format(seq))
    print("     Length: {}".format(seq.len()))

    for base in bases:
        print("     Bases count: {}".format(seq.count(base)))
        print("     Bases percentage: {}".format(seq.perc(base)))
    counter += 1

