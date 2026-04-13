# Three Address Code Generator

operators = ['+', '-', '*', '/']


def generate_TAC(expression):

    temp_count = 1
    tac = []

    expr = expression.replace(" ", "")

    lhs, rhs = expr.split('=')

    while any(op in rhs for op in operators):

        for op in operators[::-1]:  # Higher precedence first
            if op in rhs:

                index = rhs.find(op)

                left = rhs[index - 1]
                right = rhs[index + 1]

                temp = "t" + str(temp_count)

                tac.append(f"{temp} = {left} {op} {right}")

                rhs = rhs[:index - 1] + temp + rhs[index + 2:]

                temp_count += 1

                break

    tac.append(f"{lhs} = {rhs}")

    return tac


expression = input("Enter expression: ")

result = generate_TAC(expression)

print("\nThree Address Code:\n")

for line in result:
    print(line)
