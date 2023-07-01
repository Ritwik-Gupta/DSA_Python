# LL: Find Middle Node ( ** Interview Question)
# Implement the find_middle_node method for the LinkedList class.

# The find_middle_node method should return the middle node in the linked list WITHOUT using the length attribute.

# If the linked list has an even number of nodes, return the first node of the second half of the list.

# Keep in mind the following requirements:

# The method should use a two-pointer approach, where one pointer (slow) moves one node at a time and the other pointer (fast) moves two nodes at a time.

# When the fast pointer reaches the end of the list or has no next node, the slow pointer should be at the middle node of the list.

# The method should return the middle node or the first node of the second half of the list if the list has an even number of nodes.

# The method should only traverse the linked list once.  In other words, you can only use one loop.


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
        
    def find_middle_node(self):
        p1 = self.head
        p2 = self.head
        while(p1 != None and p2.next != None):
            p1 = p1.next
            p2 = p2.next.next
            if(p2 is None):
                return p1
        return p1
            
        




my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

print( my_linked_list.find_middle_node().value )



"""
    EXPECTED OUTPUT:
    ----------------
    3
    
"""