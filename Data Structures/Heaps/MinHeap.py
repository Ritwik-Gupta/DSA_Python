class MinHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return index*2 + 1
    
    def _right_child(self, index):
        return index*2 +2
    
    def _parent(self, index):
        return index//2 + 1
    
    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        curr_index = len(self.heap) - 1
        parent_index = self._parent(curr_index)

        #compare the current index with parent
        while curr_index > 0 and  self.heap[curr_index] < self.heap[parent_index]:
            self._swap(curr_index, parent_index)
            curr_index = parent_index
            parent_index = self._parent(curr_index)



h1 = MinHeap()

h1.insert(21)
h1.insert(32)
h1.insert(38)
h1.insert(56)
h1.insert(72)
h1.insert(99)
h1.insert(45)

print(h1.heap)