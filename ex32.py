the_count= [1,2,3,4,5]
fruits=['apples','oranges','pears','mango']
change=[1,'pennies',2,'dimes',3,'quarters']

for number  in the_count:
    print(f"this is the number {number}")

for fruit in fruits:
    print(f"the fruit is {fruit}")

for i in change:
    print(f"I got {i}")

elements=[]

for i in range(0,6):
    print(f"adding {i} to the list")
    elements.append(i)

for i in elements:
    print(f"Element was {i}")
