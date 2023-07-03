class Node:
    def  __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def enqueue(self, value):
        new_node = Node(value)
        if(self.length == 0):
            self.first = new_node
            self.last = new_node
            self.length = 1
        else:
            new_node.next = self.first
            self.first = new_node
        self.length += 1
        return True

    def dequeue(self):
        if(self.length == 0):
            return None
        temp = self.last
        if(self.length == 1):
            self.first = None
            self.last = None
            return temp
        curr_node = self.first
        while curr_node.next.next:
            curr_node = curr_node.next
        curr_node.next = None
        self.last = curr_node
        self.length -= 1
        return temp
    
    def print(self):
        curr_node = self.first
        while curr_node:
            print(curr_node.value, end=" ")
            curr_node = curr_node.next
        print()

        
q1 = Queue(1)

q1.enqueue(2)
q1.enqueue(3)
q1.enqueue(4)
q1.enqueue(5)
q1.print()

q1.dequeue()
q1.dequeue()
q1.print()

