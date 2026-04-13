# Lab 10 – Intermediate Code Generation (Prefix and Postfix)

## AIM
To convert an infix expression into postfix and prefix expressions.

## THEORY
Infix notation places operators between operands.
Postfix notation places operators after operands.
Prefix notation places operators before operands.

Stack is used to handle operator precedence and parentheses during conversion.

## ALGORITHM
1. Scan infix expression from left to right.
2. If operand, add to output.
3. If operator, push to stack based on precedence.
4. Handle parentheses separately.
5. Reverse expression for prefix conversion and reuse postfix logic.

## OUTPUT
Program converts given infix expression into postfix and prefix forms.

## CONCLUSION
Prefix and postfix expressions were generated successfully.
