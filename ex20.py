from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count,f):
    print(line_count,f.readline())

current_file = open(input_file)

print_all(current_file)

print("rewinding")
rewind(current_file)

print("print 3 lines:")

for current_line in range(1,4):
    print_a_line(current_line,current_file)
