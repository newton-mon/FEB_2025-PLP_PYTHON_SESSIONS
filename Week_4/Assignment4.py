'''File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.
Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.'''

fl= open('ass4.txt', 'r')
fl2= open('ass42','w')

for info in fl:
    fl2.write(info)

