def parse(tokens):

    ast = []
    for line in tokens:
        cmd = line[0]
        args = line[1:]
        ast.append((cmd.lower(), args))

    return ast
