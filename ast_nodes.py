class Number:
    def __init__(self, value): self.value = value

class String:
    def __init__(self, value): self.value = value

class Variable:
    def __init__(self, name): self.name = name

class BinOp:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class Assign:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class Print:
    def __init__(self, value):
        self.value = value

class Read:
    def __init__(self, name):
        self.name = name

class Condition:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class If:
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

class IfElse:
    def __init__(self, condition, if_body, else_body):
        self.condition = condition
        self.if_body = if_body
        self.else_body = else_body

class While:
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

class Break:
    pass

class Continue:
    pass