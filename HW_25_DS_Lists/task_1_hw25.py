class MyNode:

    def __init__(self, data):
        self.data = data
        self.next = None  # This is a link to the previously added node; If None -> this is the tail


# Class to store our Nodes
class LinkedList:
    def __init__(self):
        self.head = None  # Will represent the newest Node instance
        self.length = 0

    # Add new item in the Linked list method
    def append(self, data):
        new_node = MyNode(data)  # Creating new Node class
        new_node.next = self.head  # Assigning a link for current Node
        self.head = new_node  # The head is now the newest created Node
        self.length += 1

    def __repr__(self):
        current_node = self.head  # This is the news Node of the list
        text = "Linked list: "
        while current_node:  # If current Node != to Node we iterate
            text += f"{current_node.data} -> "  # Appending node data to result string
            current_node = current_node.next  # Changing current node to the next one by the link we've created
        return text

    # Get index of given item method
    def get_index(self, data):
        current_node = self.head
        index = 0  # Creating variable index
        while current_node:
            if self.head.data == data:  # If head's data is needed we return 0
                return 0
            if current_node.data == data:
                return index
            else:
                current_node = current_node.next
                index += 1  # Increasing index by one each element iterated
        return False  # If no object found

    # Pop method
    def pop(self, index):
        current_node = self.head
        prev_node = None
        pop_index = 0  # Will be comparing given index with this one
        while current_node:
            if index == pop_index:
                if prev_node:
                    prev_node.next = current_node.next  # Link of previous node becomes ours link for the next
                else:
                    self.head = current_node.next
                self.length -= 1  # When data was removed, _length of the list decreased
                return current_node.data  # Returning removed data
            else:
                pop_index += 1  # iterating through Linked list
                prev_node = current_node
                current_node = current_node.next
        return False  # Returning False if data not found

    # Insert method
    def insert(self, index, new_data):

        cur_node = self.head
        prev_node = None
        cur_index = 0

        new_node = MyNode(new_data)  # Creating new Node

        while cur_node:
            if cur_index == index:
                if prev_node:                       # If we are somewhere in the middle of the Linked list
                    new_node.next = cur_node        # New Node's link becomes current Node
                    prev_node.next = new_node       # Previous Node's link becomes new Node
                else:                               # If we are at the head
                    new_node.next = self.head       # New Node's next becomes head
                    self.head = new_node        # Head becomes new Node
                self.length += 1
                return True
            else:
                cur_index += 1
                prev_node = cur_node            # Iterating through the L-list
                cur_node = cur_node.next
        return False                # Returning False if haven't found data

    # Method returns a slice of L-list
    def slice(self, start, end):
        if start >= end:
            raise ValueError("Impossible slicing")
        if end > self.length:
            raise IndexError("Ending is out of range")
        index = 0
        cur_node = self.head

        temp_list = []              # Temporary list that stores nodes data after slicing

        while index != end:
            if start <= index:
                temp_list.append(cur_node.data)         # Appending to temp list
            index += 1
            cur_node = cur_node.next
        temp_list.reverse()                 # Making this list reversed

        for i, n_data in enumerate(temp_list):
            new_node = MyNode(n_data)               # Creating new Node
            if i == 0:
                new_node.next = None        # If new node is first one, next link is None
                self.head = new_node
            else:
                new_node.next = self.head
                self.head = new_node
        return self                      # Returning representation of Linked List


if __name__ == "__main__":
    l_1 = LinkedList()
    l_1.append(1)
    l_1.append(2)
    l_1.append(3)
    l_1.append(4)
    print(l_1)

    print(l_1.slice(1, 3))
