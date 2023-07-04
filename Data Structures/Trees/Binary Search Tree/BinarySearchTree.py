class Node:
    def __init__(self, value):
        self.value = value
        self.left = None 
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        temp = self.root
        if temp is None:
            self.root = new_node
            return True
        while True:
            if(value == temp.value):
                return False
            if(value > temp.value):
                if(temp.right is None):
                    temp.right = new_node
                    return True
                temp = temp.right
            else:
                if(temp.left is None):
                    temp.left = new_node
                    return True
                temp = temp.left

    def contains(self, value):
        temp = self.root
        if temp is None:
            return False
        while temp:
            if value == temp.value:
                return True
            if value > temp.value:
                temp = temp.right
            else:
                temp = temp.left
        return False



bst1 = BinarySearchTree()
bst1.insert(76)
bst1.insert(21)
bst1.insert(92)
bst1.insert(105)
bst1.insert(81)
bst1.insert(12)
bst1.insert(33)


#print(bst1.root.left.right.value)

print(bst1.contains(106))