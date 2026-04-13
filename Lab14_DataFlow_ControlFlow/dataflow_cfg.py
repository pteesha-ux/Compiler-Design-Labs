# Control Flow Graph (CFG) and Simple Data Flow Analysis

# Example program representation
program = {
    1: "a = b + c",
    2: "d = a - e",
    3: "if d > 0 goto 5",
    4: "a = d * 2",
    5: "return a"
}

# Step 1: Build CFG
cfg = {
    1: [2],
    2: [3],
    3: [4, 5],  # conditional branch
    4: [5],
    5: []
}

print("Control Flow Graph (CFG):\n")

for node in cfg:
    print(f"Statement {node} -> {cfg[node]}")


# Step 2: Data Flow Analysis (Reaching Definitions Example)

definitions = {}

for line, statement in program.items():
    if "=" in statement:
        variable = statement.split("=")[0].strip()
        definitions[line] = variable

print("\nReaching Definitions:\n")

for line in definitions:
    print(f"Definition at line {line}: variable '{definitions[line]}'")


# Step 3: Display Program

print("\nProgram Statements:\n")

for line in program:
    print(f"{line}: {program[line]}")
