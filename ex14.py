from sys import argv

script, user_name, =argv
prompt ='>'

print(f"Hi {user_name} , I' the {script} script")
print("IF like to ask few questios")
print(f"Do you like my bame")
likes = input(prompt)

print(f"Where do u live?")
lives = input(prompt)

print("Waht kind of com ?")
computer = input(prompt)

print(f"""Alright , so u {likes}, u live in {lives},
        Not sure where it is And u have {computer}""")
