# Lab 9 – Computation of LR(0) Items

## AIM
To construct canonical collection of LR(0) items using closure and goto functions.

## THEORY
LR(0) parsing is a bottom-up parsing technique.
It constructs parsing states using closure and goto operations.

Closure adds productions when dot appears before a non-terminal.
Goto moves dot over grammar symbols to generate new states.

These states form the canonical LR(0) collection.

## ALGORITHM
1. Start with augmented grammar.
2. Compute closure of initial item.
3. Apply goto for each grammar symbol.
4. Repeat until no new states appear.
5. Print canonical LR(0) item sets.

## OUTPUT
Program prints canonical LR(0) item sets in terminal.

## CONCLUSION
Canonical collection of LR(0) items constructed successfully.
