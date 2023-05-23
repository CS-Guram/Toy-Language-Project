import re

class Tokenizer:

    """ -The code defines a dictionary that assigns a type (such as "=" or "Id") to each terminal 
    symbol in the toy language, along with a compiled regular expression that matches the 
    corresponding terminal symbol in the input program. This dictionary is used by the parser to
    recognize and classify the input tokens as it parses the program. """
    tokens = {'=': re.compile(r'='), 
              ';': re.compile(r';'), 
              '+': re.compile(r'\+'), 
              '-': re.compile(r'-'), 
              '*': re.compile(r'\*'),  
              '(': re.compile(r'\('),
              ')': re.compile(r'\)'), 
              'Id': re.compile(r'[a-zA-Z_]([a-zA-Z_]|[0-9])*'), # -This line assigns the regular expression for identifiers (variable names) to the key "Id" in the tokens dictionary.
              'Lit': re.compile(r'0|[1-9][0-9]*'), # -This line assigns the regular expression for integer literals to the key "Lit" in the tokens dictionary
              'Inv': re.compile('.')} # -This line assigns a regular expression that matches any single character to the key "Inv" in the tokens dictionary

    # -Regular expression matches whitespace characters that should be removed from the input text
    whitespace = re.compile(r'\s+')

    # -initialize tokenizer by removing whitespace from text and creating variables to track the current position
    # -in the text, as well as the length of the text
    def __init__(self, text):
        self.text = re.sub(self.whitespace, '', text)
        self.endPosition = len(self.text)
        self.currentPosition = 0

    # read the next token that starts from currentPosition and return the token and its type
    def read_next_token(self):
        if self.currentPosition < self.endPosition:
            for pattern in self.tokens:
                # for all regex patterns in tokens dictionary, check for a match at current position
                match = self.tokens[pattern].match(self.text, self.currentPosition)
                if match:
                    if pattern == 'Inv':
                        # catch anything that does not match another pattern in tokens
                        raise Exception('ERROR: unrecognized character ' + self.text[match.start():match.end()])
                    else:
                        # return dictionary containing token (as a string) and the pattern type
                        self.currentPosition = match.end()
                        return {'token': self.text[match.start():match.end()], 'type': pattern}
        else:
            # if end of text is reached, return an EOF token
            return {'token': '', 'type': 'EOF'}
