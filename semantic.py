from ast_nodes import *

class SemanticError(Exception):
    pass

class SemanticAnalyzer:
    def __init__(self):
        self.symbols = {}
        self.loop_depth = 0

    def analyze(self, node):

        if isinstance(node, Number):
            return 'int'

        if isinstance(node, String):
            return 'string'

        if isinstance(node, Variable):
            if node.name not in self.symbols:
                raise SemanticError(f"Variable '{node.name}' used before assignment")
            return self.symbols[node.name]

        if isinstance(node, Assign):
            t = self.analyze(node.value)
            self.symbols[node.name] = t
            return t

        if isinstance(node, Read):
            # type unknown at read-time; may be int or string at runtime
            self.symbols[node.name] = 'unknown'

        if isinstance(node, Print):
            self.analyze(node.value)

        if isinstance(node, BinOp):
            l = self.analyze(node.left)
            r = self.analyze(node.right)

            # allow string concatenation like Python
            if node.op == 'PLUS':
                if l == 'string' or r == 'string':
                    return 'string'
                if l == 'int' and r == 'int':
                    return 'int'
                if l == 'unknown' or r == 'unknown':
                    return 'string'
                raise SemanticError("Invalid operands for +")

            # other operators require integers
            if l == 'int' and r == 'int':
                return 'int'

            raise SemanticError("Type mismatch in expression")

        if isinstance(node, Condition):
            self.analyze(node.left)
            self.analyze(node.right)

        if isinstance(node, If):
            self.analyze(node.condition)
            for s in node.body:
                self.analyze(s)

        if isinstance(node, IfElse):
            self.analyze(node.condition)
            for s in node.if_body:
                self.analyze(s)
            for s in node.else_body:
                self.analyze(s)

        if isinstance(node, While):
            self.loop_depth += 1
            self.analyze(node.condition)
            for s in node.body:
                self.analyze(s)
            self.loop_depth -= 1

        if isinstance(node, Break):
            if self.loop_depth == 0:
                raise SemanticError("break used outside loop")

        if isinstance(node, Continue):
            if self.loop_depth == 0:
                raise SemanticError("continue used outside loop")