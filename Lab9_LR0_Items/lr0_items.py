# LR(0) Items Construction (Closure + GOTO)

grammar = {
    "S'": ["S"],
    "S": ["CC"],
    "C": ["cC", "d"]
}

def closure(items):
    closure_set = set(items)

    while True:
        new_items = set()

        for item in closure_set:
            lhs, rhs = item.split("->")
            dot_pos = rhs.find(".")

            if dot_pos < len(rhs) - 1:
                symbol = rhs[dot_pos + 1]

                if symbol in grammar:
                    for production in grammar[symbol]:
                        new_item = symbol + "->." + production
                        new_items.add(new_item)

        if new_items.issubset(closure_set):
            break

        closure_set.update(new_items)

    return closure_set


def goto(items, symbol):
    moved_items = set()

    for item in items:
        lhs, rhs = item.split("->")
        dot_pos = rhs.find(".")

        if dot_pos < len(rhs) - 1 and rhs[dot_pos + 1] == symbol:
            moved_rhs = rhs[:dot_pos] + symbol + "." + rhs[dot_pos + 2:]
            moved_items.add(lhs + "->" + moved_rhs)

    return closure(moved_items)


def canonical_collection():
    start_item = closure({"S'->.S"})
    states = [start_item]
    transitions = []

    symbols = set()
    for lhs in grammar:
        symbols.add(lhs)
        for prod in grammar[lhs]:
            symbols.update(prod)

    while True:
        new_states = []

        for state in states:
            for symbol in symbols:
                next_state = goto(state, symbol)

                if next_state and next_state not in states:
                    new_states.append(next_state)
                    transitions.append((state, symbol, next_state))

        if not new_states:
            break

        states.extend(new_states)

    return states


states = canonical_collection()

print("Canonical Collection of LR(0) Items:\n")

for i, state in enumerate(states):
    print(f"I{i}:")
    for item in state:
        print(" ", item)
    print()
