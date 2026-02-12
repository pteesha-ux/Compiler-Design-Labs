# Lab 2 – Conversion of Regular Expression to NFA (Thompson Construction)

## AIM
To implement Thompson Construction algorithm to convert a given Regular Expression into an equivalent Non-deterministic Finite Automaton (NFA).

## THEORY
Regular expressions are used to represent patterns in formal languages.
Thompson Construction is a method used to convert a regular expression into an equivalent NFA.

It handles the following operators:
1. Symbol (a, b, etc.)
2. Concatenation (ab)
3. Union (a|b)
4. Kleene Star (a*)

The constructed NFA uses epsilon (ε) transitions.

## ALGORITHM
1. If the input is a single symbol, create two states and connect them with that symbol.
2. If the operator is concatenation, connect the end state of first NFA to start of second using ε transition.
3. If the operator is union (|), create a new start and end state with ε transitions to both NFAs.
4. If the operator is Kleene star (*), create loop transitions using ε.
5. Print all transitions of the constructed NFA.

## SAMPLE INPUT
a|b

## SAMPLE OUTPUT
(State transitions displayed in terminal – refer screenshot)

## CONCLUSION
The regular expression was successfully converted into an equivalent NFA using Thompson Construction.
