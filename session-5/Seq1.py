class Seq:
    """A class for representing sequences"""

    # A method always starts with self
    # Every time we create a new object __init__ method will be called
    # Attribute: what is inside the function init
    # The rest of the functions under init are the methods

    def __init__(self, strbases):
        print("New empty sequence created!")

        self.strbases = strbases

    def len(self):
        return len(self.strbases)


class Gene(Seq):
    """This class is derived from Seq class
    All the objects of class Gene will inheritate the methods from Seq class"""
    pass


# Objects
# What is inside the class Seq, is also inside s2 and the sequence is stored inside strbases

s1 = Gene("ATTCGATCC")
s2 = Seq("AAAGG")

str1 = s1.strbases
str2 = s2.strbases

l1 = s1.len()
l2 = s2.len()

print("Sequence 1: {}".format(str1))
print("     Length: {}".format(l1))
print("Sequence 2: {}".format(str2))
print("     Length: {}".format(l2))
print("The end")
