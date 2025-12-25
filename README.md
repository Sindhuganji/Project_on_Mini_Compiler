Mini Compiler Project (Custom Programming Language)

This project implements a Python-based mini compiler for a custom-designed programming language. It demonstrates core compiler design concepts including lexical analysis, parsing, semantic analysis, and interpretation. The compiler supports control flow, runtime user input, and Python-like string handling.

⸻

FEATURES

• Custom programming language
• Interactive program input from user
• Lexer, Parser, AST, Semantic Analyzer, Interpreter
• Runtime user input using read
• Conditional statements: if, else
• Loops using while
• Loop control statements: break, continue
• Python-like string and integer concatenation
• Semantic error detection before execution

⸻

COMPILER PIPELINE

Source Code
→ Lexical Analysis (Lexer)
→ Syntax Analysis (Parser & AST)
→ Semantic Analysis
→ Interpretation / Execution

⸻

PROJECT STRUCTURE

mini_compiler
lexer.py – Tokenizes source code
parser.py – Parses tokens and builds AST
ast_nodes.py – AST node definitions
semantic.py – Semantic analysis and type checking
interpreter.py – Executes the program
main.py – Compiler driver
program.txt – User program (auto-generated)
README – Project documentation

⸻

HOW TO RUN

Requirements
Python 3.11 or above

Run the compiler
python main.py

The user types the program directly in the terminal.
After typing the program, finish input using:
Mac/Linux – Ctrl + D
Windows – Ctrl + Z then Enter

⸻

SAMPLE PROGRAM

read n
i = 1

while i <= n
print “Value: “ + i
i = i + 1
end

⸻

RUNTIME INPUT

Enter value for n: 4

⸻

OUTPUT

Value: 1
Value: 2
Value: 3
Value: 4

⸻

EXAMPLE PROGRAMS

If-Else Example

read age
if age >= 18
print “Adult”
else
print “Minor”
end

Break Example

i = 1
while i <= 10
if i == 5
break
end
print i
i = i + 1
end

⸻

SEMANTIC CHECKS

• Variable used before assignment
• Type mismatch in expressions
• Invalid break or continue usage
• Errors detected before execution

⸻

ACADEMIC AND INTERVIEW VALUE

This project demonstrates strong understanding of compiler design principles, including AST-based execution, semantic validation, control-flow implementation, and separation of compile-time and runtime errors.

⸻

AUTHOR

Pushpa Sri Sindhu
B.Tech – Computer Science
SRM AP University

⸻

LICENSE

This project is created for educational and academic purposes only.
