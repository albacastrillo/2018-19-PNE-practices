# Example of reading a file located in our local filesystem

NAME = "mynotes.txt"

# Open the file
myfile = open(NAME, 'r')

# myfile is an object

print("File opened: {}".format(myfile.name))

contents = myfile.read()

print("The file contents are: {}".format(contents))

myfile.close()

f = open(NAME, 'a')
f.write("This is a text example for adding to my file")
f.close()




