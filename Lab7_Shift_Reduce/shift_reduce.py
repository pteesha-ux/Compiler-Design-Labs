# Shift Reduce Parser Implementation

# Grammar:
# E -> E+E
# E -> E*E
# E -> id

input_string = list("id+id*id$")
stack = []

print("Stack\t\tInput\t\tAction")

while True:

    # ACCEPT condition
    if stack == ["E"] and input_string == ["$"]:
        print(stack, input_string, "ACCEPT")
        break

    # REDUCE: E -> id
    if len(stack) >= 2 and stack[-2:] == ["i", "d"]:
        stack = stack[:-2]
        stack.append("E")
        print(stack, input_string, "REDUCE E->id")
        continue

    # REDUCE: E -> E+E
    if len(stack) >= 3 and stack[-3:] == ["E", "+", "E"]:
        stack = stack[:-3]
        stack.append("E")
        print(stack, input_string, "REDUCE E->E+E")
        continue

    # REDUCE: E -> E*E
    if len(stack) >= 3 and stack[-3:] == ["E", "*", "E"]:
        stack = stack[:-3]
        stack.append("E")
        print(stack, input_string, "REDUCE E->E*E")
        continue

    # SHIFT operation
    if len(input_string) > 0:
        stack.append(input_string.pop(0))
        print(stack, input_string, "SHIFT")
        continue

    print("Parsing Error")
    break
