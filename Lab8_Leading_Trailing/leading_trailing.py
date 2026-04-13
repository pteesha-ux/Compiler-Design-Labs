# Program to compute LEADING and TRAILING of grammar

grammar = {
    "E": ["E+T", "T"],
    "T": ["T*F", "F"],
    "F": ["(E)", "id"]
}

leading = {}
trailing = {}

# Initialize sets
for non_terminal in grammar:
    leading[non_terminal] = set()
    trailing[non_terminal] = set()


# Compute LEADING
def compute_leading(symbol):
    for production in grammar[symbol]:
        if production[0].islower() or not production[0].isalpha():
            leading[symbol].add(production[0])
        else:
            leading[symbol].add(production[1])
            compute_leading(production[0])


# Compute TRAILING
def compute_trailing(symbol):
    for production in grammar[symbol]:
        if production[-1].islower() or not production[-1].isalpha():
            trailing[symbol].add(production[-1])
        else:
            trailing[symbol].add(production[-2])
            compute_trailing(production[-1])


# Run computation
for non_terminal in grammar:
    compute_leading(non_terminal)
    compute_trailing(non_terminal)


# Print results
print("LEADING sets:\n")
for k, v in leading.items():
    print("LEADING(", k, ") =", v)

print("\nTRAILING sets:\n")
for k, v in trailing.items():
    print("TRAILING(", k, ") =", v)
