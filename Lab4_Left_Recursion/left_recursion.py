def remove_left_recursion(non_terminal, productions):
    alpha = []
    beta = []

    for prod in productions:
        if prod.startswith(non_terminal):
            alpha.append(prod[len(non_terminal):])
        else:
            beta.append(prod)

    if not alpha:
        print("No Left Recursion Found.")
        return

    print("\nGrammar after removing Left Recursion:\n")

    # A → βA'
    print(f"{non_terminal} -> ", end="")
    for b in beta:
        print(f"{b}{non_terminal}' | ", end="")
    print()

    # A' → αA' | ε
    print(f"{non_terminal}' -> ", end="")
    for a in alpha:
        print(f"{a}{non_terminal}' | ", end="")
    print("ε")


# Example Grammar
print("Example Grammar:")
print("A -> Aa | b")

remove_left_recursion("A", ["Aa", "b"])
