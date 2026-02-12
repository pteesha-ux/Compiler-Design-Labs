AIM:
To eliminate left recursion from a given grammar.

ALGORITHM:
1. Separate productions into alpha and beta.
2. Alpha contains left recursive productions.
3. Beta contains non-left recursive productions.
4. Rewrite grammar as:
   A → βA'
   A' → αA' | ε

SAMPLE INPUT:
A -> Aa | b

OUTPUT:
A -> bA'
A' -> aA' | ε

CONCLUSION:
Left recursion was successfully removed from the grammar.
