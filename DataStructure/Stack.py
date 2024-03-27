class Stack:
    def __init__(self):# data가 list 형식으로 있을 때
        self.data = []

    def push(self, x): # push: data 추가
        self.data.append(x)

    def pop(self): # pop: 가장 최근 데이터 제거
        if not self.data:
            return -1
        return self.data.pop()
    
    def top(self): # top: 가장 최근 데이터 확인
        if not self.data:
            return -1
        return self.data[-1]

    def size(self): # size: 스택 원소 개수 return
        return len(self.data)

    def empty(self): # empty: 스택이 비었는가? True or False
        if not self.data:
            return 1
        return 0