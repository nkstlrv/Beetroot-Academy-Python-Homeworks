class Queue:

    def __init__(self):
        self.sequence = []

    def append(self, value):
        self.sequence.append(value)

    def pull(self):
        self.sequence.pop(0)

    def check_balance(self):

        open_brackets = ('(', '[', '{')

        if any(item in open_brackets for item in self.sequence):
            open_parentheses_count = self.sequence.count('(')
            close_parentheses_count = self.sequence.count(')')
            open_braces_count = self.sequence.count('[')
            close_braces_count = self.sequence.count(']')
            open_curly_count = self.sequence.count('{')
            close_curly_count = self.sequence.count('}')

            if (open_parentheses_count != close_parentheses_count or open_braces_count != close_braces_count or
                    open_curly_count != close_curly_count):
                raise ValueError("Brackets are not balances")

            elif (open_parentheses_count != 0
                  and open_braces_count == 0 and open_curly_count == 0):
                if self.sequence.index('(') > self.sequence.index(')'):
                    raise ValueError("Brackets are not balances")

            elif (open_parentheses_count == 0
                  and open_braces_count != 0 and open_curly_count == 0):
                if self.sequence.index('[') > self.sequence.index(']'):
                    raise ValueError("Brackets are not balances")

            elif (open_parentheses_count == 0
                  and open_braces_count == 0 and open_curly_count != 0):
                if self.sequence.index('{') > self.sequence.index('}'):
                    raise ValueError("Brackets are not balances")

            elif (open_parentheses_count != 0
                  and open_braces_count != 0 and open_curly_count == 0):
                if (self.sequence.index('(') > self.sequence.index(')')
                        or self.sequence.index('[') > self.sequence.index(']')):
                    raise ValueError("Brackets are not balances")

            elif (open_parentheses_count != 0
                  and open_braces_count == 0 and open_curly_count != 0):
                if (self.sequence.index('(') > self.sequence.index(')')
                        or self.sequence.index('{') > self.sequence.index('}')):
                    raise ValueError("Brackets are not balances")

            elif (open_parentheses_count == 0
                  and open_braces_count != 0 and open_curly_count != 0):
                if (self.sequence.index('[') > self.sequence.index(']')
                        or self.sequence.index('{') > self.sequence.index('}')):
                    raise ValueError("Brackets are not balances")

            elif (open_parentheses_count == 0
                  and open_braces_count == 0 and open_curly_count == 0):
                if (self.sequence.index('(') > self.sequence.index(')')
                        or self.sequence.index('[') > self.sequence.index(']')
                        or self.sequence.index('{') > self.sequence.index('}')):
                    raise ValueError("Brackets are not balances")

            return "Sequence is balanced"
        else:
            raise ValueError("No OPEN brackets detected")


if __name__ == "__main__":
    q = Queue()

    q.append(1)
    q.append(2)
    q.append(3)
    q.append('{')
    q.append('}')
    q.append('{')
    q.append('}')
    q.append('(')
    q.append('(')
    q.append(')')
    q.append('')

    q.check_balance()
    print(q.sequence)

    # q_2 = Queue()
    #
    # q_2.append(']')
    # q_2.check_balance()
