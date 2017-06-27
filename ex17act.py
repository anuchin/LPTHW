from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")



out_file = open(to_file,'w').write(in_file.read(open(from_file)))


print("done")
