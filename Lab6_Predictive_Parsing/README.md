# Lab 6 – Predictive Parsing Table

## AIM
To construct LL(1) Predictive Parsing Table for a given grammar.

## THEORY
Predictive parsing table is used in LL(1) parsing.
It is constructed using FIRST and FOLLOW sets.

For production A → α:
1. For each terminal in FIRST(α), add A → α to table.
2. If ε ∈ FIRST(α), add A → α to FOLLOW(A) entries.

## OUTPUT
(Refer screenshot)

## CONCLUSION
Predictive parsing table was successfully constructed for the given grammar.
