class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DBLLinkedList:
    # constructor
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    # Append
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.length += 1
        return True
    # Pop
    def pop(self):
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        temp = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        temp.prev = None
        self.length -=1
        return temp
    
        
    # print Doubly linked list
    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


my_dll = DBLLinkedList(2)
my_dll.append(3)
my_dll.pop()
my_dll.print()        
        