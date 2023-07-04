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
        while temp:
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

bst1 = BinarySearchTree()
bst1.insert(1)
bst1.insert(2)
bst1.insert(0)


print(bst1.root.value)
print(bst1.root.right.value)
print(bst1.root.left.value)
