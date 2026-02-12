# Proper Thompson Construction for:
# concatenation (.)
# union (|)
# Kleene star (*)

class State:
    def __init__(self):
        self.transitions = {}

    def add_transition(self, symbol, state):
        if symbol not in self.transitions:
            self.transitions[symbol] = []
        self.transitions[symbol].append(state)


class NFA:
    def __init__(self, start, end):
        self.start = start
        self.end = end


state_count = 0

def new_state():
    global state_count
    state_count += 1
    return State()


# Symbol NFA
def symbol_nfa(symbol):
    start = new_state()
    end = new_state()
    start.add_transition(symbol, end)
    return NFA(start, end)


# Concatenation
def concatenate(nfa1, nfa2):
    nfa1.end.add_transition('ε', nfa2.start)
    return NFA(nfa1.start, nfa2.end)


# Union
def union(nfa1, nfa2):
    start = new_state()
    end = new_state()

    start.add_transition('ε', nfa1.start)
    start.add_transition('ε', nfa2.start)

    nfa1.end.add_transition('ε', end)
    nfa2.end.add_transition('ε', end)

    return NFA(start, end)


# Kleene Star
def kleene_star(nfa):
    start = new_state()
    end = new_state()

    start.add_transition('ε', nfa.start)
    start.add_transition('ε', end)

    nfa.end.add_transition('ε', nfa.start)
    nfa.end.add_transition('ε', end)

    return NFA(start, end)


# Simple regex parser (supports a|b, ab, a*)
def build_nfa(regex):
    stack = []

    i = 0
    while i < len(regex):
        if regex[i].isalpha():
            stack.append(symbol_nfa(regex[i]))

        elif regex[i] == '*':
            nfa = stack.pop()
            stack.append(kleene_star(nfa))

        elif regex[i] == '|':
            nfa1 = stack.pop()
            i += 1
            nfa2 = symbol_nfa(regex[i])
            stack.append(union(nfa1, nfa2))

        i += 1

    while len(stack) > 1:
        nfa2 = stack.pop()
        nfa1 = stack.pop()
        stack.append(concatenate(nfa1, nfa2))

    return stack.pop()


# Print NFA transitions
def print_nfa(nfa):
    visited = set()
    stack = [nfa.start]

    print("\nNFA Transitions:\n")

    while stack:
        state = stack.pop()
        if state in visited:
            continue
        visited.add(state)

        for symbol in state.transitions:
            for next_state in state.transitions[symbol]:
                print(f"{id(state)} --{symbol}--> {id(next_state)}")
                stack.append(next_state)


# Main
regex = input("Enter Regular Expression: ")
nfa = build_nfa(regex)
print_nfa(nfa)
