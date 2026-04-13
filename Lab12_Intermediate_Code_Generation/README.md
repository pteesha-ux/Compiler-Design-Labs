# Lab 12 – Intermediate Code Generation (Three Address Code)

## AIM
To generate Three Address Code (TAC) for a given arithmetic expression.

## THEORY
Intermediate Code Generation is a compiler phase that converts source code into machine-independent representation.

Three Address Code uses temporary variables and simple instructions of the form:

x = y op z

This representation simplifies optimization and final code generation.

## ALGORITHM
1. Read input expression.
2. Identify operators based on precedence.
3. Generate temporary variables for intermediate steps.
4. Replace processed expressions step-by-step.
5. Print final Three Address Code.

## OUTPUT
Program generates Three Address Code for the given expression.

## CONCLUSION
Three Address Code was successfully generated.
