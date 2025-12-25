# 🧠 Mini Compiler Project (Custom Programming Language)

A Python-based mini compiler that implements core compiler design concepts including **lexical analysis, parsing, semantic analysis, and interpretation**.  
The project supports a custom programming language with control flow, runtime input, and Python-like string handling.

---

## 🚀 Features

- Custom programming language
- File-based and interactive program input
- Lexer, Parser, AST, Semantic Analyzer, Interpreter
- Runtime user input (`read`)
- Conditional statements (`if`, `else`)
- Loops (`while`)
- Loop control (`break`, `continue`)
- Python-like string + integer concatenation
- Compile-time semantic error detection

---

## 🏗️ Compiler Pipeline

Source Code
   ↓
Lexical Analysis (Lexer)
   ↓
Syntax Analysis (Parser & AST)
   ↓
Semantic Analysis
   ↓
Interpreter (Execution)

⸻

##📁 Project Structure

mini_compiler/
├── lexer.py           # Tokenizes source code
├── parser.py          # Parses tokens and builds AST
├── ast_nodes.py       # AST node definitions
├── semantic.py        # Semantic analysis and type checking
├── interpreter.py    # Executes the program
├── main.py            # Compiler driver
├── program.txt        # User program (auto-generated)
└── README.md          # Project documentation

##▶️ How to Run

Requirements
	•	Python 3.11 or above

Run the Compiler
python main.py

Enter Program Code (User Input)

The user types the program directly in the terminal.

Example:
read n
i = 1

while i <= n
    print "Value: " + i
    i = i + 1
end

Finish input:
	•	Mac/Linux: Ctrl + D
	•	Windows: Ctrl + Z then Enter

⸻

⌨️ Runtime Input
Enter value for n: 4

⸻

📤 Output
Value: 1
Value: 2
Value: 3
Value: 4

⸻

##🛡️ Semantic Checks
	•	Variable used before assignment
	•	Type mismatch in expressions
	•	Invalid break or continue usage
	•	Errors detected before execution

⸻

##🎓 Academic & Interview Value

This project demonstrates strong understanding of:
	•	Compiler design fundamentals
	•	Abstract Syntax Tree based execution
	•	Semantic validation
	•	Control-flow implementation
	•	Separation of compile-time and runtime errors

Resume line example:

Developed a custom programming language compiler in Python implementing lexical analysis, parsing, semantic analysis, and interpretation.

⸻
