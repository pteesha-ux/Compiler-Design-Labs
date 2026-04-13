# Infix to Postfix and Prefix Conversion using Stack

precedence = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '^': 3
}


def infix_to_postfix(expression):
    stack = []
    output = ""

    for char in expression:
        if char.isalnum():
            output += char

        elif char == '(':
            stack.append(char)

        elif char == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop()

        else:
            while (stack and stack[-1] != '(' and
                   precedence.get(char, 0) <= precedence.get(stack[-1], 0)):
                output += stack.pop()
            stack.append(char)

    while stack:
        output += stack.pop()

    return output


def infix_to_prefix(expression):
    expression = expression[::-1]

    expression = list(expression)

    for i in range(len(expression)):
        if expression[i] == '(':
            expression[i] = ')'
        elif expression[i] == ')':
            expression[i] = '('

    expression = "".join(expression)

    postfix = infix_to_postfix(expression)

    return postfix[::-1]


expr = input("Enter Infix Expression: ")

print("Postfix Expression:", infix_to_postfix(expr))
print("Prefix Expression:", infix_to_prefix(expr))
