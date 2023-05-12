from task_1_hw24 import MyStack


class MyExtendedStack(MyStack):

    def __init__(self, max_len):
        self.stack = []
        super().__init__(max_len)

    def get_from_stack(self, element):
        if element not in self.stack:
            raise ValueError("No given item in stack")
        temp_list = []
        for val in self.stack:
            if val == element:
                continue
            temp_list.append(val)
        self.stack = temp_list
        return element


class MyQueue:
    def __init__(self):
        self.queue = []

    def my_append(self, value):
        self.queue.append(value)

    def my_pop(self):
        self.queue.pop(0)

    def get_from_queue(self, element):
        if element not in self.queue:
            raise ValueError("No given item in queue")
        temp_list = []
        for val in self.queue:
            if val == element:
                continue
            temp_list.append(val)
        self.queue = temp_list
        return element


if __name__ == "__main__":

    e_1 = MyExtendedStack(10)
    e_1.my_push('h')
    e_1.my_push('e')
    e_1.my_push('l')
    e_1.my_push('l')
    e_1.my_push('o')
    print(e_1.stack)

    print(e_1.get_from_stack('l'))
    print(e_1.stack)

    # q_1 = MyQueue()
    #
    # q_1.my_append(3)
    # q_1.my_append(4)
    # q_1.my_append(5)
    # q_1.my_append(6)
    # q_1.my_append(0)
    # q_1.my_append(9)
    # print(q_1.queue)
    #
    # q_1.my_pop()
    # print(q_1.queue)
    # print(q_1.get_from_queue(4))
    # print(q_1.queue)

