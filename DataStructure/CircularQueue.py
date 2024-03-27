class CircularQueue:
    def __init__(self, k: int):
        self.n = k + 1 # k개의 원소를 저장하는 원형 큐 초기화 시, 버퍼인 data는 k+1의 [0]을 지니도록 생성
        self.data = [0] * self.n
        self.front = 0
        self.rear = 0

    def enqueue(self, value: int) -> bool:
        if self.isFull(): # 큐가 가득 찼을 때 enqueue 수행 시 False를 return
            return False

        self.data[self.front] = value # 값 저장 시, data에서 front 인덱스가 가리키는 버퍼에 저장
        self.front = (self.front + 1) % self.n # front 위치 수정 (1만큼 증가)
        return True 

    def dequeue(self) -> bool:
        if self.isEmpty(): # 큐가 비었을 때 dequeue 수행 시 False를 return
            return False

        self.rear = (self.rear + 1) % self.n # rear 위치 수정 (1만큼 증가)
        return True
        
    def front(self) -> int:
        if self.isEmpty():
            return -1

        return self.data[self.rear]

    def rear(self) -> int:
        if self.isEmpty():
            return -1

        return self.data[self.front - 1] 

    def is_empty(self) -> bool:
        return self.front == self.rear

    def is_full(self) -> bool:
        return (self.front + 1) % self.n == self.rear # 큐가 가득 찼는지 여부 확인