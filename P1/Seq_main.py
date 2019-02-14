from Seq import Seq

seq1 = Seq("ATTCGATCC")
seq2 = Seq("AAAGG")
seq3 = seq1.complement()
seq4 = seq3.reverse().strbase

seq_list = [seq1, seq2, seq3, seq4]
counter = 1

for seq in seq_list:
    print("Sequence", counter, ": {}".format(seq))
    print("     Length: {}".format(seq.len()))
    bases = ['A', 'C', 'T', 'G']
    for base in bases:
        print("     Bases count: {}".format(seq.count(base)))
        print("     Bases percentage: {}".format(seq.perc(base)))
    counter += 1

