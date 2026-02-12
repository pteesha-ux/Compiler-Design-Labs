# NFA to DFA using Subset Construction

from collections import defaultdict, deque

# Example NFA
nfa = {
    0: {'a': [0, 1]},
    1: {'b': [2]},
    2: {}
}

start_state = 0
accept_states = [2]
alphabet = ['a', 'b']


def epsilon_closure(states):
    # No epsilon transitions in this simplified example
    return set(states)


def move(states, symbol):
    result = set()
    for state in states:
        if symbol in nfa[state]:
            result.update(nfa[state][symbol])
    return result


def subset_construction():
    dfa_states = {}
    dfa_transitions = {}
    queue = deque()

    start_closure = frozenset(epsilon_closure([start_state]))
    dfa_states[start_closure] = 0
    queue.append(start_closure)

    state_count = 1

    while queue:
        current = queue.popleft()
        dfa_transitions[current] = {}

        for symbol in alphabet:
            next_states = epsilon_closure(move(current, symbol))
            next_states = frozenset(next_states)

            if not next_states:
                continue

            if next_states not in dfa_states:
                dfa_states[next_states] = state_count
                state_count += 1
                queue.append(next_states)

            dfa_transitions[current][symbol] = next_states

    return dfa_states, dfa_transitions


dfa_states, dfa_transitions = subset_construction()

print("DFA States:\n")
for state, number in dfa_states.items():
    print(f"D{number} = {set(state)}")

print("\nDFA Transitions:\n")
for state in dfa_transitions:
    for symbol in dfa_transitions[state]:
        print(f"{set(state)} --{symbol}--> {set(dfa_transitions[state][symbol])}")
