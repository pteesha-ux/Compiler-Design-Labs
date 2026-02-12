# LL(1) Parsing Table for given grammar

grammar = {
    "E": {"id": "TR", "(": "TR"},
    "R": {"+": "+TR", ")": "ε", "$": "ε"},
    "T": {"id": "FY", "(": "FY"},
    "Y": {"*": "*FY", "+": "ε", ")": "ε", "$": "ε"},
    "F": {"id": "id", "(": "(E)"}
}

print("Predictive Parsing Table:\n")

for non_terminal in grammar:
    for terminal in grammar[non_terminal]:
        print(f"M[{non_terminal}, {terminal}] = {grammar[non_terminal][terminal]}")
