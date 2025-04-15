# DataDSL

A compiler/interpreter for a domain-specific language (DSL) focused on data manipulation. This project demonstrates the implementation of a complete compiler pipeline, from lexical analysis to code generation.

## Compiler Pipeline

1. **Lexical Analysis** (`tokenizer.py`)
   - Breaks down source code into tokens
   - Handles string literals and whitespace

2. **Parsing** (`parser.py`)
   - Converts tokens into an Abstract Syntax Tree (AST)
   - Validates syntax and structure

3. **Code Generation** (`compiler.py`)
   - Transforms AST into executable Python code
   - Uses pandas for efficient data operations

## Language Features

The DSL provides a clean syntax for common data operations:
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

This compiles to Python code that uses pandas for efficient data processing.

## Technical Details

The compiler pipeline:
1. Tokenizes the input into a stream of tokens
2. Parses the tokens into an AST representing the operations
3. Generates optimized pandas code from the AST
4. Executes the generated code

## Usage

1. Write your data manipulation operations in a `.dsl` file
2. Run `python main.py` to compile and execute the DSL code

## Project Structure

- `tokenizer.py`: Lexical analyzer (scanner)
- `parser.py`: Syntax analyzer and AST generator
- `compiler.py`: Code generator targeting pandas
- `main.py`: Driver program that orchestrates the compilation process
