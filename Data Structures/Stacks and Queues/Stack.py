class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def push(self,value):
        new_node = Node(value)
        if(self.height == 0):
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
    
    def pop(self):
        if(self.height == 0):
            return None 
        temp = self.top
        self.top = self.top.next
        self.height -= 1
        temp.next = None
        return temp

    def print(self):
        curr_node = self.top
        print("===")
        while curr_node:
            print(curr_node.value)
            curr_node = curr_node.next
        print("===")


s1 = Stack(1)

s1.push(2)
s1.push(3)
s1.push(4)
s1.push(5)

s1.print()