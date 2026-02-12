# Lab 1 – Implementation of Lexical Analyzer

## AIM
To implement a Lexical Analyzer that identifies tokens such as keywords, identifiers, operators, numbers, and delimiters from given source code.

## THEORY
A lexical analyzer is the first phase of a compiler. 
It reads the source code and converts it into a sequence of tokens.
Each token represents a meaningful element of the language.

## ALGORITHM
1. Define keywords, operators, and delimiters.
2. Read source code as input.
3. Use regular expressions to split the input into words.
4. Check each word against token categories.
5. Print the identified tokens.

## SAMPLE INPUT
int a = 10;

## OUTPUT
(KEYWORD, int)
(IDENTIFIER, a)
(OPERATOR, =)
(NUMBER, 10)
(DELIMITER, ;)

## CONCLUSION
The lexical analyzer successfully identified different tokens from the given source code.
