class MaxHeap:
    def __init__(self, items = []):
        self.heap = [0]
        for i in items:
            self.heap.append(i)
            self.float_up(len(self.heap) - 1)
            
    def float_up(self, index):
        parent = index // 2
        if index <= 1:
            return
        elif self.heap[index] > self.heap[parent]:
            self.swap(index, parent)
            self.float_up(parent)
    
    def push(self, value):
        self.heap.append(value)
        self.float_up(len(self.heap) - 1)
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def peek(self): # returns the maximum value of the Heap
        if self.heap[1]:
            return self.heap[1]
        else:
            print("No root to return")
    
    def pop(self):
        if len(self.heap) > 2:
            self.swap(1, len(self.heap))  #
            max = self.heap.pop()         #
            self.bubble_down(1)            #
        
        elif len(self.heap) == 2:
            max = self.heap.pop()
        else:
            max = False
            print("No data to remove")
    
    def bubble_down(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:            #
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:          # 
            largest = right 
        if largest != index:
            self.swap(index, largest)                                                 #
            self.bubble_down(largest)                                                 #
        
    
m = MaxHeap([95, 3, 21])
m.push(10)
print(str(m.heap))
#print(str(m.pop()))

##Learn bubble down and pop
