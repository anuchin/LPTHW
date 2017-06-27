from sys import argv

script, filename =argv

print(f" Now we are to erase {filename}\n")
print("If u dont want that press ztrl +c otherwise enter")

input("?")

print(f"opening the {filename}")
target = open(filename,'r+')

# print("Truncateing the filename")
# target.truncate()

print("Now input 3 lines")

line1=input("Line1")
line2=input("Line2")
line3=input("Line3")

contents = line1+'\n'+line2+'\n'+line3+'\n'

print("Now writing these lines\n")

target.write(contents)
# target.write("\n")
# target.write(line2,)
# target.write("\n")
# target.write(line3,)
# target.write("\n")

print("prionting content")

print(target.read())

print(f"Now closing {filename}")
target.close()
