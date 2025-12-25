from ast_nodes import *

# Control flow signals
class BreakSignal(Exception):
    pass

class ContinueSignal(Exception):
    pass


class Interpreter:
    def __init__(self):
        self.env = {}   # symbol table (runtime values)

    def eval(self, node):

        # ---------- LITERALS ----------
        if isinstance(node, Number):
            return node.value

        if isinstance(node, String):
            return node.value

        # ---------- VARIABLES ----------
        if isinstance(node, Variable):
            return self.env[node.name]

        # ---------- ASSIGNMENT ----------
        if isinstance(node, Assign):
            self.env[node.name] = self.eval(node.value)
            return None

        # ---------- INPUT / OUTPUT ----------
        if isinstance(node, Read):
            val = input(f"Enter value for {node.name}: ")
            self.env[node.name] = int(val) if val.isdigit() else val
            return None

        if isinstance(node, Print):
            print(self.eval(node.value))
            return None

        # ---------- EXPRESSIONS ----------
        if isinstance(node, BinOp):
            l = self.eval(node.left)
            r = self.eval(node.right)

            # PLUS (+) → Python-like behavior
            if node.op == 'PLUS':
                if isinstance(l, str) or isinstance(r, str):
                    return str(l) + str(r)
                return l + r

            # Other arithmetic operators (ints only)
            if node.op == 'MINUS':
                return l - r
            if node.op == 'MULT':
                return l * r
            if node.op == 'DIV':
                return l / r

        # ---------- CONDITIONS ----------
        if isinstance(node, Condition):
            l = self.eval(node.left)
            r = self.eval(node.right)

            if node.op == 'GT': return l > r
            if node.op == 'LT': return l < r
            if node.op == 'GE': return l >= r
            if node.op == 'LE': return l <= r
            if node.op == 'EQ': return l == r
            if node.op == 'NE': return l != r

        # ---------- IF / ELSE ----------
        if isinstance(node, If):
            if self.eval(node.condition):
                for s in node.body:
                    self.eval(s)
            return None

        if isinstance(node, IfElse):
            if self.eval(node.condition):
                for s in node.if_body:
                    self.eval(s)
            else:
                for s in node.else_body:
                    self.eval(s)
            return None

        # ---------- LOOP CONTROL ----------
        if isinstance(node, Break):
            raise BreakSignal()

        if isinstance(node, Continue):
            raise ContinueSignal()

        # ---------- WHILE LOOP ----------
        if isinstance(node, While):
            while self.eval(node.condition):
                try:
                    for s in node.body:
                        self.eval(s)
                except ContinueSignal:
                    continue
                except BreakSignal:
                    break
            return None