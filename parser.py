from ast_nodes import *

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def cur(self):
        return self.tokens[self.pos]

    def eat(self, t):
        if self.cur()[0] == t:
            self.pos += 1
        else:
            raise SyntaxError(f"Syntax error at line {self.cur()[2]}")

    def parse(self):
        stmts = []
        while self.pos < len(self.tokens):
            stmts.append(self.statement())
        return stmts

    def statement(self):
        tok = self.cur()

        if tok[0] == 'ID' and tok[1] == 'if':
            return self.if_stmt()

        if tok[0] == 'ID' and tok[1] == 'while':
            return self.while_stmt()

        if tok[0] == 'ID' and tok[1] == 'break':
            self.eat('ID')
            return Break()

        if tok[0] == 'ID' and tok[1] == 'continue':
            self.eat('ID')
            return Continue()

        if tok[0] == 'ID' and tok[1] == 'print':
            self.eat('ID')
            return Print(self.expr())

        if tok[0] == 'ID' and tok[1] == 'read':
            self.eat('ID')
            name = self.cur()[1]
            self.eat('ID')
            return Read(name)

        if tok[0] == 'ID' and self.tokens[self.pos+1][0] == 'ASSIGN':
            name = tok[1]
            self.eat('ID')
            self.eat('ASSIGN')
            return Assign(name, self.expr())

        raise SyntaxError(f"Invalid statement at line {tok[2]}")

    def if_stmt(self):
        self.eat('ID')  # if
        cond = self.condition()
        if_body = []
        else_body = []

        while self.pos < len(self.tokens):
            if self.cur()[0] == 'ID' and self.cur()[1] == 'else':
                self.eat('ID')
                break
            if self.cur()[0] == 'ID' and self.cur()[1] == 'end':
                self.eat('ID')
                return If(cond, if_body)
            if_body.append(self.statement())

        while self.pos < len(self.tokens):
            if self.cur()[0] == 'ID' and self.cur()[1] == 'end':
                self.eat('ID')
                return IfElse(cond, if_body, else_body)
            else_body.append(self.statement())

        raise SyntaxError("Missing 'end' for if")

    def while_stmt(self):
        self.eat('ID')  # while
        cond = self.condition()
        body = self.block()
        return While(cond, body)

    def block(self):
        stmts = []
        while self.pos < len(self.tokens):
            if self.cur()[0] == 'ID' and self.cur()[1] == 'end':
                self.eat('ID')
                return stmts
            stmts.append(self.statement())
        raise SyntaxError("Missing 'end' for block")

    def condition(self):
        left = self.expr()
        op = self.cur()[0]
        self.eat(op)
        right = self.expr()
        return Condition(left, op, right)

    def expr(self):
        node = self.term()
        while self.pos < len(self.tokens) and self.cur()[0] in ('PLUS', 'MINUS'):
            op = self.cur()[0]
            self.eat(op)
            node = BinOp(node, op, self.term())
        return node

    def term(self):
        node = self.factor()
        while self.pos < len(self.tokens) and self.cur()[0] in ('MULT', 'DIV'):
            op = self.cur()[0]
            self.eat(op)
            node = BinOp(node, op, self.factor())
        return node

    def factor(self):
        tok = self.cur()

        if tok[0] == 'NUMBER':
            self.eat('NUMBER')
            return Number(tok[1])

        if tok[0] == 'STRING':
            self.eat('STRING')
            return String(tok[1])

        if tok[0] == 'ID':
            self.eat('ID')
            return Variable(tok[1])

        raise SyntaxError(f"Invalid expression at line {tok[2]}")