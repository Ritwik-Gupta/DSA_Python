import math

class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2*index + 1
    
    def _right_child(self, index):
        return 2*index + 2
    
    def _parent(self, index):
        return int(index/2)
    
    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def print(self):
        print(self.heap)

    def insert(self, value):
        self.heap.append(value)
        current_index = len(self.heap) - 1
        parent_index = self._parent(current_index)

        while current_index > 0 and self.heap[current_index] > self.heap[parent_index]:
            self._swap(current_index, parent_index)
            current_index = parent_index
            parent_index = self._parent(current_index)
            
        return True
    
    # def print_like_tree(self):
    #     levels = math.floor(math.log(len(self.heap),2) + 1)
    #     curr_node = self.heap[0]
    #     size = len(self.heap)
    #     for i in range(levels):

    def _sink(self, index):
        max_index = index
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if left_index < len(self.heap) and self.heap[left_index] > self.heap[max_index]:
                max_index = left_index

            if right_index < len(self.heap) and self.heap[right_index] > self.heap[max_index]:
                max_index = right_index

            if(max_index != index):
                self._swap(max_index, index)
                index = max_index
            else:
                return

    def remove(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop(0)
        
        self.heap[0] = self.heap.pop()
        self._sink(0)
            


myheap = MaxHeap()

myheap = MaxHeap()
myheap.insert(99)
myheap.insert(72)
myheap.insert(61)
myheap.insert(58)
myheap.print()

myheap.insert(100)
myheap.print()

myheap.insert(75)
myheap.print()