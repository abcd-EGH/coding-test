from CircularQueue import CircularQueue

class CircularDeque(CircularQueue):
    def __init__(self, capacity: int):
        super().__init__(capacity)
    
    def addRear(self, value): self.enqueue(value)
    def deleteFront(self): return self.dequeue()
    def getFront(self): return self.peek()

    def addFront(self, value):
        if self.isFull():
            return False
        
        self.data[self.front] = value
        self.front = (self.front - 1 + self.capacity) % self.capacity

    def deleteRear(self):
        if self.isEmpty():
            raise IndexError("Can't deleteRear anymore. There is no data.")
        
        temp = self.data[self.rear]
        self.data[self.rear] = None
        self.rear = (self.rear - 1 + self.capacity) % self.capacity
        return temp
    
    def getRear(self):
        if not self.isEmpty():
            return self.data[self.rear]
