from tokenizer import tokenize
from compiler import compile_ast
from parser import parse
from rich import print

with open("example.dsl", "r") as file:
    code = file.read()

tokens = tokenize(code)
ast = parse(tokens)
compiled_code = compile_ast(ast)


print("Compiled python code:")
print(compiled_code)
