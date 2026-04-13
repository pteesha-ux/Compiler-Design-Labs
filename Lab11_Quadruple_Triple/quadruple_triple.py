# Intermediate Code Generation
# Quadruple, Triple and Indirect Triple Representation

expression = "a=b+c*d"

print("Input Expression:", expression)


# Step 1: Convert expression manually into Three Address Code
print("\nThree Address Code:")

print("t1 = c * d")
print("t2 = b + t1")
print("a = t2")


# Step 2: Quadruple Representation
print("\nQuadruple Representation:")

quadruple = [
    ("*", "c", "d", "t1"),
    ("+", "b", "t1", "t2"),
    ("=", "t2", "-", "a")
]

for q in quadruple:
    print(q)


# Step 3: Triple Representation
print("\nTriple Representation:")

triple = [
    ("*", "c", "d"),
    ("+", "b", "(0)"),
    ("=", "(1)", "a")
]

for index, t in enumerate(triple):
    print(index, t)


# Step 4: Indirect Triple Representation
print("\nIndirect Triple Representation:")

pointer_table = [0, 1, 2]

print("Pointer Table:", pointer_table)

for index in pointer_table:
    print(index, triple[index])
