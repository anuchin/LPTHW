def print_two(*args):
    arg1,arg2 =args
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_two_again(arg1, arg2):
    print(f"arg1:{arg1}, arg2:{arg2}")

def print_one(arg1):
    print(f"arg1:{arg1}")

def print_none():
    print("I gont nothing")

print_two("ZED","secret")
print_two_again("sell","see" )
print_one("one")
print_none()
