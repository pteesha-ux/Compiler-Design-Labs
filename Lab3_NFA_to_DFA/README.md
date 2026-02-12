# Lab 3 – Conversion of NFA to DFA (Subset Construction)

## AIM
To convert a Non-deterministic Finite Automaton (NFA) into an equivalent Deterministic Finite Automaton (DFA) using Subset Construction algorithm.

## THEORY
Subset Construction algorithm converts NFA into DFA by:
1. Treating each DFA state as a set of NFA states.
2. Computing epsilon-closure of states.
3. Repeating transitions for each symbol in the alphabet.
4. Creating new DFA states for new subsets.

## ALGORITHM
1. Compute epsilon-closure of start state.
2. For each input symbol, compute move and closure.
3. Add new subsets as DFA states.
4. Repeat until no new states are generated.

## OUTPUT
(Refer screenshot)

## CONCLUSION
The NFA was successfully converted into an equivalent DFA using Subset Construction.
