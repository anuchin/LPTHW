print("praticing \' marks")
print("\ttabs \n newline")

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("-------")
print(poem)
print("-------")

five=10-2+3-6
print(f"This shoulf be five{five}")

def secret_formula(started):
    jelly_beans= started*500
    jars= jelly_beans/1000
    crates = jars/100
    return jelly_beans,jars,crates

start_point= 10000
beans, jars, crates= secret_formula(start_point)

print("with start {}".format(start_point))

print(f"Wed ghave{beans} beans, {jars} jars, nad {crates} crates")

start_point = start_point/10

print(" WE can do this wat")
formula= secret_formula(start_point)

print("We'd ahve {} beans, {} jars, and {} crates".format(*formula))
