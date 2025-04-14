import re


def tokenize(code):
    """
    Lexical analysis: decompose the input code into tokens that can be used by the parser
    """
    tokens = []
    for line in code.strip().splitlines():
        parts = re.findall(r'"[^"]*"|\S+', line)
        tokens.append(parts)
    print(f"Tokens: {tokens}")
    return tokens
