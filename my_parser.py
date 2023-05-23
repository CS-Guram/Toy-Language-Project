# Guram Kutaladze
from my_tokenizer import Tokenizer

class Parser:    
    """ -This code initializes the Parser by loading the program into the Tokenizer, 
    which breaks it down into individual tokens. Then, the parsing process begins from the program level"""
    def __init__(self, text):
        self.t = Tokenizer(text)
        self.current_token = {}
        self.symbol_table = {}
        self.program()

    # -This line of code reads the next token from the Tokenizer and stores it in the variable called current_token.
    def consume_token(self):
        self.current_token = self.t.read_next_token()

    # check if the next token matches the expected_token
    def match(self, expected_token):
        if self.current_token['type'] != expected_token:
            raise Exception('Syntax Error: expected ' + expected_token +
                            ' but found type ' + self.current_token['type'])

    # parse program
    def program(self):
        while True:
            self.assignment()
            if self.current_token['type'] == 'EOF':
                break

    # -the code block is responsible for parsing assignment statements in the program.
    def assignment(self):
        self.consume_token()
        if self.current_token['type'] == 'Id':
            var_name = self.current_token['token']
            self.consume_token()
            self.match('=')
            expr = self.expr()
            self.match(';')
            self.symbol_table[var_name] = expr
            return

    # parse expressions
    def expr(self):
        t = self.term()
        return t + self.expr_p()

    # used to eliminate left recursion when parsing expressions
    def expr_p(self):
        if self.current_token['type'] == '+':
            t = self.term()
            return t + self.expr_p()
        elif self.current_token['type'] == '-':
            t = self.term()
            return (-1 * t) + self.expr_p()
        else:
            return 0

    # -parsing terms
    def term(self):
        f = self.factor()
        return f * self.term_p()

    #  -It is used to eliminate left recursion when parsing terms.
    def term_p(self):
        self.consume_token()
        if self.current_token['type'] == '*':
            f = self.factor()
            return f * self.term_p()
        else:
            return 1

    # -This method parses factors in the expression
    def factor(self):
        self.consume_token()
        if self.current_token['type'] == 'Lit':
            return int(self.current_token['token'])
        elif self.current_token['type'] == 'Id':
            if self.current_token['token'] in self.symbol_table:
                return self.symbol_table.get(self.current_token['token'])
            else:
                raise Exception('Error: uninitialized variable ' + self.current_token['token'])
        elif self.current_token['type'] == '+':
            return self.factor()
        elif self.current_token['type'] == '-':
            return -1 * self.factor()
        elif self.current_token['type'] == '(':
            exp = self.expr()
            self.match(')')
            return exp
