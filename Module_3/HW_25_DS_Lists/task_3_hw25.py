class QueueNode:
    def __init__(self, data):
        self.next = None
        self.data = data


# Queue implementation using Linked lists
class LinkedQueue:
    def __init__(self):
        self._length = 0
        self.head = None
        self.length = 0

    def append(self, data):
        new_node = QueueNode(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1
        return True

    def __repr__(self):
        cur_node = self.head
        rep = "Linked Queue: "
        while cur_node:
            rep += f"{cur_node.data} --> "
            cur_node = cur_node.next
        return rep

    def pop_queue(self):        # pop method FIFO
        cur_node = self.head
        pop_item = None
        while cur_node.next:
            if cur_node.next.next is None:
                pop_item = cur_node.next
                cur_node.next = None
            else:
                cur_node = cur_node.next
        self.length -= 1
        return pop_item.data

    def front(self):    # Returns front item of the L-queue (head)
        return self.head.data

    def rear(self):        # Returns rear item of the L-queue (tail)
        cur_node = self.head
        while cur_node:
            if cur_node.next is None:
                return cur_node.data
            else:
                cur_node = cur_node.next





if __name__ == "__main__":

    queue_1 = LinkedQueue()
    queue_1.append(1)
    queue_1.append(2)
    queue_1.append(3)
    queue_1.append(4)
    queue_1.append(5)
    queue_1.append(6)
    print(queue_1)
    print(queue_1.pop_queue())
    print(queue_1)
    print(queue_1.front())
    print(queue_1.rear())

