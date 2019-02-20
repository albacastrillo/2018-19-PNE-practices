class Seq:
    """Class for representing sequences"""

    def __init__(self, strbase):

        self.strbase = strbase

    def len(self):
        """Returns the length of the sequence"""

        return len(self.strbase)

    def complement(self):
        """Returns a new sequence that is the complement of the object's sequence"""

        list_complement = []

        for base in self.strbase:
            if base == 'A':
                list_complement.append('T')
            elif base == 'C':
                list_complement.append('G')
            elif base == 'T':
                list_complement.append('A')
            elif base == 'G':
                list_complement.append('C')

        seq_complement = ''.join(list_complement)

        return seq_complement

    def reverse(self):
        """Returns a new sequence that is the reverse of the current sequence"""

        seq_reverse = self.strbase[::-1]

        return seq_reverse

    def count(self, base):
        """Returns the number of times the base "base" appears in the sequence"""

        counter = self.strbase.count(base)

        return counter


    def perc(self, base):
        """Returns the percentage of the base "base" over the total bases"""

        if len(self.strbase) > 0:
            percent = round(100.0 * self.strbase.count(base) / len(self.strbase), 1)
        else:
            percent = 0

        return percent
