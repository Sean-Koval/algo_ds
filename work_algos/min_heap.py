Class Heap:
    def __init__(self):
        self.heap = [0]
        self.size = 0
    
    def arrange(self, k):
        while k // 2 > 0:
            if self.heap[k] < self.heap[k//2]:
                