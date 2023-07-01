class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def append(self, value):
        new_node = Node(value)
        if(self.length == 0):
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if(self.length > 0):
            temp = self.tail
            if(self.length == 1):
                self.head = None
                self.tail = None
            else:
                #getting the 2nd last item
                self.tail = temp.prev
                self.tail.next = None
                temp.prev = None
            self.length -= 1
            return temp
        return None

    def prepend(self, value):
        new_node = Node(value)
        if(self.length == 0):
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if(self.length > 0):
            temp = self.head
            if(self.length == 1):
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
                temp.prev = None
            self.length -= 1
            return temp
        return None
    
    def get(self, idx):
        if(idx < 0  or idx >= self.length):
            return None
        else:
            if(idx == 0):
                return self.head
            if(idx == self.length-1):
                return self.tail
            curr_node = self.head
            for _ in range(idx):
                curr_node = curr_node.next
            return curr_node
        
    def set(self, idx, value):
        if(idx < 0  or idx >= self.length):
            return None
        else:
            curr_node = self.get(idx)
            curr_node.value = value
            return True


    def print(self):
        curr_node = self.head
        while(curr_node != None):
            print(curr_node.value, end=" ")
            curr_node = curr_node.next
        print()


l1 = DoublyLinkedList(0)

l1.append(1)
l1.append(2)
l1.append(3)
l1.append(4)
l1.append(5)
l1.append(6)
l1.print()

l1.pop_first()
l1.pop_first()
l1.print()

l1.set(4,44)
l1.print()

