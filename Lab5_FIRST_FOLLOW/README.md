# Lab 5 – FIRST and FOLLOW Computation

## AIM
To compute FIRST and FOLLOW sets for a given grammar.

## THEORY
FIRST set contains all terminals that can appear at the beginning of strings derived from a non-terminal.
FOLLOW set contains terminals that can appear immediately to the right of a non-terminal.

## ALGORITHM
1. If symbol is terminal → FIRST is symbol itself.
2. If production contains ε → include ε.
3. FOLLOW of start symbol includes $.
4. For each production A → αBβ:
   - Add FIRST(β) to FOLLOW(B).
   - If β is empty, add FOLLOW(A).

## OUTPUT
(Refer screenshot)

## CONCLUSION
FIRST and FOLLOW sets were successfully computed for the given grammar.
