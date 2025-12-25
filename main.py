from lexer import tokenize
from parser import Parser
from interpreter import Interpreter
from semantic import SemanticAnalyzer, SemanticError

print("Type your program below.")
print("Press Ctrl+D (Mac/Linux) or Ctrl+Z + Enter (Windows) to finish.\n")

# 1️⃣ Take program input from USER (terminal)
lines = []
try:
    while True:
        line = input()
        lines.append(line)
except EOFError:
    pass

# 2️⃣ Save user code into program.txt
with open("program.txt", "w") as f:
    f.write("\n".join(lines))

print("\nProgram saved to program.txt")
print("Executing...\n")

# 3️⃣ Read program.txt and compile
with open("program.txt") as f:
    code = f.read()

tokens = tokenize(code)
ast = Parser(tokens).parse()

# 4️⃣ Semantic Analysis
analyzer = SemanticAnalyzer()
try:
    for stmt in ast:
        analyzer.analyze(stmt)
except SemanticError as e:
    print("Semantic Error:", e)
    exit(1)

# 5️⃣ Execute
interp = Interpreter()
for stmt in ast:
    interp.eval(stmt)