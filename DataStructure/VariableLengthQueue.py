from Node import Node
from DoubleLinkedList_JH import DoubleLinkedList_JH

class Queue:
    def __init__(self):
        self.dll = DoubleLinkedList_JH()

    def enqueue(self, value) -> bool:
        return self.dll.insert(value)

    def dequeue(self) -> Node:
        return self.dll.remove_at_last()
    
    def __len__(self):
        return self.dll.size
    
queue = Queue()
queue.enqueue(2)
queue.enqueue(4)
queue.enqueue(5)
print(queue.dequeue().data)
print(len(queue))