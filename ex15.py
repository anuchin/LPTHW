#imports argv
from sys import argv

#get the script name and the file to be opened
script, filename = argv

#open text file
txt = open(filename)

#print the content
print(f"Here's your {filename}:")
print(txt.read())

print("Type the filename again")
file_again = input(">")

txt_again = open(file_again)

print(txt_again.read())
