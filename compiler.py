def compile_ast(ast):
    output = ["import pandas as pd"]
    for command, args in ast:
        if command == "load":
            filename = args[0].strip('"')
            output.append(f'df = pd.read_csv("{filename}")')
        elif command == "filter":
            output.append(f'df = df[df["{args[0]}"] {args[1]} {args[2]}]')
        elif command == "select":
            cols = ". ".join(f'"{col}"' for col in args)
            output.append(f'df = df[["{cols}"]]')
        elif command == "sort":
            col = args[0]
            ascending = "False" if args[1] == "desc" else "True"
            output.append(f'df = df.sort_values("{col}", ascending={ascending})')
    return "\n".join(output)
