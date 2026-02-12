import re

keywords = {'int', 'float', 'if', 'else', 'while', 'return'}
operators = {'+', '-', '*', '/', '=', '==', '<', '>'}
delimiters = {';', ',', '(', ')', '{', '}'}

def lexical_analyzer(code):
    tokens = []
    words = re.findall(r'\w+|==|[+\-*/=;(),{}<>]', code)

    for word in words:
        if word in keywords:
            tokens.append(("KEYWORD", word))
        elif word in operators:
            tokens.append(("OPERATOR", word))
        elif word in delimiters:
            tokens.append(("DELIMITER", word))
        elif word.isdigit():
            tokens.append(("NUMBER", word))
        else:
            tokens.append(("IDENTIFIER", word))

    return tokens


code = input("Enter source code: ")

tokens = lexical_analyzer(code)

print("\nTokens:")
for token in tokens:
    print(token)
