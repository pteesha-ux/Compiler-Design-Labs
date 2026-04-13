# Experiment 7 – Shift Reduce Parsing

## AIM
To implement Shift Reduce Parsing technique for a given grammar using stack operations.

## THEORY
Shift Reduce Parsing is a bottom-up parsing technique used in compiler design.
It uses a stack to process input symbols and applies grammar productions to reduce them step-by-step until the start symbol is obtained.

The parser performs two main operations:
1. SHIFT – Push input symbols onto the stack.
2. REDUCE – Replace symbols on the stack using grammar rules.

Parsing continues until the input string is completely processed and the start symbol remains on the stack.

## GRAMMAR USED
E → E + E  
E → E * E  
E → id

## INPUT STRING
id + id * id

## ALGORITHM
1. Initialize the stack as empty.
2. Read the input string and append end marker ($).
3. Shift symbols from input onto the stack.
4. Apply reduction rules whenever possible.
5. Repeat SHIFT and REDUCE operations until only the start symbol remains.
6. Accept the string if parsing is successful.

## OUTPUT
The program displays stack contents, remaining input, and parsing actions (SHIFT / REDUCE / ACCEPT) step-by-step.

## RESULT
The shift reduce parser was successfully implemented and verified for the given input string.
