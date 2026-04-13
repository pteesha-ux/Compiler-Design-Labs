# Lab 11 – Quadruple, Triple and Indirect Triple Representation

## AIM
To generate intermediate code using Quadruple, Triple and Indirect Triple representations.

## THEORY
Intermediate code is generated between source code and machine code.

Quadruple format:
(op, arg1, arg2, result)

Triple format:
(op, arg1, arg2) with position reference

Indirect Triple format:
Uses pointer table referencing triple entries.

These representations help optimize code before final machine code generation.

## ALGORITHM
1. Convert expression into Three Address Code.
2. Represent operations using Quadruple format.
3. Represent operations using Triple format.
4. Use pointer table for Indirect Triple representation.

## OUTPUT
Program displays Quadruple, Triple and Indirect Triple representations.

## CONCLUSION
Intermediate code representations were generated successfully.
