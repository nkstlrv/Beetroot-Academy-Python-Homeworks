class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None


# Stack implementation using Linked lists
class LinkedStack:

    def __init__(self, max_len):
        self.max_len = max_len
        self.head = None
        self._length = 0
        if self.max_len <= 0:
            raise ValueError("Max _length must be minimum (1)")

    def push(self, push_data):
        new_node = StackNode(push_data)
        while self._length <= self.max_len:
            new_node.next = self.head
            self.head = new_node
            self._length += 1
            if self._length > self.max_len:  # If L-stack _length exceeds maximum --> tail node is getting removed
                self._pop_tail()
            return True
        return False

    def __repr__(self):
        cur_node = self.head
        rep = "Linked Stack: "
        while cur_node:
            rep += f"{cur_node.data} --> "
            cur_node = cur_node.next
        return rep

    def _pop_tail(self):         # This method is needed in case the max _length of Stack is exceeded
        cur_node = self.head
        while cur_node.next:
            if cur_node.next.next is None:
                cur_node.next = None
            else:
                cur_node = cur_node.next
        self._length -= 1
        return True

    def empty(self):            # Checks if L-stack is empty
        if self._length == 0:
            return True
        else:
            return False

    def size(self):         # Returns _length of this L-stack
        return self._length

    def pull(self):             # Removes and returns top most element of the L-stack
        pulled = None
        cur_node = self.head
        pulled = cur_node
        self.head = cur_node.next
        self._length -= 1
        return pulled.data

    def peek(self):             # Returns top-most element but do not remove it
        return self.head.data



if __name__ == "__main__":

    stack_1 = LinkedStack(4)
    print(stack_1.empty())

    stack_1.push(1)
    stack_1.push(2)
    stack_1.push(3)
    print(stack_1.size())
    print(stack_1)

    stack_1.push(4)
    stack_1.push(5)
    stack_1.push(6)
    stack_1.push(7)

    print(stack_1)
    print(stack_1.pull())
    print(stack_1)
    # print(stack_1.peek())
    # print(stack_1)


