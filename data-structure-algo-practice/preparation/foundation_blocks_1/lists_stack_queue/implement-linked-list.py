# Node class
class Node:
    
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def push(self,value):
        node = Node(value)
        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1
        
    def search(self, value):
        current = self.head
        while current != None:
            if current.data == value:
                return current
            else:
                current = current.next
        raise Exception('Value does not exist')
        
    def print(self):
        current = self.head
        while current != None:
            print(current.data)
            current = current.next
    
    def reverse(self):
        current = linked_list.head
        reversed_head = None
        forward_head = current
        
        while current != None:
            forward_head = current.next
            current.next = reversed_head
            reversed_head = current
            current = forward_head
        
        return reversed_head