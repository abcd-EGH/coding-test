class CircularQueue:
    def __init__(self, capacity: int):
        self.capacity = capacity # capacity개의 원소를 저장하는 원형 큐 초기화
        self.data = [None] * self.capacity # 버퍼인 data는 capacity+1의 [0]을 지니도록 생성
        self.front = 0 # 첫번째 요소 바로 이전 위치(인덱스)
        self.rear = 0 # 마지막 요소 위치(인덱스)

    def enqueue(self, value) -> bool:
        if self.isFull(): # 큐가 가득 찼을 때 enqueue 수행 시 False를 return
            return False

        self.rear = (self.rear + 1) % self.capacity # rear 위치 수정 (1만큼 증가)
        self.data[self.rear] = value # rear가 가르키는 위치에 값 저장
        return True

    def dequeue(self) -> bool:
        if self.isEmpty(): # 큐가 비었을 때 dequeue 수행 시 False를 return
            raise IndexError("Can't dequeue anymore. There is no data.")

        self.front = (self.front + 1) % self.capacity # front 위치 수정 (1만큼 증가)
        self.data[self.front] = None # front가 가르키는 data 삭제
        return True

    def isEmpty(self) -> bool:
        return self.front == self.rear

    def isFull(self) -> bool:
        return self.front == (self.rear + 1) % self.capacity
    
    def peek(self):
        if not self.isEmpty():
            return self.data[self.front+1]
    
    def size(self):
        return (self.rear - self.front + self.capacity) % self.capacity
    
    def display(self):
        for i in range(self.front+1, self.front+1+self.size()):
            print(self.data[i%self.capacity], end=' ')
        print()

class RingQueue(CircularQueue):
    def enqueue(self, value):
        self.rear = (self.rear + 1) % self.capacity # rear 위치 수정 (1만큼 증가)
        self.data[self.rear] = value # rear가 가르키는 위치에 값 저장
        if self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            self.data[self.front] = None # front가 가르키는 data 삭제