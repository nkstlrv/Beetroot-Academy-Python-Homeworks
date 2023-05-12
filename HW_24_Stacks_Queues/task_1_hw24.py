class MyStack:

    def __init__(self, max_len):
        self.max_len = max_len
        self.stack = []

    def my_push(self, my_char):
        if len(self.stack) < self.max_len:
            self.stack.append(my_char)
        else:
            self.stack.pop(0)
            self.stack.append(my_char)

    def my_reverse_push(self, my_char):
        if len(self.stack) < self.max_len:
            self.stack.insert(0, my_char)
        else:
            self.stack.pop()
            self.stack.insert(0, my_char)

    def my_pull(self):
        self.stack.pop()

    def my_reverse_pull(self):
        self.stack.pop(0)

    def my_is_empty(self):
        return len(self.stack) == 0


if __name__ == "__main__":
    s_1 = MyStack(5)

    s_1.my_push('1')
    s_1.my_push('2')
    s_1.my_push('3')
    s_1.my_push('4')
    s_1.my_push('5')
    s_1.my_push('6')

    print(s_1.stack)

    s_1.my_pull()
    s_1.my_pull()

    print(s_1.stack)

    s_2 = MyStack(5)

    s_2.my_reverse_push('h')
    s_2.my_reverse_push('e')
    s_2.my_reverse_push('l')
    s_2.my_reverse_push('l')
    s_2.my_reverse_push('o')

    print(s_2.stack)

    s_2.my_reverse_push('7')
    s_2.my_reverse_push('8')
    print(s_2.stack)

    s_2.my_reverse_pull()
    print(s_2.stack)

    print(s_2.my_is_empty())
