def add(a,b):
    print(f"adding {a} +{b}")
    return a+b

def sub(a,b):
    print(f"subtracting {a} +{b}")
    return a-b

def mul(a,b):
    print(f"multi {a}+{b}")
    return a*b

num1 = int(input("1"))
num2 = int(input("2"))

t=mul(2,sub(100,add(num1,num2)))
print(t)
