# DataDSL

A simple domain-specific language (DSL) for data manipulation operations. The language provides a clean syntax for common data operations like loading, filtering, selecting, and sorting data.

## Features

- Load data from CSV files
- Filter data based on conditions
- Select specific columns
- Sort data in ascending or descending order

## Example

```dsl
load "users.csv"
filter age > 30
select name, age
sort age desc
```

## Components

- `tokenizer.py`: Lexical analysis to break down DSL code into tokens
- `parser.py`: Parses tokens into an abstract syntax tree
- `compiler.py`: Compiles the AST into executable Python code
- `main.py`: Main entry point that processes DSL files

## Usage

1. Write your data manipulation operations in a `.dsl` file
2. Run `python main.py` to compile and execute the DSL code 