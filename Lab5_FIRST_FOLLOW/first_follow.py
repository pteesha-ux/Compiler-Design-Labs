# Grammar representation
grammar = {
    "E": ["TR"],
    "R": ["+TR", "ε"],
    "T": ["FY"],
    "Y": ["*FY", "ε"],
    "F": ["(E)", "id"]
}

FIRST = {}
FOLLOW = {}

# Function to compute FIRST
def first(symbol):
    if symbol not in grammar:
        return {symbol}

    result = set()
    for production in grammar[symbol]:
        if production == "ε":
            result.add("ε")
        else:
            result |= first(production[0])
    return result


# Initialize FIRST
for non_terminal in grammar:
    FIRST[non_terminal] = first(non_terminal)


# Initialize FOLLOW
for non_terminal in grammar:
    FOLLOW[non_terminal] = set()

FOLLOW["E"].add("$")  # Start symbol


# Simplified FOLLOW computation
for non_terminal in grammar:
    for production in grammar[non_terminal]:
        for i in range(len(production)):
            if production[i] in grammar:
                if i + 1 < len(production):
                    FOLLOW[production[i]].update(first(production[i+1]) - {"ε"})
                else:
                    FOLLOW[production[i]].update(FOLLOW[non_terminal])


print("FIRST Sets:\n")
for k, v in FIRST.items():
    print(f"FIRST({k}) = {v}")

print("\nFOLLOW Sets:\n")
for k, v in FOLLOW.items():
    print(f"FOLLOW({k}) = {v}")
