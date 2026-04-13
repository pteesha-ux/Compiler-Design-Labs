# Lab 8 – Computation of LEADING and TRAILING

## AIM
To compute LEADING and TRAILING sets for a given grammar.

## THEORY
LEADING(A) is the set of terminals that appear at the beginning of strings derived from A.

TRAILING(A) is the set of terminals that appear at the end of strings derived from A.

These sets are useful in operator precedence parsing.

## ALGORITHM
1. If first symbol of production is terminal, add to LEADING.
2. If first symbol is non-terminal, add its LEADING set.
3. If last symbol is terminal, add to TRAILING.
4. If last symbol is non-terminal, add its TRAILING set.
5. Repeat until no change occurs.

## OUTPUT
Program prints LEADING and TRAILING sets in terminal.

## CONCLUSION
LEADING and TRAILING sets were computed successfully.
