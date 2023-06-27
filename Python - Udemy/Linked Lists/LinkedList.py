#Creates a node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None    

class LinkedList:
    def __init__(self, value):
        self.value = Node(value)
        self.head =  self.value
        self.tail = self.value
        self.length = 1

    def prepend(self, value):
        new_node = Node(value)
        if(self.head == None):
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1

    def append(self, value):
        new_node = Node(value)
        if(self.head == None):
            self.head =  new_node
            self.tail = new_node
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    def pop(self):
        if(self.head is not None):
            curr_node = self.head
            temp = curr_node
            if(curr_node.next is None): #LL with only 1 node
                self.head = None
                self.tail = None
            else:
                while(curr_node.next.next is not None): #getting the 2nd last node
                    curr_node = curr_node.next

                temp = curr_node.next
                self.tail = curr_node
                curr_node.next = None

            self.length -= 1
            return temp
        else:
            return None


    def popFirst(self):
        if(self.length > 0):
            temp = self.head
            if(self.head.next is None):
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
            self.length -= 1
            return temp
        else:
            return None
    
    def get(self, idx):
        curr_node = self.head
        if(idx < 0 or idx >= self.length or curr_node is None):
            return None
        else:
            for _ in range(idx):
                curr_node = curr_node.next 
            return curr_node 
        
    def set_value(self, idx, value):
        temp = self.get(idx)
        if temp is not None:
            temp.value = value

    def print(self):
        curr_node = self.head
        while(curr_node != None):
            print(curr_node.value, end=" ")
            curr_node = curr_node.next
        print()


l1 = LinkedList(3)

l1.append(4)
l1.append(5)
l1.append(6)

l1.print()

l1.set_value(1,0)
l1.print()

l1.set_value(3,9)
l1.print()

