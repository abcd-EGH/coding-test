class Stack:
    def __init__(self, capacity: int):# data가 list 형식으로 있을 때
        self.capacity = capacity
        self.data = [None] * capacity
        self.top = -1

    def push(self, x) -> None: # push: data 추가
        if not self.isFull():
            self.top += 1
            self.data[self.top] = x
        else:
            raise IndexError("Can't push anymore. Need to increase capacity.")

    def pop(self): # pop: 가장 최근 데이터 제거
        if self.isEmpty():
            return -1
        else:
            temp = self.data[self.top]
            self.data[self.top] = None
            self.top -= 1
            return temp
            
    def peek(self): # peek: 가장 최근 데이터 확인
        if self.isEmpty():
            return -1
        else:
            return self.data[self.top]

    def size(self) -> int: # size: 스택 원소 개수 return
        return len(self)

    def isEmpty(self) -> bool: # empty: 스택이 비었는가? True or False
        if self.top == -1:
            return True
        return False
    
    def isFull(self) -> bool:
        return self.top == self.capacity - 1

    def __len__(self) -> int:
        return self.top + 1


def checkBracket(statement):
    stack = Stack(len(statement))
    leftBracket = '[{('
    rightBracket = ']})'
    for s in statement:
        if s in leftBracket:
            stack.push(s)
        elif s in rightBracket:
            if len(stack) == 0:
                print("Bracket Error 2")
                return
            check = stack.pop()
            if check != leftBracket[rightBracket.index(s)]:
                print("Bracket Error 3")
                return
    if len(stack) != 0:
        print("Bracket Error 1")
    else:
        print("Perfect.")
    return